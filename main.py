import tkinter as tk
from tkinter import messagebox
import sqlite3
#Database setup
conn = sqlite3.connect('todo.db')
cursor = conn.cursor()
cursor.execute('''
               CREATE TABLE IF NOT EXISTS tasks(id INTEGER PRIMARY KEY AUTOINCREMENT,
               task TEXT NOT NULL)''')
conn.commit()
#Function to add a task
def  add_task():
    task = entry.get()
    if task:
        cursor.execute('INSERT INTO tasks (task) VALUES (?)', (task,))
        conn.commit()
        entry.delete(0,tk.END)
        load_tasks()
    else:
        messagebox.showwarning("warning","Please enter a task.")
def delete_task():
    selected = listbox.curselection()
    if selected:
        task_text = listbox.get(selected[0])
        cursor.execute("DELETE FROM tasks WHERE task = ?", (task_text,))
        conn.commit()
        load_tasks()
    else:
        messagebox.showwarning("Warning","Please select a task to delete.")
def load_tasks():
    listbox.delete(0,tk.END)
    cursor.execute("SELECT task FROM tasks")
    for row in cursor.fetchall():
        listbox.insert(tk.END, row[0])
#GUI setup
root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x400")
root.config(bg="white")

entry = tk.Entry(root,width=40,font=("Arial", 14))
entry.pack(pady=10)

add_btn = tk.Button(root,text="ADD TASK", command = add_task, bg = "green",fg = "white")
add_btn.pack(pady=5)

delete_btn = tk.Button(root,text="DELETE TASK",command = delete_task)
delete_btn.pack(pady=5)

listbox = tk.Listbox(root,width = 50,height=15,font=("Arial",14))
listbox.pack(pady=10)
load_tasks()
root.mainloop()
