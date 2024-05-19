from statsbombpy import sb
from snowflake_connection import get_connection

# Establish connection
conn = get_connection()
cur = conn.cursor()

# Load matches data
matches = sb.matches(competition_id=37, season_id=90)

# Insert data into matches table
for index, row in matches.iterrows():
    cur.execute(
        "INSERT INTO statsbomb_schema.matches (match_id, competition_id, season_id, match_date, home_team_id, away_team_id, home_score, away_score, venue_name, referee_name) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
        (row['match_id'], row['competition_id'], row['season_id'], row['match_date'], row['home_team_id'], row['away_team_id'], row['home_score'], row['away_score'], row['venue_name'], row['referee_name'])
    )

# Close the connection
cur.close()
conn.close()