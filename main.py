# ============================================
# Developers Task Management System (by Adyan)
# ============================================

import json
import os

TASKS_FILE = "tasks.json"
tasks = []

# ------------------ File Operations ------------------

def load_tasks():
    """Load tasks from JSON file if it exists."""
    global tasks
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r", encoding="utf-8") as f:
            try:
                tasks = json.load(f)
            except json.JSONDecodeError:
                tasks = []
    else:
        tasks = []

def save_tasks():
    """Save all tasks to JSON file."""
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=4, ensure_ascii=False)

# ------------------ Core Functions ------------------

def show_menu():
    print("\n=== 🧩 Developers Task Management ===")
    print("1. ➕ Add new task")
    print("2. 📋 View all tasks")
    print("3. ✅ Mark task as completed")
    print("4. 🗑 Delete task")
    print("5. 🔄 Clear all tasks")
    print("6. 🚪 Exit")

def add_task():
    title = input("Enter task title: ").strip()
    if not title:
        print("⚠ Task title cannot be empty.")
        return
    tasks.append({"title": title, "completed": False})
    save_tasks()
    print(f"✅ Task '{title}' added successfully.")

def view_tasks():
    if not tasks:
        print("📭 No tasks found.")
        return
    print("\nYour Tasks:")
    for i, task in enumerate(tasks, start=1):
        status = "✔ Done" if task["completed"] else "❌ Not done"
        print(f"{i}. {task['title']} - {status}")

def complete_task():
    view_tasks()
    if not tasks:
        return
    try:
        num = int(input("\nEnter task number to mark as completed: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["completed"] = True
            save_tasks()
            print("🎯 Task marked as completed!")
        else:
            print("⚠ Invalid task number.")
    except ValueError:
        print("⚠ Please enter a valid number.")

def delete_task():
    view_tasks()
    if not tasks:
        return
    try:
        num = int(input("\nEnter task number to delete: "))
        if 1 <= num <= len(tasks):
            deleted = tasks.pop(num - 1)
            save_tasks()
            print(f"🗑 Task '{deleted['title']}' deleted.")
        else:
            print("⚠ Invalid task number.")
    except ValueError:
        print("⚠ Please enter a valid number.")

def clear_all():
    confirm = input("⚠ Are you sure you want to delete ALL tasks? (y/n): ").lower()
    if confirm == "y":
        tasks.clear()
        save_tasks()
        print("🧹 All tasks cleared!")
    else:
        print("❎ Operation canceled.")

# ------------------ Main Loop ------------------

def main():
    load_tasks()
    print("Welcome back, Developer 👋")
    while True:
        show_menu()
        choice = input("Select an option: ").strip()
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            clear_all()
        elif choice == "6":
            print("Goodbye 👋 See you later.")
            break
        else:
            print("⚠ Invalid choice, please try again.")

# ------------------ Run ------------------
if __name__ == "__main__":
    main()
