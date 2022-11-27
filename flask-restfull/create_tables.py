import sqlite3

connection = sqlite3.connect('test.db')
print("Opened database successfully")

cursor = connection.cursor()

# Create table
create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table)
print("Table created successfully")

# create items table
create_table = "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name text, price real)"
cursor.execute(create_table)
print("Table created successfully")

#insert dummy values for testing 
# insert_query = "INSERT INTO items VALUES ('test', 10.21)"
# cursor.execute(insert_query)




connection.commit()

connection.close()