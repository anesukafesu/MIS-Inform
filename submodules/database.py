import sqlite3

connection = sqlite3.connect('database.sqlite3')

def db(statement):
    cursor = connection.cursor()
    return cursor.execute(statement)
