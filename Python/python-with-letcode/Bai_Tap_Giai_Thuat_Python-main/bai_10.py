import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        listbox.delete(selected_task_index)
    else:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def edit_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        edited_task = entry.get()
        if edited_task:
            listbox.delete(selected_task_index)
            listbox.insert(selected_task_index, edited_task)
            entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")
    else:
        messagebox.showwarning("Warning", "Please select a task to edit.")

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Create and pack widgets
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

add_button = tk.Button(button_frame, text="Add Task", command=add_task)
add_button.pack(side=tk.LEFT, padx=5)

delete_button = tk.Button(button_frame, text="Delete Task", command=delete_task)
delete_button.pack(side=tk.LEFT, padx=5)

edit_button = tk.Button(button_frame, text="Edit Task", command=edit_task)
edit_button.pack(side=tk.LEFT, padx=5)

listbox = tk.Listbox(root, selectmode=tk.SINGLE, height=10, width=40)
listbox.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
