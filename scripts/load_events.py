import json
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

events = sb.events(match_id=3788741)
for event in events:
    event_data = json.dumps(event)
    cursor.execute("INSERT INTO events (match_id, team_id, player_id, type, timestamp, minute, second, possession, location, related_events, event_data) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, ST_GeomFromText(%s), %s, %s)", (
        event['match_id'],
        event['team_id'],
        event.get('player_id', None),
        event['type']['name'],
        event['timestamp'],
        event['minute'],
        event['second'],
        event['possession'],
        f"POINT({event['location'][0]} {event['location'][1]})" if 'location' in event else None,
        json.dumps(event.get('related_events', [])),
        event_data
    ))

conn.commit()
cursor.close()
conn.close()