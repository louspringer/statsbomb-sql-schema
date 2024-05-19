CREATE SCHEMA IF NOT EXISTS statsbomb_schema;
USE SCHEMA statsbomb_schema;

CREATE TABLE IF NOT EXISTS competitions (
    competition_id INTEGER PRIMARY KEY,
    competition_name STRING,
    country_name STRING,
    competition_gender STRING
);