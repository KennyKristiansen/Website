#! python3
# database_creator.py - Extract and fill cookbook

import sqlite3

# Connect to database
database_name = 'cookbook.sqlite'
try:
    connection = sqlite3.connect(database=database_name, isolation_level=None)
    print(f'connected to {database_name}')
except sqlite3.Error as e:
    print(f'Could not connect to database. Error: {e}')
try:
    connection.execute('''DROP TABLE ingredient''')
    connection.execute('''DROP TABLE recipe''')
    connection.execute('''DROP TABLE steps''')
except:
    pass

# Create tables
try:
    # noinspection PyUnboundLocalVariable
    connection.execute('CREATE TABLE IF NOT EXISTS recipe('
                       'id INT PRIMARY KEY, '
                       'name TEXT, '
                       'link TEXT, '
                       'description TEXT, '
                       'calories TEXT, '
                       'protein TEXT, '
                       'carbs TEXT, '
                       'fat TEXT)')

    connection.execute('CREATE TABLE IF NOT EXISTS ingredient('
                       'recipe_id INT NOT NULL, '
                       'ingredient TEXT, '
                       'amount INT, '
                       'unit TEXT, '
                       'FOREIGN KEY (recipe_id) REFERENCES recipe(id))')

    connection.execute('CREATE TABLE IF NOT EXISTS steps('
                       'recipe_id INT, '
                       'recipe_step INT, '
                       'description TEXT, '
                       'FOREIGN KEY (recipe_id) REFERENCES recipe(id))')

    table_names = connection.cursor()
    where = ['table']
    table_names.execute('SELECT name '
                        'FROM sqlite_master '
                        'WHERE type=(?)', where)
    table_names = table_names.fetchall()

    print(f'Tables successfully executed: {table_names}')
except sqlite3.OperationalError as e:
    print(f'Tables failed to execute: {e}')

# Commit and close connection
connection.commit()
connection.close()
