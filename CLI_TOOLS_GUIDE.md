# 5 Useful Python CLI Tools

I've generated 5 practical command-line tools for you. Here's a quick guide:

## 1. **Password Generator CLI** (`cli_password_generator.py`)
Generate secure random passwords with customizable options.

**Features:**
- Configurable password length
- Toggle uppercase, lowercase, digits, special characters
- Generate multiple passwords at once

**Usage Examples:**
```bash
python cli_password_generator.py -l 16
python cli_password_generator.py -l 20 --no-special
python cli_password_generator.py -c 5 -l 12  # Generate 5 passwords
```

---

## 2. **Todo Manager CLI** (`cli_todo_manager.py`)
Simple task management with JSON file persistence.

**Features:**
- Add, list, complete, and delete tasks
- Set task priority (low, normal, high)
- Persistent storage in `todos.json`
- Shows creation timestamps

**Usage Examples:**
```bash
python cli_todo_manager.py add "Buy groceries" -p high
python cli_todo_manager.py list
python cli_todo_manager.py complete 1
python cli_todo_manager.py all  # Show completed tasks too
python cli_todo_manager.py delete 2
```

---

## 3. **File Finder CLI** (`cli_file_finder.py`)
Search for files by name, extension, size, or modification date.

**Features:**
- Search by filename (partial match)
- Filter by file extension
- Filter by file size range
- Find recently modified files
- Shows file modification timestamps and human-readable sizes

**Usage Examples:**
```bash
python cli_file_finder.py . -n document
python cli_file_finder.py . -e txt
python cli_file_finder.py . --min-size 1MB --max-size 100MB
python cli_file_finder.py . --days 7  # Modified in last 7 days
```

---

## 4. **Directory Analyzer CLI** (`cli_directory_analyzer.py`)
Analyze directory structure showing sizes and file counts.

**Features:**
- Total directory size and file/directory counts
- Breakdown by file type/extension
- Average file size per type
- Configurable analysis depth
- Human-readable file sizes

**Usage Examples:**
```bash
python cli_directory_analyzer.py .
python cli_directory_analyzer.py . -d 2  # Limit depth
python cli_directory_analyzer.py . --top 20  # Show top 20 file types
```

---

## 5. **Text File Processor CLI** (`cli_text_processor.py`)
Process text files with various operations.

**Features:**
- Case conversion (uppercase, lowercase, title case)
- Remove empty lines and duplicates
- Text statistics (character, word, line count)
- Word frequency analysis
- Find and replace functionality
- Output to new file or display preview

**Usage Examples:**
```bash
python cli_text_processor.py input.txt --uppercase
python cli_text_processor.py input.txt --stats
python cli_text_processor.py input.txt --word-freq 10
python cli_text_processor.py input.txt --lowercase -o output.txt
python cli_text_processor.py input.txt --find "old" --replace "new" -o output.txt
python cli_text_processor.py input.txt --remove-empty
```

---

## Quick Tips

- All tools support `--help` for detailed options
- Add `#!/usr/bin/env python3` at the top allows running as `./filename.py` on Linux/Mac
- Most tools handle errors gracefully with helpful messages
- Use `-o` or `--output` flags to save results to files where applicable

Happy coding! 🚀
