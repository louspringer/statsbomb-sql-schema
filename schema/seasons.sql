CREATE TABLE seasons (
    season_id INT PRIMARY KEY,
    season_name VARCHAR(255),
    competition_id INT,
    FOREIGN KEY (competition_id) REFERENCES competitions(competition_id)
);