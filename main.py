# ============================================
# Developers Task Management System (by Adyan)
# ============================================

import json
import os
import tkinter as tk
from tkinter import messagebox, simpledialog

TASKS_FILE = "tasks.json"

# -------------------- Load / Save Tasks --------------------

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_tasks():
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=4, ensure_ascii=False)


# -------------------- Update Progress --------------------

def update_progress():
    if len(tasks) == 0:
        progress_var.set(0)
    else:
        done_count = sum(1 for t in tasks if t["done"])
        percent = int((done_count / len(tasks)) * 100)
        progress_var.set(percent)
    progress_label.config(text=f"نسبة الإنجاز: {progress_var.get()}%")


# -------------------- Refresh List --------------------

def refresh_list():
    listbox.delete(0, tk.END)
    for t in tasks:
        mark = "✔️" if t["done"] else "❌"
        listbox.insert(tk.END, f"{mark}  {t['title']}")
    update_progress()


# -------------------- Add Task --------------------

def add_task():
    title = entry.get().strip()
    if title == "":
        messagebox.showwarning("تنبيه", "اكتب مهمة!")
        return

    tasks.append({"title": title, "done": False})
    entry.delete(0, tk.END)
    save_tasks()
    refresh_list()


# -------------------- Delete Task --------------------

def delete_task():
    selected = listbox.curselection()
    if not selected:
        messagebox.showwarning("تنبيه", "اختار مهمة حتى تحذفها!")
        return

    index = selected[0]
    tasks.pop(index)
    save_tasks()
    refresh_list()


# -------------------- Toggle Complete --------------------

def toggle_task():
    selected = listbox.curselection()
    if not selected:
        messagebox.showwarning("تنبيه", "اختار مهمة!")
        return

    index = selected[0]
    tasks[index]["done"] = not tasks[index]["done"]
    save_tasks()
    refresh_list()


# -------------------- GUI --------------------

root = tk.Tk()
root.title("To-Do List")
root.geometry("350x500")
root.configure(bg="#222")

tasks = load_tasks()

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10, padx=10, fill="x")

add_btn = tk.Button(root, text="إضافة مهمة", font=("Arial", 12), command=add_task)
add_btn.pack(pady=5)

frame = tk.Frame(root)
frame.pack(pady=10)

listbox = tk.Listbox(frame, width=30, height=12, font=("Arial", 14))
listbox.pack(side=tk.LEFT)

scroll = tk.Scrollbar(frame, command=listbox.yview)
scroll.pack(side=tk.RIGHT, fill=tk.Y)
listbox.config(yscrollcommand=scroll.set)

toggle_btn = tk.Button(root, text="تبديل الإنجاز ✔️❌", font=("Arial", 12), command=toggle_task)
toggle_btn.pack(pady=5)

delete_btn = tk.Button(root, text="حذف المهمة 🗑️", font=("Arial", 12), command=delete_task)
delete_btn.pack(pady=5)

progress_var = tk.IntVar()
progress_label = tk.Label(root, text="نسبة الإنجاز: 0%", font=("Arial", 14), bg="#222", fg="white")
progress_label.pack(pady=15)

progress_bar = tk.Canvas(root, width=300, height=20, bg="white")
progress_bar.pack()

def draw_progress(*args):
    progress_bar.delete("all")
    percent = progress_var.get()
    fill_width = 3 * percent
    progress_bar.create_rectangle(0, 0, fill_width, 20, fill="green")

progress_var.trace("w", draw_progress)

refresh_list()

root.mainloop()
