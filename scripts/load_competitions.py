from statsbombpy import sb
from snowflake_connection import get_connection

# Establish connection
conn = get_connection()
cur = conn.cursor()

# Load competitions data
competitions = sb.competitions()

# Insert data into competitions table
for index, row in competitions.iterrows():
    cur.execute(
        "INSERT INTO statsbomb_schema.competitions (competition_id, competition_name, country_name, competition_gender) VALUES (%s, %s, %s, %s)",
        (row['competition_id'], row['competition_name'], row['country_name'], row['competition_gender'])
    )

# Close the connection
cur.close()
conn.close()