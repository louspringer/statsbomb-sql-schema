CREATE SCHEMA IF NOT EXISTS statsbomb_schema;
USE SCHEMA statsbomb_schema;

CREATE TABLE IF NOT EXISTS seasons (
    season_id INTEGER PRIMARY KEY,
    season_name STRING,
    competition_id INTEGER,
    FOREIGN KEY (competition_id) REFERENCES competitions(competition_id)
);