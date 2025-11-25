import sqlite3

# Connect to the database
conn = sqlite3.connect("school.db")
cursor = conn.cursor()

# Run SQL query using Python
cursor.execute("SELECT id, name, grade, city FROM students;")
rows = cursor.fetchall()

print("All students:")
print("--------------------------------")

for row in rows:
    student_id, name, grade, city = row
    print(f"ID: {student_id}, Name: {name}, Grade: {grade}, City: {city}")

conn.close()




