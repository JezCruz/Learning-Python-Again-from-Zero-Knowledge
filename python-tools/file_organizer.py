import os
import shutil

source_folder = input("Enter folder path: ")

file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Music": [".mp3", ".wav"],
    "Programs": [".py", ".js", ".cpp", ".java"]
}

for filename in os.listdir(source_folder):
    file_path = os.path.join(source_folder, filename)

    if os.path.isfile(file_path):
        ext = os.path.splitext(filename)[1].lower()

        moved = False
        for folder, extensions in file_types.items():
            if ext in extensions:
                target_folder = os.path.join(source_folder, folder)
                os.makedirs(target_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(target_folder, filename))
                moved = True
                break

        if not moved:
            other_folder = os.path.join(source_folder, "Others")
            os.makedirs(other_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(other_folder, filename))

print("Files organized successfully!")