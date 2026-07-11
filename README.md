# Data Engineering Project

This project starts a local PostgreSQL database with Docker and provides a Python-based data generator that creates sample event data and inserts it into the database.

## Project Structure

- [docker-compose.yml](docker-compose.yml) – defines the PostgreSQL container
- [main.py](main.py) – entry point for running the data generation flow
- [produce/produce.py](produce/produce.py) – generates sample events and inserts them into PostgreSQL
- [produce/db_connect.py](produce/db_connect.py) – manages database connections and insert operations

## Prerequisites

- Docker Desktop running
- Python 3.13+
- [uv](https://docs.astral.sh/uv/) installed

## Environment Variables

Create a `.env` file in the project root with the following values:

```env
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_USER=myuser
POSTGRES_PASSWORD=mypassword
POSTGRES_DB=mydatabase
```

## Start the Database

From the project root, start PostgreSQL with:

```bash
docker-compose up -d
```

To stop the container later:

```bash
docker-compose down
```

## Install Dependencies

```bash
uv sync
```

## Run the Application

```bash
uv run main.py
```

When you run the script, it will prompt you for the number of users to generate and then insert sample event records into the database.

## Troubleshooting

- If the database connection fails, make sure Docker is running and the PostgreSQL container is up.
- If you change credentials, update both the Compose file and the `.env` file.
- If the script hangs, confirm that PostgreSQL is reachable on `localhost:5432`.
