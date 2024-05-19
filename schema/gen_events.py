import json
from statsbombpy import sb
import pandas as pd
from snowflake_connection import get_connection

# Establish connection
conn = get_connection()
cur = conn.cursor()

# Fetch events data
events = sb.events(match_id=3788741)

# Extract column names from the DataFrame
columns = events.columns.tolist()

# Map DataFrame columns to Snowflake data types
column_types = {
    'ball_receipt_outcome': 'VARCHAR',
    'ball_recovery_offensive': 'BOOLEAN',
    'ball_recovery_recovery_failure': 'BOOLEAN',
    'block_deflection': 'BOOLEAN',
    'carry_end_location': 'VARIANT',
    'clearance_aerial_won': 'BOOLEAN',
    'clearance_body_part': 'VARCHAR',
    'clearance_head': 'BOOLEAN',
    'clearance_left_foot': 'BOOLEAN',
    'clearance_right_foot': 'BOOLEAN',
    'counterpress': 'BOOLEAN',
    'dribble_nutmeg': 'BOOLEAN',
    'dribble_outcome': 'VARCHAR',
    'dribble_overrun': 'BOOLEAN',
    'duel_outcome': 'VARCHAR',
    'duel_type': 'VARCHAR',
    'duration': 'FLOAT',
    'foul_committed_advantage': 'BOOLEAN',
    'foul_committed_card': 'VARCHAR',
    'foul_won_advantage': 'BOOLEAN',
    'foul_won_defensive': 'BOOLEAN',
    'goalkeeper_body_part': 'VARCHAR',
    'goalkeeper_end_location': 'VARIANT',
    'goalkeeper_outcome': 'VARCHAR',
    'goalkeeper_position': 'VARCHAR',
    'goalkeeper_punched_out': 'BOOLEAN',
    'goalkeeper_technique': 'VARCHAR',
    'goalkeeper_type': 'VARCHAR',
    'id': 'NUMBER',
    'index': 'NUMBER',
    'interception_outcome': 'VARCHAR',
    'location': 'VARIANT',
    'match_id': 'NUMBER',
    'minute': 'NUMBER',
    'miscontrol_aerial_won': 'BOOLEAN',
    'off_camera': 'BOOLEAN',
    'out': 'BOOLEAN',
    'pass_aerial_won': 'BOOLEAN',
    'pass_angle': 'FLOAT',
    'pass_assisted_shot_id': 'NUMBER',
    'pass_body_part': 'VARCHAR',
    'pass_cross': 'BOOLEAN',
    'pass_deflected': 'BOOLEAN',
    'pass_end_location': 'VARIANT',
    'pass_goal_assist': 'BOOLEAN',
    'pass_height': 'VARCHAR',
    'pass_inswinging': 'BOOLEAN',
    'pass_length': 'FLOAT',
    'pass_no_touch': 'BOOLEAN',
    'pass_outcome': 'VARCHAR',
    'pass_outswinging': 'BOOLEAN',
    'pass_recipient': 'VARCHAR',
    'pass_recipient_id': 'NUMBER',
    'pass_shot_assist': 'BOOLEAN',
    'pass_switch': 'BOOLEAN',
    'pass_technique': 'VARCHAR',
    'pass_through_ball': 'BOOLEAN',
    'pass_type': 'VARCHAR',
    'period': 'NUMBER',
    'play_pattern': 'VARCHAR',
    'player': 'VARCHAR',
    'player_id': 'NUMBER',
    'position': 'VARCHAR',
    'possession': 'NUMBER',
    'possession_team': 'VARCHAR',
    'possession_team_id': 'NUMBER',
    'related_events': 'VARIANT',
    'second': 'NUMBER',
    'shot_body_part': 'VARCHAR',
    'shot_deflected': 'BOOLEAN',
    'shot_end_location': 'VARIANT',
    'shot_first_time': 'BOOLEAN',
    'shot_freeze_frame': 'VARIANT',
    'shot_key_pass_id': 'NUMBER',
    'shot_outcome': 'VARCHAR',
    'shot_statsbomb_xg': 'FLOAT',
    'shot_technique': 'VARCHAR',
    'shot_type': 'VARCHAR',
    'substitution_outcome': 'VARCHAR',
    'substitution_outcome_id': 'NUMBER',
    'substitution_replacement': 'VARCHAR',
    'substitution_replacement_id': 'NUMBER',
    'tactics': 'VARIANT',
    'team': 'VARCHAR',
    'team_id': 'NUMBER',
    'timestamp': 'TIMESTAMP',
    'type': 'VARCHAR',
    'under_pressure': 'BOOLEAN'
}

# Generate DDL statement for creating the table
table_name = 'statsbomb_schema.events'
ddl_statement = f"CREATE OR REPLACE TABLE {table_name} ("

for column in columns:
    ddl_statement += f"\n    {column} {column_types.get(column, 'VARCHAR')},"

ddl_statement = ddl_statement.rstrip(',')  # Remove the trailing comma
ddl_statement += "\n);"

# Print the DDL statement
print(ddl_statement)

# Optionally execute the DDL statement in Snowflake
cur.execute(ddl_statement)

# Close the connection
cur.close()
conn.close()
