
import sqlite3

# Database connect karein
conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()

# Table banayein
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
''')

# Data insert karein
cursor.execute('''
INSERT INTO users (name, age)
VALUES ('John', 25)
''')

# Data read karein
cursor.execute('SELECT * FROM users')
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.commit()
conn.close()
