from statsbombpy import sb
from snowflake_connection import get_connection

# Establish connection
conn = get_connection()
cur = conn.cursor()

# Load seasons data
seasons = sb.seasons()

# Insert data into seasons table
for index, row in seasons.iterrows():
    cur.execute(
        "INSERT INTO statsbomb_schema.seasons (season_id, season_name, competition_id) VALUES (%s, %s, %s)",
        (row['season_id'], row['season_name'], row['competition_id'])
    )

# Close the connection
cur.close()
conn.close()