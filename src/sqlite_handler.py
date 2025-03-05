import sqlite3
import json
from typing import Any, Dict, List, Optional
from src.logger import logger

def infer_column_type(value: Any) -> str:
    type_mapping = {
        type(None): "NULL",
        int: "INTEGER",
        float: "REAL",
        bool: "INTEGER",
        str: "TEXT",
        list: "TEXT",
        dict: "TEXT"
    }
    return type_mapping.get(type(value), "TEXT")

def create_table(conn: sqlite3.Connection, table_name: str, columns: List[str]) -> None:
    column_definitions = [
        f"{col} {infer_column_type(None)}" for col in columns
    ]
    columns_str = ', '.join(column_definitions)
    create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_str});"

    try:
        with conn:
            conn.execute(create_table_query)
        logger.info(f"Table '{table_name}' created successfully with correct data types.")
    except sqlite3.DatabaseError as e:
        logger.error(f"Error creating table '{table_name}': {e}")

def insert_data(conn: sqlite3.Connection, table_name: str, data: List[Dict[str, Any]]) -> None:
    if not data:
        logger.warning("No data provided for insertion.")
        return

    columns = data[0].keys()
    columns_str = ', '.join(columns)
    placeholders = ', '.join(['?'] * len(columns))
    insert_query = f"INSERT INTO {table_name} ({columns_str}) VALUES ({placeholders})"

    try:
        with conn:
            for row in data:
                row_values = [
                    json.dumps(value) if isinstance(value, (dict, list)) else value
                    for value in row.values()
                ]
                conn.execute(insert_query, tuple(row_values))
        logger.info(f"{len(data)} records successfully inserted into table '{table_name}'.")
    except sqlite3.IntegrityError as e:
        logger.error(f"Integrity error inserting into table '{table_name}': {e}")
    except sqlite3.DatabaseError as e:
        logger.error(f"Database error inserting data into table '{table_name}': {e}")

def connect_db(db_file: str) -> Optional[sqlite3.Connection]:
    try:
        conn = sqlite3.connect(db_file)
        logger.info(f"Connected to database '{db_file}' successfully.")
        return conn
    except sqlite3.Error as e:
        logger.error(f"Error connecting to database '{db_file}': {e}")
        return None