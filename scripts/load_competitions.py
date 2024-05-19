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

competitions = sb.competitions()
competitions.to_sql(name='competitions', con=conn, if_exists='replace', index=False)

conn.commit()
cursor.close()
conn.close()