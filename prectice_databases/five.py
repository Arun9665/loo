
import sqlite3

conn = sqlite3.connect('more.db')  # file-based DB
cursor = conn.cursor()

cursor.execute('''

   CREATE TABLE IF NOT EXISTS money(
               
        id INTIGER PRAMARY KEY,
        name TEXT,
        age INTIGER
               
    
    )

''')
conn.commit()

cursor.execute("INSERT INTO money (name, age) VALUES (?, ?) ", ('amit', 22))
conn.commit()

cursor.execute("SELECT * FROM money ")
rows = cursor.fetchall()
for i in rows:
    print(i)

conn.close()


