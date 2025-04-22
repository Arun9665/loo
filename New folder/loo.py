

import sqlite3

# Yeh command "example.db" file create karegi, jahan database ka data store hoga
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Ab aap isme tables create kar sakte hain
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    phone NUMBER NOT NULL,          
    email TEXT UNIQUE NOT NULL
            
)
''')

conn.commit()
conn.close()
