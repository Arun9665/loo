
import sqlite3

conn = sqlite3.connect("spoon.db")
culsor = conn.cursor()

culsor.execute('''
     CREATE TABLE IF NOT EXISTS momebi(
               
        id INTIGER PRAMARY KEY,
        name TEXT,
        age INTIGER,
        number INTIGER
        
    )


''')
conn.commit()

culsor.execute("INSERT INTO momebi (name, age, number) VALUES (?, ?, ?)", ('ali', 25, 7219463969))
conn.commit()

culsor.execute("SELECT * FROM momebi")
rows = culsor.fetchall()
for row in rows:
    print(row)

conn.close()