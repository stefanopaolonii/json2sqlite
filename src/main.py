from src.config import DB_FILE, JSON_FILE, TABLE_NAME
from src.json_reader import load_json
from src.sqlite_handler import create_table, insert_data, connect_db
from src.logger import logger

def json_to_sqlite():
    try:
        data = load_json(JSON_FILE)
        
        if not data:
            logger.warning("The JSON file is empty!")
            return
        
        with connect_db(DB_FILE) as conn:
            columns = data[0].keys()  
            create_table(conn, TABLE_NAME, columns)
            
            insert_data(conn, TABLE_NAME, data)
        
        logger.info(f"Data from the JSON file has been inserted into the database {DB_FILE}")
    
    except Exception as e:
        logger.error(f"An error occurred: {e}")

if __name__ == "__main__":
    json_to_sqlite()
