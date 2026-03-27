# Batch File Renamer
import os
import re
from pathlib import Path

def rename_files_add_prefix(directory, prefix, file_extension=None):
    """
    Add a prefix to all files in a directory
    """
    try:
        files = os.listdir(directory)
        renamed_count = 0
        
        for filename in files:
            filepath = os.path.join(directory, filename)
            
            if os.path.isfile(filepath):
                if file_extension is None or filename.endswith(file_extension):
                    new_name = f"{prefix}_{filename}"
                    new_path = os.path.join(directory, new_name)
                    os.rename(filepath, new_path)
                    print(f"✓ {filename} → {new_name}")
                    renamed_count += 1
        
        print(f"\nTotal files renamed: {renamed_count}")
        return renamed_count
    except Exception as e:
        print(f"Error: {e}")
        return 0

def rename_files_sequential(directory, base_name, file_extension):
    """
    Rename files sequentially (file_1, file_2, etc.)
    """
    try:
        files = [f for f in os.listdir(directory) if f.endswith(file_extension)]
        files.sort()
        renamed_count = 0
        
        for idx, filename in enumerate(files, 1):
            filepath = os.path.join(directory, filename)
            ext = Path(filename).suffix
            new_name = f"{base_name}_{idx}{ext}"
            new_path = os.path.join(directory, new_name)
            os.rename(filepath, new_path)
            print(f"✓ {filename} → {new_name}")
            renamed_count += 1
        
        print(f"\nTotal files renamed: {renamed_count}")
        return renamed_count
    except Exception as e:
        print(f"Error: {e}")
        return 0

def remove_pattern_from_filenames(directory, pattern):
    """
    Remove a specific pattern from all filenames
    """
    try:
        files = os.listdir(directory)
        renamed_count = 0
        
        for filename in files:
            filepath = os.path.join(directory, filename)
            if os.path.isfile(filepath) and pattern in filename:
                new_name = filename.replace(pattern, '')
                new_path = os.path.join(directory, new_name)
                os.rename(filepath, new_path)
                print(f"✓ {filename} → {new_name}")
                renamed_count += 1
        
        print(f"\nTotal files renamed: {renamed_count}")
        return renamed_count
    except Exception as e:
        print(f"Error: {e}")
        return 0

if __name__ == "__main__":
    print("Batch File Renamer Tool")
    print("Use the functions to rename files in bulk")
