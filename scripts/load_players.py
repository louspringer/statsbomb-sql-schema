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

players = sb.players(match_id=3788741)
players.to_sql(name='players', con=conn, if_exists='replace', index=False)

conn.commit()
cursor.close()
conn.close()