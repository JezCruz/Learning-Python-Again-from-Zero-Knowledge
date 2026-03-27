# File Backup Automation
import os
import shutil
from datetime import datetime
import json

def backup_directory(source_dir, backup_base_dir="backups"):
    """
    Create a timestamped backup of a directory
    """
    if not os.path.exists(source_dir):
        print(f"Error: Source directory '{source_dir}' not found")
        return False
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"{os.path.basename(source_dir)}_backup_{timestamp}"
    backup_path = os.path.join(backup_base_dir, backup_name)
    
    try:
        os.makedirs(backup_base_dir, exist_ok=True)
        shutil.copytree(source_dir, backup_path)
        print(f"✓ Backup created: {backup_path}")
        return True
    except Exception as e:
        print(f"✗ Backup failed: {e}")
        return False

def backup_file(file_path, backup_dir="backups"):
    """
    Create a timestamped backup of a single file
    """
    if not os.path.isfile(file_path):
        print(f"Error: File '{file_path}' not found")
        return False
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.basename(file_path)
    name, ext = os.path.splitext(filename)
    backup_filename = f"{name}_backup_{timestamp}{ext}"
    backup_path = os.path.join(backup_dir, backup_filename)
    
    try:
        os.makedirs(backup_dir, exist_ok=True)
        shutil.copy2(file_path, backup_path)
        print(f"✓ File backup created: {backup_path}")
        return True
    except Exception as e:
        print(f"✗ Backup failed: {e}")
        return False

if __name__ == "__main__":
    # Example usage
    test_file = "test21.py"
    if os.path.exists(test_file):
        backup_file(test_file)
    print("Backup automation ready to use")
