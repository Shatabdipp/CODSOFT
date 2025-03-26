import tkinter as tk
from tkinter import messagebox, ttk
import json
from datetime import datetime

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced To-Do List")
        self.root.geometry("600x700")
        self.root.configure(bg="#f4f4f4")
        
        self.tasks = []
        self.load_tasks()
        
        self.header_label = tk.Label(root, text="To-Do List", font=("Arial", 16, "bold"), bg="#f4f4f4")
        self.header_label.pack(pady=10)
        
        self.task_entry = tk.Entry(root, width=40, font=("Arial", 12))
        self.task_entry.pack(pady=10)
        
        self.priority_var = tk.StringVar()
        self.priority_dropdown = ttk.Combobox(root, textvariable=self.priority_var, values=["High", "Medium", "Low"], state="readonly")
        self.priority_dropdown.set("Medium")
        self.priority_dropdown.pack(pady=5)
        
        self.due_date_entry = tk.Entry(root, width=40, font=("Arial", 12))
        self.due_date_entry.insert(0, "YYYY-MM-DD")
        self.due_date_entry.pack(pady=5)
        
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"))
        self.add_button.pack(pady=5)
        
        self.task_listbox = tk.Listbox(root, width=60, height=15, font=("Arial", 12))
        self.task_listbox.pack(pady=10)
        
        self.update_button = tk.Button(root, text="Update Task", command=self.update_task, bg="#FFA500", fg="white", font=("Arial", 12, "bold"))
        self.update_button.pack(pady=5)
        
        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task, bg="#f44336", fg="white", font=("Arial", 12, "bold"))
        self.delete_button.pack(pady=5)
        
        self.clear_button = tk.Button(root, text="Clear All", command=self.clear_all_tasks, bg="#FF5733", fg="white", font=("Arial", 12, "bold"))
        self.clear_button.pack(pady=5)
        
        self.save_button = tk.Button(root, text="Save Tasks", command=self.save_tasks, bg="#2196F3", fg="white", font=("Arial", 12, "bold"))
        self.save_button.pack(pady=5)
        
        self.exit_button = tk.Button(root, text="Exit", command=root.quit, bg="#555", fg="white", font=("Arial", 12, "bold"))
        self.exit_button.pack(pady=5)
        
        self.display_tasks()
        
    def add_task(self):
        task = self.task_entry.get()
        priority = self.priority_var.get()
        due_date = self.due_date_entry.get()
        
        try:
            datetime.strptime(due_date, "%Y-%m-%d")
        except ValueError:
            messagebox.showwarning("Warning", "Enter a valid date in YYYY-MM-DD format")
            return
        
        if task:
            self.tasks.append({"task": task, "priority": priority, "due_date": due_date})
            self.display_tasks()
            self.task_entry.delete(0, tk.END)
            self.due_date_entry.delete(0, tk.END)
            self.due_date_entry.insert(0, "YYYY-MM-DD")
        else:
            messagebox.showwarning("Warning", "Task cannot be empty")
    
    def update_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            new_task = self.task_entry.get()
            new_priority = self.priority_var.get()
            new_due_date = self.due_date_entry.get()
            
            try:
                datetime.strptime(new_due_date, "%Y-%m-%d")
            except ValueError:
                messagebox.showwarning("Warning", "Enter a valid date in YYYY-MM-DD format")
                return
            
            if new_task:
                self.tasks[selected_index] = {"task": new_task, "priority": new_priority, "due_date": new_due_date}
                self.display_tasks()
                self.task_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "Updated task cannot be empty")
        except IndexError:
            messagebox.showwarning("Warning", "Select a task to update")
    
    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_index]
            self.display_tasks()
        except IndexError:
            messagebox.showwarning("Warning", "Select a task to delete")
    
    def clear_all_tasks(self):
        confirm = messagebox.askyesno("Confirm", "Are you sure you want to delete all tasks?")
        if confirm:
            self.tasks = []
            self.display_tasks()
    
    def display_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            task_display = f"{task['task']} - {task['priority']} - Due: {task['due_date']}"
            self.task_listbox.insert(tk.END, task_display)
    
    def save_tasks(self):
        with open("tasks.json", "w") as file:
            json.dump(self.tasks, file)
        messagebox.showinfo("Success", "Tasks saved successfully")
    
    def load_tasks(self):
        try:
            with open("tasks.json", "r") as file:
                self.tasks = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.tasks = []

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
