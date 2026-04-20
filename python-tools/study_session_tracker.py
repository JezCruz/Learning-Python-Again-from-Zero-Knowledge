import json
import os
from datetime import datetime

FILE_NAME = "python-tools/json_files/study_sessions.json"


def load_sessions():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r", encoding="utf-8") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []
    return []


def save_sessions(sessions):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(sessions, file, indent=4, ensure_ascii=False)


def add_session(sessions):
    subject = input("Enter subject or skill: ").strip()

    while True:
        hours_input = input("Enter hours studied: ").strip()
        try:
            hours = float(hours_input)
            if hours <= 0:
                print("Hours must be greater than 0.")
                continue
            break
        except ValueError:
            print("Invalid input. Enter a number only.")

    date_today = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    session = {
        "subject": subject,
        "hours": hours,
        "date": date_today
    }

    sessions.append(session)
    save_sessions(sessions)
    print("Study session saved successfully!")


def view_sessions(sessions):
    if not sessions:
        print("No study sessions yet.")
        return

    print("\n===== ALL STUDY SESSIONS =====")
    for i, session in enumerate(sessions, start=1):
        print(f"\nSession #{i}")
        print(f"Subject : {session['subject']}")
        print(f"Hours   : {session['hours']}")
        print(f"Date    : {session['date']}")


def show_total_hours(sessions):
    if not sessions:
        print("No study sessions yet.")
        return

    total = sum(session["hours"] for session in sessions)
    print(f"\nTotal study hours: {total:.2f}")


def main():
    sessions = load_sessions()

    while True:
        print("\n===== STUDY SESSION TRACKER =====")
        print("1. Add Study Session")
        print("2. View All Sessions")
        print("3. Show Total Hours")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_session(sessions)
        elif choice == "2":
            view_sessions(sessions)
        elif choice == "3":
            show_total_hours(sessions)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1 to 4.")


if __name__ == "__main__":
    main()