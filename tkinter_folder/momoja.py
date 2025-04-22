
import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox

# Database setup
conn = sqlite3.connect("students.db")
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        course TEXT NOT NULL
    )
""")
conn.commit()

# Insert function
def add_student():
    name = name_var.get()
    age = age_var.get()
    course = course_var.get()
    
    if name and age and course:
        cursor.execute("INSERT INTO students (name, age, course) VALUES (?, ?, ?)", (name, age, course))
        conn.commit()
        messagebox.showinfo("Success", "Student added successfully!")
        display_students()
    else:
        messagebox.showerror("Error", "All fields are required")

# Show all students
def display_students():
    cursor.execute("SELECT * FROM students")
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

name_var = tk.StringVar()
age_var = tk.StringVar()
course_var = tk.StringVar()

tk.Entry(root, textvariable=name_var).grid(row=0, column=1)
tk.Entry(root, textvariable=age_var).grid(row=1, column=1)
tk.Entry(root, textvariable=course_var).grid(row=2, column=1)

tk.Button(root, text="Add Student", command=add_student).grid(row=3, column=0, columnspan=2)

# Treeview (Table)
columns = ("ID", "Name", "Age", "Course")
tree = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
tree.grid(row=4, column=0, columnspan=2)

display_students()

root.mainloop()