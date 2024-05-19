import json
from statsbombpy import sb
from snowflake_connection import get_connection
import pandas as pd

# Define expected columns based on the Snowflake table schema
expected_columns = [
    'event_id', 'match_id', 'team_id', 'player_id', 'type', 'timestamp',
    'minute', 'second', 'possession', 'location', 'related_events'
]

# Establish connection
conn = get_connection()
cur = conn.cursor()

# Load events data
events = sb.events(match_id=3788741)

# Extract column names from the DataFrame
dataframe_columns = events.columns.tolist()
print(dataframe_columns)

# Check if all expected columns are present in the DataFrame
missing_columns = [col for col in expected_columns if col not in dataframe_columns]

if missing_columns:
    raise ValueError(f"Missing columns in DataFrame: {missing_columns}")

# Check for any additional columns in the DataFrame not expected in the table schema
additional_columns = [col for col in dataframe_columns if col not in expected_columns + ['event_id', 'event_data']]

if additional_columns:
    raise ValueError(f"Additional unexpected columns in DataFrame: {additional_columns}")

# Insert data into events table
for index, row in events.iterrows():
    event_data = json.dumps(row.to_dict())
    cur.execute(
        """
        INSERT INTO statsbomb_schema.events (
            event_id, match_id, team_id, player_id, type, timestamp, minute, second,
            possession, location, related_events, event_data
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, ST_GeomFromText(%s), %s, %s)
        """,
        (
            row['event_id'], row['match_id'], row['team_id'], row['player_id'], row['type'], row['timestamp'], row['minute'],
            row['second'], row['possession'], f"POINT({row['location'][0]} {row['location'][1]})" if 'location' in row else None,
            json.dumps(row['related_events']), event_data
        )
    )

# Close the connection
cur.close()
conn.close()