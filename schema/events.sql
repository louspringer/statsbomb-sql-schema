CREATE TABLE events (
    event_id INT PRIMARY KEY AUTO_INCREMENT,
    match_id INT,
    team_id INT,
    player_id INT,
    type VARCHAR(255),
    timestamp TIMESTAMP,
    minute INT,
    second INT,
    possession INT,
    location POINT,
    related_events JSON,
    event_data JSON,
    FOREIGN KEY (match_id) REFERENCES matches(match_id),
    FOREIGN KEY (team_id) REFERENCES teams(team_id),
    FOREIGN KEY (player_id) REFERENCES players(player_id)
);