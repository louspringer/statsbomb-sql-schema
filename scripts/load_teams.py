from statsbombpy import sb
from snowflake_connection import get_connection

# Establish connection
conn = get_connection()
cur = conn.cursor()

# Load teams data
teams = sb.teams()

# Insert data into teams table
for index, row in teams.iterrows():
    cur.execute(
        "INSERT INTO statsbomb_schema.teams (team_id, team_name) VALUES (%s, %s)",
        (row['team_id'], row['team_name'])
    )

# Close the connection
cur.close()
conn.close()