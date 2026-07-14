import sqlite3

def get_connection():
    connection = sqlite3.connect("database/fincontrol.db")
    return connection

def initialize_database():
    connection = get_connection()
    cursor = connection.cursor()
    with open("database/schema.sql", "r") as file:
        schema = file.read()
    cursor.executescript(schema)
    connection.commit()
    connection.close()
