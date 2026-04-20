#!/usr/bin/env python3
"""
File Finder CLI
Search for files by name, extension, size, or modification date.
"""

import argparse
import os
import sys
from pathlib import Path
from datetime import datetime, timedelta


def find_files(root_dir, name=None, extension=None, min_size=None, max_size=None, days=None):
    """Find files matching specified criteria."""
    matches = []
    root_path = Path(root_dir)
    
    if not root_path.exists():
        print(f"Error: Directory '{root_dir}' not found.", file=sys.stderr)
        return matches
    
    cutoff_date = datetime.now() - timedelta(days=days) if days else None
    
    for filepath in root_path.rglob('*'):
        if filepath.is_file():
            # Check name
            if name and name.lower() not in filepath.name.lower():
                continue
            
            # Check extension
            if extension and not filepath.suffix.lower() == f".{extension.lstrip('.')}".lower():
                continue
            
            # Check file size
            file_size = filepath.stat().st_size
            if min_size and file_size < min_size:
                continue
            if max_size and file_size > max_size:
                continue
            
            # Check modification date
            if cutoff_date:
                mod_time = datetime.fromtimestamp(filepath.stat().st_mtime)
                if mod_time < cutoff_date:
                    continue
            
            matches.append(filepath)
    
    return sorted(matches)


def format_size(bytes):
    """Format bytes to human-readable size."""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if bytes < 1024:
            return f"{bytes:.1f}{unit}"
        bytes /= 1024
    return f"{bytes:.1f}TB"


def main():
    parser = argparse.ArgumentParser(
        description="Find files by various criteria",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="Examples:\n"
               "  python cli_file_finder.py . -n document\n"
               "  python cli_file_finder.py . -e txt\n"
               "  python cli_file_finder.py . --min-size 1MB --max-size 100MB\n"
               "  python cli_file_finder.py . --days 7"
    )
    
    parser.add_argument('directory', help='Root directory to search')
    parser.add_argument('-n', '--name', help='Search by filename (partial match)')
    parser.add_argument('-e', '--extension', help='Search by file extension')
    parser.add_argument('--min-size', help='Minimum file size (e.g., 1KB, 1MB)')
    parser.add_argument('--max-size', help='Maximum file size (e.g., 100MB, 1GB)')
    parser.add_argument('--days', type=int, help='Modified in last N days')
    
    args = parser.parse_args()
    
    # Parse size arguments
    def parse_size(size_str):
        if not size_str:
            return None
        units = {'B': 1, 'KB': 1024, 'MB': 1024**2, 'GB': 1024**3, 'TB': 1024**4}
        for unit, multiplier in units.items():
            if size_str.upper().endswith(unit):
                return int(float(size_str[:-len(unit)]) * multiplier)
        return int(size_str)
    
    min_size = parse_size(args.min_size)
    max_size = parse_size(args.max_size)
    
    # Find files
    results = find_files(
        args.directory,
        name=args.name,
        extension=args.extension,
        min_size=min_size,
        max_size=max_size,
        days=args.days
    )
    
    if not results:
        print("No files found matching criteria.")
        return
    
    print(f"\nFound {len(results)} file(s):\n")
    print(f"{'Filename':<50} {'Size':<12} {'Modified':<20}")
    print("-" * 82)
    
    for filepath in results:
        stat = filepath.stat()
        mod_time = datetime.fromtimestamp(stat.st_mtime).strftime("%Y-%m-%d %H:%M")
        size = format_size(stat.st_size)
        print(f"{str(filepath.relative_to(args.directory)):<50} {size:<12} {mod_time:<20}")


if __name__ == "__main__":
    main()
