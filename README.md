# SQLite

This module provides a simple interface to interact with SQLite databases. It allows you to perform common database operations such as creating tables, inserting data, querying data, and more.

## Features

- **Create Tables**: Easily create tables with specified schemas.
- **Insert Data**: Insert single or multiple rows of data.
- **Query Data**: Execute SQL queries to retrieve data.
- **Update Data**: Update existing records in the database.
- **Delete Data**: Remove records from the database.
- **Transaction Management**: Support for transactions to ensure data integrity.

## Installation

To install the SQLite module, you can use pip:

```sh
pip install sqlite-module
```

## Usage

Here are some examples of how to use the SQLite module:

### Importing the Module

```python
import sqlite_module
```

### Creating a Database Connection

```python
conn = sqlite_module.connect('example.db')
```

### Creating a Table

```python
create_table_sql = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER
);
"""
sqlite_module.execute_query(conn, create_table_sql)
```

### Inserting Data

```python
insert_sql = "INSERT INTO users (name, age) VALUES (?, ?)"
data = ('John Doe', 30)
sqlite_module.execute_query(conn, insert_sql, data)
```

### Querying Data

```python
select_sql = "SELECT * FROM users"
rows = sqlite_module.execute_query(conn, select_sql)
for row in rows:
    print(row)
```

### Updating Data

```python
update_sql = "UPDATE users SET age = ? WHERE name = ?"
data = (31, 'John Doe')
sqlite_module.execute_query(conn, update_sql, data)
```

### Deleting Data

```python
delete_sql = "DELETE FROM users WHERE name = ?"
data = ('John Doe',)
sqlite_module.execute_query(conn, delete_sql, data)
```

### Closing the Connection

```python
conn.close()
```

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss your ideas.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [SQLite](https://www.sqlite.org/) - The database engine used by this module.
- [Python](https://www.python.org/) - The programming language used to develop this module.
