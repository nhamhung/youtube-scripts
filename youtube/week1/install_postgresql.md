# Installing PostgreSQL

Reference: https://wiki.postgresql.org/wiki/Homebrew

- `brew update; brew doctor`
- `brew install postgresql@14`
- `brew services start postgresql@14`
- `brew services list`

# Connect through `psql`

## Manual way

- `psql list` to list all databases
- `psql postgres` to connect to a database
- copy + paste content of `create_customers_table.sql` file into terminal
- `\l` to list databases
- `\c <db_name>` to choose database
- `-dt` to list tables

## Scripting way

- `psql -h localhost -d postgres -U nhamhhung -p 5432 -f /Users/nhamhhung/Teaching/week1/create_customers_table.sql`

Why port 5432?

- By default, psql runs on port 5432
- To double-confirm, run: `SELECT * FROM pg_settings WHERE name = 'port';`
