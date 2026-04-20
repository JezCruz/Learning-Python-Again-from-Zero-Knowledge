#!/usr/bin/env python3
"""
Todo Manager CLI
Simple task management with file persistence.
"""

import argparse
import json
import os
import sys
from datetime import datetime


class TodoManager:
    def __init__(self, filename="todos.json"):
        self.filename = filename
        self.todos = self.load_todos()
    
    def load_todos(self):
        """Load todos from file."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                return json.load(f)
        return []
    
    def save_todos(self):
        """Save todos to file."""
        with open(self.filename, 'w') as f:
            json.dump(self.todos, f, indent=2)
    
    def add(self, task, priority="normal"):
        """Add a new todo."""
        todo = {
            "id": len(self.todos) + 1,
            "task": task,
            "priority": priority,
            "completed": False,
            "created": datetime.now().isoformat()
        }
        self.todos.append(todo)
        self.save_todos()
        print(f"✓ Added: {task} (ID: {todo['id']})")
    
    def list_todos(self, show_completed=False):
        """List all todos."""
        if not self.todos:
            print("No todos yet!")
            return
        
        active = [t for t in self.todos if not t['completed']] if not show_completed else self.todos
        
        if not active:
            print("All tasks completed!")
            return
        
        print(f"\n{'ID':<4} {'Status':<8} {'Priority':<10} {'Task':<40}")
        print("-" * 65)
        
        for todo in active:
            status = "✓" if todo['completed'] else "○"
            print(f"{todo['id']:<4} {status:<8} {todo['priority']:<10} {todo['task']:<40}")
    
    def complete(self, todo_id):
        """Mark a todo as completed."""
        for todo in self.todos:
            if todo['id'] == todo_id:
                todo['completed'] = True
                self.save_todos()
                print(f"✓ Completed: {todo['task']}")
                return
        print(f"Todo with ID {todo_id} not found.")
    
    def delete(self, todo_id):
        """Delete a todo."""
        for i, todo in enumerate(self.todos):
            if todo['id'] == todo_id:
                task = todo['task']
                self.todos.pop(i)
                self.save_todos()
                print(f"✓ Deleted: {task}")
                return
        print(f"Todo with ID {todo_id} not found.")


def main():
    parser = argparse.ArgumentParser(description="Simple Todo Manager")
    subparsers = parser.add_subparsers(dest='command', help='Commands')
    
    subparsers.add_parser('list', help='List all todos')
    subparsers.add_parser('all', help='List all todos including completed')
    
    add_parser = subparsers.add_parser('add', help='Add a new todo')
    add_parser.add_argument('task', help='Task description')
    add_parser.add_argument('-p', '--priority', choices=['low', 'normal', 'high'],
                           default='normal', help='Task priority')
    
    complete_parser = subparsers.add_parser('complete', help='Mark todo as completed')
    complete_parser.add_argument('id', type=int, help='Todo ID')
    
    delete_parser = subparsers.add_parser('delete', help='Delete a todo')
    delete_parser.add_argument('id', type=int, help='Todo ID')
    
    args = parser.parse_args()
    
    manager = TodoManager()
    
    if args.command == 'add':
        manager.add(args.task, args.priority)
    elif args.command == 'complete':
        manager.complete(args.id)
    elif args.command == 'delete':
        manager.delete(args.id)
    elif args.command == 'all':
        manager.list_todos(show_completed=True)
    else:
        manager.list_todos()


if __name__ == "__main__":
    main()
