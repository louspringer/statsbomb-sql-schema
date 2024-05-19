CREATE SCHEMA IF NOT EXISTS statsbomb_schema;
USE SCHEMA statsbomb_schema;

CREATE TABLE IF NOT EXISTS matches (
    match_id INTEGER PRIMARY KEY,
    competition_id INTEGER,
    season_id INTEGER,
    match_date DATE,
    home_team_id INTEGER,
    away_team_id INTEGER,
    home_score INTEGER,
    away_score INTEGER,
    venue_name STRING,
    referee_name STRING,
    FOREIGN KEY (competition_id) REFERENCES competitions(competition_id),
    FOREIGN KEY (season_id) REFERENCES seasons(season_id)
);