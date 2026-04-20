#!/usr/bin/env python3
"""
Text File Processor CLI
Process text files with various operations.
"""

import argparse
import sys
from pathlib import Path
from collections import Counter
import re


class TextProcessor:
    def __init__(self, filepath):
        self.filepath = Path(filepath)
        if not self.filepath.exists():
            raise FileNotFoundError(f"File '{filepath}' not found.")
        
        with open(self.filepath, 'r', encoding='utf-8', errors='ignore') as f:
            self.content = f.read()
    
    def uppercase(self):
        """Convert text to uppercase."""
        return self.content.upper()
    
    def lowercase(self):
        """Convert text to lowercase."""
        return self.content.lower()
    
    def title_case(self):
        """Convert text to title case."""
        return self.content.title()
    
    def remove_empty_lines(self):
        """Remove empty lines."""
        lines = [line for line in self.content.split('\n') if line.strip()]
        return '\n'.join(lines)
    
    def word_count(self):
        """Count words in text."""
        words = self.content.split()
        return len(words)
    
    def line_count(self):
        """Count lines in text."""
        return len(self.content.split('\n'))
    
    def char_count(self):
        """Count characters."""
        return len(self.content)
    
    def word_frequency(self, top_n=20):
        """Get top N most frequent words."""
        words = re.findall(r'\b\w+\b', self.content.lower())
        counter = Counter(words)
        return counter.most_common(top_n)
    
    def remove_duplicates(self, by_line=True):
        """Remove duplicate lines or words."""
        if by_line:
            seen = set()
            lines = []
            for line in self.content.split('\n'):
                if line not in seen:
                    seen.add(line)
                    lines.append(line)
            return '\n'.join(lines)
        else:
            words = self.content.split()
            seen = set()
            unique = []
            for word in words:
                if word not in seen:
                    seen.add(word)
                    unique.append(word)
            return ' '.join(unique)
    
    def replace_text(self, old, new):
        """Replace text."""
        return self.content.replace(old, new)
    
    def save(self, filepath):
        """Save processed text to file."""
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(self.content)
        print(f"✓ Saved to {filepath}")


def main():
    parser = argparse.ArgumentParser(
        description="Process text files with various operations",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="Examples:\n"
               "  python cli_text_processor.py input.txt --uppercase\n"
               "  python cli_text_processor.py input.txt --stats\n"
               "  python cli_text_processor.py input.txt --word-freq 10\n"
               "  python cli_text_processor.py input.txt --lowercase -o output.txt"
    )
    
    parser.add_argument('input_file', help='Input text file')
    parser.add_argument('-o', '--output', help='Output file (if not specified, only displays result)')
    
    # Processing options
    parser.add_argument('--uppercase', action='store_true', help='Convert to uppercase')
    parser.add_argument('--lowercase', action='store_true', help='Convert to lowercase')
    parser.add_argument('--title', action='store_true', help='Convert to title case')
    parser.add_argument('--remove-empty', action='store_true', help='Remove empty lines')
    parser.add_argument('--remove-duplicates', action='store_true', help='Remove duplicate lines')
    
    # Analytics
    parser.add_argument('--stats', action='store_true', help='Show text statistics')
    parser.add_argument('--word-freq', type=int, metavar='N', 
                       help='Show top N most frequent words')
    
    # Find and replace
    parser.add_argument('--find', help='Find text (use with --replace)')
    parser.add_argument('--replace', help='Replace text (use with --find)')
    
    args = parser.parse_args()
    
    try:
        processor = TextProcessor(args.input_file)
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    
    # Store original content for processing
    original_content = processor.content
    
    # Apply transformations
    if args.uppercase:
        processor.content = processor.uppercase()
        print("Applied: uppercase\n")
    
    if args.lowercase:
        processor.content = processor.lowercase()
        print("Applied: lowercase\n")
    
    if args.title:
        processor.content = processor.title_case()
        print("Applied: title case\n")
    
    if args.remove_empty:
        processor.content = processor.remove_empty_lines()
        print("Applied: removed empty lines\n")
    
    if args.remove_duplicates:
        processor.content = processor.remove_duplicates()
        print("Applied: removed duplicate lines\n")
    
    if args.find and args.replace:
        old_count = processor.content.count(args.find)
        processor.content = processor.replace_text(args.find, args.replace)
        print(f"Applied: replaced {old_count} occurrence(s)\n")
    
    # Display analytics
    if args.stats:
        print("Text Statistics:")
        print(f"  Characters: {processor.char_count()}")
        print(f"  Words:      {processor.word_count()}")
        print(f"  Lines:      {processor.line_count()}")
        print()
    
    if args.word_freq:
        print(f"Top {args.word_freq} Most Frequent Words:")
        for word, count in processor.word_frequency(args.word_freq):
            print(f"  {word:<20} {count:>5} times")
        print()
    
    # Display or save result
    if not (args.uppercase or args.lowercase or args.title or args.remove_empty 
            or args.remove_duplicates or (args.find and args.replace)):
        # No transformation applied, just show content or stats
        if args.stats or args.word_freq:
            return
        print("No operation specified. Use --help for available options.")
        return
    
    if args.output:
        processor.save(args.output)
    else:
        print("Processed Content (first 500 characters):")
        print("-" * 50)
        preview = processor.content[:500]
        print(preview)
        if len(processor.content) > 500:
            print(f"\n... ({len(processor.content) - 500} more characters)")
        print("\nUse -o/--output to save the result to a file.")


if __name__ == "__main__":
    main()
