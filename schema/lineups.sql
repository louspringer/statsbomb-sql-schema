CREATE TABLE lineups (
    lineup_id INT PRIMARY KEY AUTO_INCREMENT,
    match_id INT,
    team_id INT,
    player_id INT,
    starting_position VARCHAR(255),
    jersey_number INT,
    FOREIGN KEY (match_id) REFERENCES matches(match_id),
    FOREIGN KEY (team_id) REFERENCES teams(team_id),
    FOREIGN KEY (player_id) REFERENCES players(player_id)
);