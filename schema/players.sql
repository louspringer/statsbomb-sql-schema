CREATE SCHEMA IF NOT EXISTS statsbomb_schema;
USE SCHEMA statsbomb_schema;

CREATE TABLE IF NOT EXISTS players (
    player_id INTEGER PRIMARY KEY,
    player_name STRING,
    nickname STRING,
    birth_date DATE,
    country_of_birth STRING,
    nationality STRING
);