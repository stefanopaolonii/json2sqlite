import json
from src.logger import logger

def load_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        logger.info(f'Loaded JSON file from {file_path}')
        return data
    except FileNotFoundError:
        logger.error(f'File not found: {file_path}')
    except json.JSONDecodeError:
        logger.error(f'Invalid JSON file: {file_path}')
    except Exception as e:
        logger.error(f'Error loading JSON file: {file_path}')
        raise
