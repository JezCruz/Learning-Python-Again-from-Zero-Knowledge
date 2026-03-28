#!/usr/bin/env python3
"""
Directory Analyzer CLI
Analyze directory structure showing sizes and file counts.
"""

import argparse
import os
import sys
from pathlib import Path
from collections import defaultdict


def analyze_directory(root_dir, depth=None):
    """Analyze directory structure."""
    root_path = Path(root_dir)
    
    if not root_path.exists():
        print(f"Error: Directory '{root_dir}' not found.", file=sys.stderr)
        return None
    
    stats = {
        'total_size': 0,
        'total_files': 0,
        'total_dirs': 0,
        'by_extension': defaultdict(lambda: {'size': 0, 'count': 0}),
        'subdirs': {}
    }
    
    try:
        for root, dirs, files in os.walk(root_path):
            current_depth = len(Path(root).relative_to(root_path).parts)
            
            if depth is not None and current_depth >= depth:
                dirs.clear()
                continue
            
            stats['total_dirs'] += len(dirs)
            
            for file in files:
                filepath = Path(root) / file
                try:
                    size = filepath.stat().st_size
                    stats['total_size'] += size
                    stats['total_files'] += 1
                    
                    ext = filepath.suffix or 'NO EXTENSION'
                    stats['by_extension'][ext]['size'] += size
                    stats['by_extension'][ext]['count'] += 1
                except (OSError, IOError):
                    pass
    except PermissionError:
        print("Warning: Permission denied for some directories.", file=sys.stderr)
    
    return stats


def format_size(bytes):
    """Format bytes to human-readable size."""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if bytes < 1024:
            return f"{bytes:.2f}{unit}"
        bytes /= 1024
    return f"{bytes:.2f}TB"


def main():
    parser = argparse.ArgumentParser(
        description="Analyze directory structure"
    )
    
    parser.add_argument('directory', help='Directory to analyze')
    parser.add_argument('-d', '--depth', type=int, help='Maximum depth to analyze')
    parser.add_argument('--top', type=int, default=10,
                       help='Show top N file types (default: 10)')
    
    args = parser.parse_args()
    
    stats = analyze_directory(args.directory, args.depth)
    
    if not stats:
        sys.exit(1)
    
    print(f"\n{'Directory Analysis: ' + args.directory}")
    print("=" * 70)
    
    print(f"\nOverall Statistics:")
    print(f"  Total Size:     {format_size(stats['total_size'])}")
    print(f"  Total Files:    {stats['total_files']}")
    print(f"  Total Dirs:     {stats['total_dirs']}")
    
    if stats['by_extension']:
        print(f"\nTop {args.top} File Types by Size:")
        print(f"{'Extension':<15} {'Count':<10} {'Total Size':<15} {'Avg Size':<12}")
        print("-" * 52)
        
        sorted_exts = sorted(
            stats['by_extension'].items(),
            key=lambda x: x[1]['size'],
            reverse=True
        )[:args.top]
        
        for ext, data in sorted_exts:
            avg_size = data['size'] // data['count'] if data['count'] > 0 else 0
            print(f"{ext:<15} {data['count']:<10} {format_size(data['size']):<15} {format_size(avg_size):<12}")
    
    print("\n" + "=" * 70)


if __name__ == "__main__":
    main()
