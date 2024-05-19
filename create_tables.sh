#!/bin/bash

# Function to execute a SQL file using the named connection
execute_sql() {
    local sql_file=$1
    snowsql -c alv -f $sql_file -o exit_on_error=true -o friendly=false
}

# Execute SQL files in order
execute_sql "schema/competitions.sql"
execute_sql "schema/seasons.sql"
execute_sql "schema/teams.sql"
execute_sql "schema/players.sql"
execute_sql "schema/matches.sql"
execute_sql "schema/lineups.sql"
execute_sql "schema/events.sql"

echo "All tables created successfully."