
import sqlite3

conn = sqlite3.connect('my_doller.db')  # file-based DB
cursor = conn.cursor()

cursor.execute('''

   CREATE TABLE IF NOT EXISTS amit(
               
        id INTIGER PRAMARY KEY,
        name TEXT,
        fathername TEXT,
        mothername TEXT,
        phonenumber INTIGER,
        age INTIGER
               
    
    )

''')
conn.commit()

cursor.execute("INSERT INTO amit (name, fathername, mothername, phonenumber, age) VALUES (?, ?, ?, ?, ?)", ('ali', 'arun', 'suverne', 7219463969, 25))
conn.commit()

cursor.execute("SELECT * FROM amit")
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()