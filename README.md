# StatsBomb SQL Schema

This repository contains a SQL schema for StatsBomb Open Data, designed to facilitate easier integration and analysis of football (soccer) data.

## Getting Started

### Prerequisites

- MySQL or PostgreSQL database
- Python 3.x
- `statsbombpy` library
- `mysql-connector-python` or `psycopg2` library

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/statsbomb-sql-schema.git
   cd statsbomb-sql-schema
   ```

2. Set up the database:
   ```bash
   mysql -u yourusername -p < schema/competitions.sql
   mysql -u yourusername -p < schema/seasons.sql
   mysql -u yourusername -p < schema/matches.sql
   mysql -u yourusername -p < schema/teams.sql
   mysql -u yourusername -p < schema/players.sql
   mysql -u yourusername -p < schema/lineups.sql
   mysql -u yourusername -p < schema/events.sql
   ```

3. Load the data:
   ```bash
   python scripts/load_competitions.py
   python scripts/load_matches.py
   python scripts/load_teams.py
   python scripts/load_players.py
   python scripts/load_lineups.py
   python scripts/load_events.py
   ```

### Usage

See the `examples` directory for example queries to get started with your analysis.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.