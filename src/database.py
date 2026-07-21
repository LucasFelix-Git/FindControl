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

def initialize_categories():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
        INSERT OR IGNORE INTO categoria (nome_categoria)
        VALUES
        ("Alimentação"),
        ("Transporte"),
        ("Moradia"),
        ("Saúde"),
        ("Educação"),
        ("Lazer"),
        ("Salário"),
        ("Investimentos")
""")
    connection.commit()
    connection.close()