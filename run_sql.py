import sqlite3

# Connect to the database
conn = sqlite3.connect("school.db")
cursor = conn.cursor()

print("Type an SQL query, e.g., SELECT * FROM students;")
query = input("SQL> ")

cursor.execute(query)
rows = cursor.fetchall()

# Print each row
for row in rows:
    print(row)

conn.close()
