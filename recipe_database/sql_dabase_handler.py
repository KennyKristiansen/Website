import sqlite3
import os

os.chdir('''C:\\Users\\kenny\\PycharmProjects\\Python training\\Exercises\\recipe\\''')
database_name = 'cookbook.sqlite'
try:
    connection = sqlite3.connect(database=database_name, isolation_level=None)
    print(f'connected to {database_name}')
except sqlite3.Error as e:
    print(f'Could not connect to database. Error: {e}')
    quit()

results = connection.execute('SELECT id, protein FROM recipe WHERE CAST(protein AS INTEGER) >= 40 AND CAST(fat AS INTEGER) <= 25')
for result in results:
    print(result)
