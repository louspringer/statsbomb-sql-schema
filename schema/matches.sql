CREATE TABLE matches (
    match_id INT PRIMARY KEY,
    competition_id INT,
    season_id INT,
    match_date DATE,
    home_team_id INT,
    away_team_id INT,
    home_score INT,
    away_score INT,
    venue_name VARCHAR(255),
    referee_name VARCHAR(255),
    FOREIGN KEY (competition_id) REFERENCES competitions(competition_id),
    FOREIGN KEY (season_id) REFERENCES seasons(season_id)
);