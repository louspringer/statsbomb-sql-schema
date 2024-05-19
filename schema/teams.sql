CREATE SCHEMA IF NOT EXISTS statsbomb_schema;
USE SCHEMA statsbomb_schema;

CREATE TABLE IF NOT EXISTS teams (
    team_id INTEGER PRIMARY KEY,
    team_name STRING
);