CREATE SCHEMA IF NOT EXISTS statsbomb_schema;
USE SCHEMA statsbomb_schema;

CREATE TABLE IF NOT EXISTS lineups (
    lineup_id INTEGER PRIMARY KEY AUTOINCREMENT,
    match_id INTEGER,
    team_id INTEGER,
    player_id INTEGER,
    starting_position STRING,
    jersey_number INTEGER,
    FOREIGN KEY (match_id) REFERENCES matches(match_id),
    FOREIGN KEY (team_id) REFERENCES teams(team_id),
    FOREIGN KEY (player_id) REFERENCES players(player_id)
);