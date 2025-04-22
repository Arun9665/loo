
import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox

# Database setup
conn = sqlite3.connect("studentso.db")
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS studentso (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        course TEXT NOT NULL,
        amount INTIGER NOT NULL
    )
""")
conn.commit()

# Insert function
def add_student():
    name = name_var.get()
    age = age_var.get()
    course = course_var.get()
    amount = amount_var.get()
    
    if name and age and course and amount:
        cursor.execute("INSERT INTO studentso (name, age, course, amount) VALUES (?, ?, ?, ?)", (name, age, course, amount))
        conn.commit()
        messagebox.showinfo("Success", "Student added successfully!")
        display_students()
    else:
        messagebox.showerror("Error", "All fields are required")

# Show all students
def display_students():
    cursor.execute("SELECT * FROM studentso")
    rows = cursor.fetchall()
    for row in tree.get_children():
        tree.delete(row)
    for row in rows:
        tree.insert("", "end", values=row)

# GUI setup
root = tk.Tk()
root.title("Student Management System")

# Input fields
tk.Label(root, text="Name").grid(row=0, column=0)
tk.Label(root, text="Age").grid(row=1, column=0)
tk.Label(root, text="Course").grid(row=2, column=0)
tk.Label(root, text="amount").grid(row=3, column=0)

name_var = tk.StringVar()
age_var = tk.StringVar()
course_var = tk.StringVar()
amount_var = tk.StringVar()

tk.Entry(root, textvariable=name_var).grid(row=0, column=1)
tk.Entry(root, textvariable=age_var).grid(row=1, column=1)
tk.Entry(root, textvariable=course_var).grid(row=2, column=1)
tk.Entry(root, textvariable=amount_var).grid(row=3, column=1)

tk.Button(root, text="Add Student", command=add_student).grid(row=4, column=0, columnspan=2)

# Treeview (Table)
columns = ("ID", "Name", "Age", "Course", "amount")
tree = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
tree.grid(row=5, column=0, columnspan=2)

display_students()

root.mainloop()