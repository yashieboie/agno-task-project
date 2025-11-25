import sqlite3

# 1) Connect to database file (it will create it if it doesn't exist)
conn = sqlite3.connect("school.db")
cursor = conn.cursor()

# 2) Create a table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    grade INTEGER,
    city TEXT
);
""")

# 3) Insert sample data (10 rows)
students_data = [
    ("Rahul", 8, "Hyderabad"),
    ("Priya", 9, "Chennai"),
    ("Amit", 10, "Mumbai"),
    ("Sneha", 8, "Hyderabad"),
    ("Arjun", 7, "Delhi"),
    ("Kavya", 9, "Bengaluru"),
    ("Rohit", 10, "Pune"),
    ("Meera", 8, "Hyderabad"),
    ("Vikram", 7, "Mumbai"),
    ("Anjali", 9, "Chennai"),
]

cursor.executemany(
    "INSERT INTO students (name, grade, city) VALUES (?, ?, ?);",
    students_data
)

# 4) Save (commit) and close
conn.commit()
conn.close()

print("Database created and sample data inserted!")
