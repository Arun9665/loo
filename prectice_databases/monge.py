
import sqlite3

# Step 1: Database connection
conn = sqlite3.connect('com.db')
cursor = conn.cursor()

# Step 2: Create 'students' table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT
    )
''')

# Step 3: Create 'courses' table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS courses (
        id INTEGER PRIMARY KEY,
        student_id INTEGER,
        course_name TEXT,
        FOREIGN KEY (student_id) REFERENCES students (id)
    )
''')

# Step 4: Insert some sample data into 'students'
cursor.execute("INSERT INTO students (name) VALUES ('Ali')")
cursor.execute("INSERT INTO students (name) VALUES ('Sara')")
cursor.execute("INSERT INTO students (name) VALUES ('Ahmed')")
conn.commit()

# Step 5: Insert some sample data into 'courses'
cursor.execute("INSERT INTO courses (student_id, course_name) VALUES (1, 'Math')")
cursor.execute("INSERT INTO courses (student_id, course_name) VALUES (2, 'Physics')")
cursor.execute("INSERT INTO courses (student_id, course_name) VALUES (1, 'English')")
conn.commit()

# Step 6: JOIN query to combine data from both tables
cursor.execute('''
    SELECT students.name, courses.course_name
    FROM students
    INNER JOIN courses ON students.id = courses.student_id
''')

# Step 7: Fetch and print the results
rows = cursor.fetchall()
for row in rows:
    print(f"Student: {row[0]}, Course: {row[1]}")

# Step 8: Close the connection
conn.close()
