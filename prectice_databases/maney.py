
import sqlite3

# Database connection create karein
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

# Books Table banayein
cursor.execute('''
CREATE TABLE IF NOT EXISTS Books (
    BookID INTEGER PRIMARY KEY,
    Title TEXT NOT NULL,
    Author TEXT NOT NULL,
    Publisher TEXT,
    Genre TEXT,
    Availability BOOLEAN
)
''')
print("Books Table successfully created!")

# Data insert karna
books = [
    (1, "The Catcher in the Rye", "J.D. Salinger", "Little, Brown and Company", "Fiction", True),
    (2, "To Kill a Mockingbird", "Harper Lee", "J.B. Lippincott & Co.", "Fiction", True),
    (3, "1984", "George Orwell", "Secker & Warburg", "Dystopian", False)
]

cursor.executemany("INSERT INTO Books VALUES (?, ?, ?, ?, ?, ?)", books)
print("Data successfully inserted!")

# Database changes save aur close karein
conn.commit()
conn.close()
