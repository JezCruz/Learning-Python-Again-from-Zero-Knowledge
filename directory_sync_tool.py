# Directory Sync Tool
import os
import shutil
from pathlib import Path
from typing import List, Tuple

class DirectorySync:
    """
    Synchronize files between two directories
    """
    
    def __init__(self, source_dir: str, target_dir: str):
        self.source_dir = source_dir
        self.target_dir = target_dir
    
    def get_file_list(self, directory: str) -> set:
        """
        Get all files in a directory recursively
        """
        files = set()
        for root, dirs, filenames in os.walk(directory):
            for filename in filenames:
                rel_path = os.path.relpath(os.path.join(root, filename), directory)
                files.add(rel_path)
        return files
    
    def sync_one_way(self, delete_missing: bool = False) -> Tuple[int, int]:
        """
        Sync files from source to target (one-way)
        """
        source_files = self.get_file_list(self.source_dir)
        target_files = self.get_file_list(self.target_dir)
        
        copied_count = 0
        deleted_count = 0
        
        # Copy/update files from source to target
        for file in source_files:
            source_path = os.path.join(self.source_dir, file)
            target_path = os.path.join(self.target_dir, file)
            
            # Create directory if needed
            os.makedirs(os.path.dirname(target_path), exist_ok=True)
            
            # Copy file if it doesn't exist or is older
            if not os.path.exists(target_path) or os.path.getmtime(source_path) > os.path.getmtime(target_path):
                shutil.copy2(source_path, target_path)
                print(f"✓ Copied: {file}")
                copied_count += 1
        
        # Delete files in target that don't exist in source
        if delete_missing:
            for file in target_files:
                if file not in source_files:
                    target_path = os.path.join(self.target_dir, file)
                    os.remove(target_path)
                    print(f"✗ Deleted: {file}")
                    deleted_count += 1
        
        return copied_count, deleted_count
    
    def get_sync_stats(self) -> dict:
        """
        Get synchronization statistics
        """
        source_files = self.get_file_list(self.source_dir)
        target_files = self.get_file_list(self.target_dir)
        
        missing_in_target = source_files - target_files
        extra_in_target = target_files - source_files
        
        return {
            'source_file_count': len(source_files),
            'target_file_count': len(target_files),
            'missing_in_target': len(missing_in_target),
            'extra_in_target': len(extra_in_target)
        }

if __name__ == "__main__":
    print("Directory Sync Tool v1.0")
    print("Use to synchronize files between directories")
