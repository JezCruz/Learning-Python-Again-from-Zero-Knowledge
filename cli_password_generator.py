#!/usr/bin/env python3
"""
Password Generator CLI
Generate secure random passwords with customizable options.
"""

import argparse
import random
import string
import sys


def generate_password(length=12, uppercase=True, lowercase=True, digits=True, special=True):
    """Generate a random password based on specified criteria."""
    characters = ""
    
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if digits:
        characters += string.digits
    if special:
        characters += string.punctuation
    
    if not characters:
        print("Error: At least one character type must be selected.", file=sys.stderr)
        return None
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def main():
    parser = argparse.ArgumentParser(
        description="Generate secure random passwords",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="Examples:\n"
               "  python cli_password_generator.py -l 16\n"
               "  python cli_password_generator.py -l 20 --no-special\n"
               "  python cli_password_generator.py -c 5 -l 12"
    )
    
    parser.add_argument('-l', '--length', type=int, default=12,
                        help='Password length (default: 12)')
    parser.add_argument('-c', '--count', type=int, default=1,
                        help='Number of passwords to generate (default: 1)')
    parser.add_argument('--no-uppercase', action='store_true',
                        help='Exclude uppercase letters')
    parser.add_argument('--no-lowercase', action='store_true',
                        help='Exclude lowercase letters')
    parser.add_argument('--no-digits', action='store_true',
                        help='Exclude digits')
    parser.add_argument('--no-special', action='store_true',
                        help='Exclude special characters')
    
    args = parser.parse_args()
    
    if args.length < 4:
        print("Error: Password length must be at least 4.", file=sys.stderr)
        sys.exit(1)
    
    print(f"Generating {args.count} password(s) ({args.length} characters each):\n")
    
    for _ in range(args.count):
        pwd = generate_password(
            length=args.length,
            uppercase=not args.no_uppercase,
            lowercase=not args.no_lowercase,
            digits=not args.no_digits,
            special=not args.no_special
        )
        if pwd:
            print(f"  {pwd}")


if __name__ == "__main__":
    main()
