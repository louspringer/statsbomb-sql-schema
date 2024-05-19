from statsbombpy import sb
from snowflake_connection import get_connection

# Establish connection
conn = get_connection()
cur = conn.cursor()

# Load players data
players = sb.players()

# Insert data into players table
for index, row in players.iterrows():
    cur.execute(
        "INSERT INTO statsbomb_schema.players (player_id, player_name, nickname, birth_date, country_of_birth, nationality) VALUES (%s, %s, %s, %s, %s, %s)",
        (row['player_id'], row['player_name'], row['nickname'], row['birth_date'], row['country_of_birth'], row['nationality'])
    )

# Close the connection
cur.close()
conn.close()