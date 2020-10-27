#! python3
# database_api.py - Ease the connection between data and database

import sqlite3

# Connect to database
database_name = 'cookbook.sqlite'
try:
    connection = sqlite3.connect(database=database_name, isolation_level=None)
    print(f'connected to {database_name}')
except sqlite3.Error as e:
    print(f'Could not connect to database. Error: {e}')


# Define classes for table input
class Recipe:
    def __init__(self):
        """

        :rtype: object
        """
        self.id = None
        self.name = None
        self.link = None
        self.description = None
        self.calories = None
        self.protein = None
        self.carbs = None
        self.fat = None

    def export(self):
        try:
            table_data = [self.id, self.name, self.link, self.description, self.calories, self.protein, self.carbs, self.fat]
            connection.execute('INSERT INTO recipe VALUES (?,?,?,?,?,?,?,?)', table_data)
        except sqlite3.IntegrityError:
            pass

    def print(self):
        print(self.id)
        print(self.name)
        print(self.link)
        print(self.description)


class Ingredient:
    def __init__(self):
        self.id = None
        self.ingredient = None
        self.amount = None
        self.unit = None

    def export(self):
        try:
            table_data = [self.id, self.ingredient, self.amount, self.unit]
            connection.execute('INSERT INTO ingredient VALUES (?,?,?,?)', table_data)
        #except sqlite3.IntegrityError:
        except IndentationError:
            pass


class Steps:
    def __init__(self):
        self.id = None
        self.step = None
        self.description = None

    def export(self):
        try:
            table_data = [self.id, self.step, self.description]
            connection.execute('INSERT INTO steps VALUES (?,?,?)', table_data)
        except sqlite3.IntegrityError:
            pass
