
import sqlite3
from prettytable import PrettyTable

# Database se connect karein (agar file exist nahi karti, to yeh nayi file banayega)
conn = sqlite3.connect('todo_list.db')
cursor = conn.cursor()

# Tasks ka table banayein
cursor.execute('''
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT NOT NULL,
    status TEXT NOT NULL
)
''')

# Task add karne ka function
def add_task(task):
    cursor.execute('INSERT INTO tasks (task, status) VALUES (?, ?)', (task, 'Pending'))
    conn.commit()
    print(f"Task '{task}' added successfully!")

# Task status update karne ka function
def mark_task_complete(task_id):
    cursor.execute('UPDATE tasks SET status = ? WHERE id = ?', ('Completed', task_id))
    conn.commit()
    print(f"Task ID {task_id} marked as Completed.")

# Saare tasks dekhne ka function
def view_tasks():
    cursor.execute('SELECT * FROM tasks')
    rows = cursor.fetchall()
    if rows:
        table = PrettyTable(['ID', 'Task', 'Status'])
        for row in rows:
            table.add_row(row)
        print(table)
    else:
        print("No tasks available.")

# Main menu
while True:
    print("\nTo-Do List Menu")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Complete")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        task_name = input("Enter the task: ")
        add_task(task_name)
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        task_id = int(input("Enter Task ID to mark as complete: "))
        mark_task_complete(task_id)
    elif choice == '4':
        print("Exiting To-Do List App. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")

conn.close()
