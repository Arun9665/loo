
import sqlite3

conn = sqlite3.connect('my_ajinkya.db')  # file-based DB
cursor = conn.cursor()

cursor.execute('''

   CREATE TABLE IF NOT EXISTS mobile(
               
        id INTIGER PRAMARY KEY,
        name TEXT,
        age INTIGER
               
    
    )

''')
conn.commit()

cursor.execute("INSERT INTO mobile (name, age) VALUES (?, ?)", ('ali', 25))
conn.commit()

cursor.execute("SELECT * FROM mobile")
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()