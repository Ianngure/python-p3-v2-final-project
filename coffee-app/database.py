import sqlite3


CREATE_BEANS_TABLE = "CREATE TABLE beans (id INTEGER PRIMARY KEY, name TEXT, method TEXT ,rating INTEGER);"
INSERT_BEAN = "INSERT INTO beans ()"



def connect():
    return sqlite3.connect("data.db")


def create_tables(connection):
  with connection:
    connection.execute(CREATE_BEANS_TABLE
    )