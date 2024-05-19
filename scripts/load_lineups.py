from statsbombpy import sb
from snowflake_connection import get_connection

# Establish connection
conn = get_connection()
cur = conn.cursor()

# Load lineups data
lineups = sb.lineups(match_id=3788741)

# Insert data into lineups table
for index, row in lineups.iterrows():
    cur.execute(
        "INSERT INTO statsbomb_schema.lineups (lineup_id, match_id, team_id, player_id, starting_position, jersey_number) VALUES (%s, %s, %s, %s, %s, %s)",
        (row['lineup_id'], row['match_id'], row['team_id'], row['player_id'], row['starting_position'], row['jersey_number'])
    )

# Close the connection
cur.close()
conn.close()