from dotenv import load_dotenv
import os
import psycopg


load_dotenv()

POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
POSTGRES_PORT = int(os.getenv("POSTGRES_PORT", "5432"))
POSTGRES_USER = os.getenv("POSTGRES_USER") or os.getenv("postgres_user") or "myuser"
POSTGRES_PASSWORD = (
    os.getenv("POSTGRES_PASSWORD") or os.getenv("postgres_password") or "mypassword"
)
POSTGRES_DB = os.getenv("POSTGRES_DB") or os.getenv("postgres_db") or "mydatabase"


def get_connection():
    return psycopg.connect(
        host=POSTGRES_HOST,
        port=POSTGRES_PORT,
        dbname=POSTGRES_DB,
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD,
        connect_timeout=5,
    )


def check_connection():
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT current_date;")
                print("Connection successful")
                print("Current date:", cur.fetchone()[0])
    except Exception as exc:
        print(f"Connection failed: {exc}")
        raise


def insert_record(table_name, columns, values):
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                placeholders = ", ".join(["%s"] * len(values))
                column_list = ", ".join(columns)
                query = (
                    f"INSERT INTO {table_name} ({column_list}) VALUES ({placeholders})"
                )
                cur.execute(query, values)
                conn.commit()
                print(f"Inserted into {table_name} successfully")
    except Exception as exc:
        print(f"Failed to insert record: {exc}")
        raise


def create_new_table(table_name, columns, types):
    with get_connection() as conn:
        with conn.cursor() as cur:
            columns_with_types = ", ".join(
                [f"{col} {typ}" for col, typ in zip(columns, types)]
            )
            query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_with_types})"
            cur.execute(query)
            print(f"Table {table_name} created successfully")


def read_records(table_name):
    with get_connection() as conn:
        with conn.cursor() as cur:
            query = f"SELECT * FROM {table_name}"
            cur.execute(query)
            records = cur.fetchall()
            for record in records:
                print(record)


if __name__ == "__main__":
    # create_new_table("events_hourly", ["id", "name", "email","address","event","timestamp"], ["VARCHAR(100)", "VARCHAR(100)", "VARCHAR(100)", "VARCHAR(200)", "VARCHAR(100)", "TIMESTAMP"])
    # read_records("events_hourly")
    check_connection()
    # Example usage:)
