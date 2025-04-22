
import sqlite3

# Step 1: Connect to a database (ya naya banega agar nahi hai)
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Step 2: Table banana
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER
    )
''')

# Step 3: Thoda sample data insert karna
cursor.execute("INSERT INTO students (name, age) VALUES ('Ali', 20)")
cursor.execute("INSERT INTO students (name, age) VALUES ('Sara', 22)")
cursor.execute("INSERT INTO students (name, age) VALUES ('Ahmed', 21)")
conn.commit()

# Step 4: DELETE query — let's delete student jiska naam 'Sara' hai
cursor.execute("DELETE FROM students WHERE name = 'Sara'")
conn.commit()

# Step 5: Check remaining data
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Step 6: Close the connection
conn.close()
