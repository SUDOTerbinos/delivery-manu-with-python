import tkinter as tk
from tkinter import messagebox

def submit():
    project_name = project_entry.get()
    category = category_var.get()
    deadline = deadline_entry.get()
    
    if not project_name or not category or not deadline:
        messagebox.showerror("Error", "All fields are required!")
        return
    
    messagebox.showinfo("Success", f"Project '{project_name}' in '{category}' category is set to be delivered by {deadline}.")

def clear_fields():
    project_entry.delete(0, tk.END)
    deadline_entry.delete(0, tk.END)
    category_var.set(categories[0])

root = tk.Tk()
root.title("Project Delivery Menu")
root.geometry("400x300")

tk.Label(root, text="Project Name:").pack(pady=5)
project_entry = tk.Entry(root, width=40)
project_entry.pack(pady=5)

categories = ["Web Development", "Cybersecurity", "Machine Learning", "Data Science"]
category_var = tk.StringVar(value=categories[0])
tk.Label(root, text="Category:").pack(pady=5)
category_menu = tk.OptionMenu(root, category_var, *categories)
category_menu.pack(pady=5)

tk.Label(root, text="Deadline (YYYY-MM-DD):").pack(pady=5)
deadline_entry = tk.Entry(root, width=40)
deadline_entry.pack(pady=5)

tk.Button(root, text="Submit", command=submit).pack(pady=10)
tk.Button(root, text="Clear", command=clear_fields).pack(pady=5)

root.mainloop()
