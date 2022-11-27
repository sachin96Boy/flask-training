import sqlite3

conn = sqlite3.connect('test.db')
print("Opened database successfully")

cursor = conn.cursor()

# Create table
create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table)
print("Table created successfully")

# Insert a row of data
insert_query = "INSERT INTO users VALUES (NULL, ?, ?)"
cursor.execute(insert_query, ('bob', 'asdf'))
print("Record created successfully")

# Insert multiple rows of data
users = [
    ('jose', 'asdf'),
    ('rolf', 'asdf'),
]
cursor.executemany(insert_query, users)
print("Records created successfully for multiple users")

#select query
select_query = "SELECT * FROM users"
for row in cursor.execute(select_query):
    print(row)


conn.commit()

conn.close()

