import json
import os
from datetime import datetime

FILE_NAME = "python-tools/json_files/chronicle_journal_entries.json"


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
    print("\n===== ADD NEW JOURNAL ENTRY =====")

    author = input("Enter author name: ").strip()
    journal_title = input("Enter journal title: ").strip()
    content = input("Enter journal content: ").strip()

    now = datetime.now()
    date_created = now.strftime("%Y-%m-%d")
    time_created = now.strftime("%I:%M:%S %p")

    entry = {
        "author": author,
        "title": journal_title,
        "date": date_created,
        "time": time_created,
        "content": content
    }

    entries.append(entry)
    save_entries(entries)

    print("\nJournal entry saved successfully!")


def view_entries(entries):
    if not entries:
        print("\nNo journal entries found.")
        return

    print("\n===== ALL JOURNAL ENTRIES =====")
    for i, entry in enumerate(entries, start=1):
        print(f"\nEntry #{i}")
        print(f"Title  : {entry['title']}")
        print(f"Author : {entry['author']}")
        print(f"Date   : {entry['date']}")
        print(f"Time   : {entry['time']}")
        print(f"Content: {entry['content']}")


def search_by_title(entries):
    if not entries:
        print("\nNo journal entries found.")
        return

    keyword = input("Enter title keyword to search: ").strip().lower()
    found = False

    print("\n===== SEARCH RESULTS =====")
    for i, entry in enumerate(entries, start=1):
        if keyword in entry["title"].lower():
            found = True
            print(f"\nEntry #{i}")
            print(f"Title  : {entry['title']}")
            print(f"Author : {entry['author']}")
            print(f"Date   : {entry['date']}")
            print(f"Time   : {entry['time']}")
            print(f"Content: {entry['content']}")

    if not found:
        print("No matching journal title found.")


def main():
    entries = load_entries()

    while True:
        print("\n==============================")
        print("   CHRONICLE JOURNAL MAKER")
        print("==============================")
        print("1. Add New Journal Entry")
        print("2. View All Journal Entries")
        print("3. Search Journal by Title")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_entry(entries)
        elif choice == "2":
            view_entries(entries)
        elif choice == "3":
            search_by_title(entries)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1 to 4.")


if __name__ == "__main__":
    main()