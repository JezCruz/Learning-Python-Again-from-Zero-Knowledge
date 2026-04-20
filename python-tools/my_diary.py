import json
import os
from datetime import datetime

FILE_NAME = "python-tools/json_files/diary_entries.json"


def load_entries():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r", encoding="utf-8") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []
    return []


def save_entries(entries):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(entries, file, indent=4, ensure_ascii=False)


def add_entry(entries):
    name = input("Enter your name: ").strip()
    title = input("Enter diary title: ").strip()
    content = input("Write your diary entry: ").strip()
    date_created = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    entry = {
        "name": name,
        "title": title,
        "content": content,
        "date_created": date_created
    }

    entries.append(entry)
    save_entries(entries)
    print("Diary entry saved successfully!")


def view_entries(entries):
    if not entries:
        print("No diary entries yet.")
        return

    print("\n===== ALL DIARY ENTRIES =====")
    for i, entry in enumerate(entries, start=1):
        print(f"\nEntry #{i}")
        print(f"Name   : {entry['name']}")
        print(f"Title  : {entry['title']}")
        print(f"Content: {entry['content']}")
        print(f"Date   : {entry['date_created']}")


def main():
    entries = load_entries()

    while True:
        print("\n===== DIARY PROGRAM =====")
        print("1. Add Diary Entry")
        print("2. View All Entries")
        print("3. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_entry(entries)
        elif choice == "2":
            view_entries(entries)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1 to 3.")


if __name__ == "__main__":
    main()