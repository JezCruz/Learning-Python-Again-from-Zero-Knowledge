# Daily Task Tracker

import json
import os

FILE_NAME = "tasks.json"

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent=4)

def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks yet.\n")
        return
    print("\nYour Tasks:")
    for i, task in enumerate(tasks):
        status = "✔" if task["done"] else "✘"
        print(f"{i+1}. [{status}] {task['title']}")
    print()

def add_task(tasks):
    title = input("Enter task: ")
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print("Task added!\n")

def mark_done(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Enter task number to mark as done: ")) - 1
        tasks[index]["done"] = True
        save_tasks(tasks)
        print("Task marked as done!\n")
    except:
        print("Invalid input.\n")

def delete_task(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Enter task number to delete: ")) - 1
        tasks.pop(index)
        save_tasks(tasks)
        print("Task deleted!\n")
    except:
        print("Invalid input.\n")

def main():
    tasks = load_tasks()
    
    while True:
        print("==== TO-DO LIST ====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark as Done")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Choose: ")
        
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.\n")

if __name__ == "__main__":
    main()