"""
This GUI-based To-Do List application provides a user-friendly way to manage tasks with basic functionalities like adding, removing, and completing tasks. 
The use of tkinter makes it easy to create and manage the graphical interface, allowing users to interact with their to-do list more intuitively.
"""

import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        
        self.tasks = []

        # Frame for the listbox and scrollbar
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)

        # Listbox to display tasks
        self.listbox = tk.Listbox(self.frame, width=50, height=15, selectmode=tk.SINGLE)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        # Scrollbar for the listbox
        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)

        # Entry widget to enter a new task
        self.entry = tk.Entry(self.root, width=50)
        self.entry.pack(pady=5)

        # Buttons to add, remove, and complete tasks
        self.add_button = tk.Button(self.root, text="Add Task", width=15, command=self.add_task)
        self.add_button.pack(pady=5)

        self.remove_button = tk.Button(self.root, text="Remove Task", width=15, command=self.remove_task)
        self.remove_button.pack(pady=5)

        self.complete_button = tk.Button(self.root, text="Complete Task", width=15, command=self.complete_task)
        self.complete_button.pack(pady=5)

    def add_task(self):
        task = self.entry.get()
        if task:
            self.tasks.append({"task": task, "completed": False})
            self.update_listbox()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def remove_task(self):
        try:
            selected_task_index = self.listbox.curselection()[0]
            self.tasks.pop(selected_task_index)
            self.update_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task.")

    def complete_task(self):
        try:
            selected_task_index = self.listbox.curselection()[0]
            self.tasks[selected_task_index]["completed"] = True
            self.update_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task.")

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "Complete" if task["completed"] else "Incomplete"
            self.listbox.insert(tk.END, f'{task["task"]} - {status}')

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
