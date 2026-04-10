filename = input("Enter text file name: ")

try:
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()

    words = content.split()
    lines = content.splitlines()
    characters = len(content)

    print("\n--- FILE STATS ---")
    print("Lines:", len(lines))
    print("Words:", len(words))
    print("Characters:", characters)

except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print("Error:", e)