import sqlite3

connection = sqlite3.connect('test.db')
print("Opened database successfully")

cursor = connection.cursor()

# Create table
create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table)
print("Table created successfully")


connection.commit()

connection.close()