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

lineups = sb.lineups(match_id=3788741)
lineups.to_sql(name='lineups', con=conn, if_exists='replace', index=False)

conn.commit()
cursor.close()
conn.close()