# json2sqlite 🚀

## Description 📄
`json2sqlite` is a tool that allows importing data from a JSON file into an SQLite database. This project is useful for anyone who wants to transfer structured data from a JSON format to a relational database quickly and easily.

## Project Structure 📁
The project structure is as follows:
```
json2sqlite/
│-- data/
│   ├── data.json  # JSON file to be imported (to be placed manually in this directory)
│-- src/
│   ├── __init__.py         # Module initialization file
│   ├── config.py           # Database and JSON file configuration
│   ├── json_reader.py      # Module for reading the JSON file
│   ├── logger.py           # Module for log management
│   ├── main.py             # Main script for data import
│   ├── sqlite_handler.py   # Module for SQLite database management
│-- README.md               # Project documentation
```

## Requirements 📋
- Python 3.x
- Python modules: `sqlite3`, `json`, `logging`

## Installation 💻
1. Clone the repository:
    ```sh
    git clone https://github.com/stefanopaolonii/json2sqlite.git
    cd json2sqlite
    ```

## Configuration ⚙️
Edit the `config.py` file to specify:
- The path to the JSON file (which must be placed in the `data/` directory)
- The name of the SQLite database
- The name of the table

Example configuration:
```python
DB_FILE = 'database.sqlite'
TABLE_NAME = 'my_table'
JSON_FILE = 'data/data.json'
```

## Usage ▶️
To run the script and import the JSON data into the SQLite database, execute the following command:
```sh
python -m src.main
```

## License 📜
This project is distributed under the MIT license. See the `LICENSE` file for more details.
