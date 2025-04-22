import sqlite3

conn=sqlite3.connect("ajinkya.db")
conn.execute('''
    create table amit(
        st_id INT AUTO_INCREMENT PRIMARY KEY,
        st_name VARCHAR(50),
        st_class VARCHAR(10),
        st_emil VARCHAR(30)
             
                  
             
             
    )


''')

conn.close()