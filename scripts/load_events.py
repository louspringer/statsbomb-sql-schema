import json
from statsbombpy import sb
from snowflake_connection import get_connection

# Establish connection
conn = get_connection()
cur = conn.cursor()

# Load events data
events = sb.events(match_id=3788741)

# Insert data into events table
for index, row in events.iterrows():
    event_data = json.dumps(row.to_dict())
    cur.execute(
        "INSERT INTO statsbomb_schema.events (event_id, match_id, team_id, player_id, type, timestamp, minute, second, possession, location, related_events, event_data) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, ST_GeomFromText(%s), %s, %s)",
        (row['event_id'], row['match_id'], row['team_id'], row['player_id'], row['type'], row['timestamp'], row['minute'], row['second'],
         row['possession'], f"POINT({row['location'][0]} {row['location'][1]})" if 'location' in row else None, json.dumps(row['related_events']), event_data)
    )

# Close the connection
cur.close()
conn.close()