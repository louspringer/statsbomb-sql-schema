import pandas as pd
from statsbombpy import sb
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="statsbomb"
)
cursor = conn.cursor()

teams = sb.teams(competition_id=37, season_id=90)
teams.to_sql(name='teams', con=conn, if_exists='replace', index=False)

conn.commit()
cursor.close()
conn.close()