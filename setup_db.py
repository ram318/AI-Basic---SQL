import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        name TEXT,
        rollno INTEGER PRIMARY KEY,
        mathsmarks INTEGER,
        sciencemarks INTEGER,
        socialmarks INTEGER
    )
''')

students = [
    ("Alice", 101, 75, 80, 85),
    ("Bob", 102, 55, 60, 70),
    ("Charlie", 103, 90, 85, 88),
    ("David", 104, 40, 30, 50)
]

cursor.executemany("INSERT OR IGNORE INTO students VALUES (?, ?, ?, ?, ?)", students)
conn.commit()
conn.close()