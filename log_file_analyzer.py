# Log File Analyzer
import re
from collections import defaultdict
from datetime import datetime

def parse_log_file(log_file_path):
    """
    Parse a log file and extract error patterns
    """
    errors = defaultdict(int)
    warnings = defaultdict(int)
    
    try:
        with open(log_file_path, 'r') as f:
            for line in f:
                line = line.strip()
                if 'ERROR' in line.upper():
                    # Extract error message
                    match = re.search(r'ERROR:\s*(.+?)(?:\n|$)', line)
                    if match:
                        errors[match.group(1)] += 1
                elif 'WARNING' in line.upper():
                    match = re.search(r'WARNING:\s*(.+?)(?:\n|$)', line)
                    if match:
                        warnings[match.group(1)] += 1
        
        return errors, warnings
    except FileNotFoundError:
        print(f"Error: Log file '{log_file_path}' not found")
        return {}, {}

def generate_log_report(errors, warnings):
    """
    Generate a summary report of log analysis
    """
    print("\n=== LOG ANALYSIS REPORT ===")
    print(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    print("ERRORS:")
    if errors:
        for error_msg, count in sorted(errors.items(), key=lambda x: x[1], reverse=True):
            print(f"  [{count}x] {error_msg}")
    else:
        print("  No errors found")
    
    print("\nWARNINGS:")
    if warnings:
        for warning_msg, count in sorted(warnings.items(), key=lambda x: x[1], reverse=True):
            print(f"  [{count}x] {warning_msg}")
    else:
        print("  No warnings found")

if __name__ == "__main__":
    # Example log file analysis
    log_path = "sample.log"
    print("Log File Analyzer v1.0")
    print(f"Looking for log files in current directory...")
