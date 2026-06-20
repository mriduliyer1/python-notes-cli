#!/usr/bin/env python3
"""
Python Notes CLI - Command-line application for managing notes and tasks.
"""

import argparse
import sys
from notes import Note, NotesDB


def main():
    """Main entry point for the CLI application."""
    
    # Create argument parser
    parser = argparse.ArgumentParser(
        description="A simple CLI app for managing notes and tasks",
        prog="python-notes-cli"
    )
    
    # Create subparsers for different commands
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Add command
    add_parser = subparsers.add_parser("add", help="Add a new note")
    add_parser.add_argument("--title", required=True, help="Note title")
    add_parser.add_argument("--description", required=True, help="Note description")
    
    # List command
    list_parser = subparsers.add_parser("list", help="List all notes")
    
    # View command
    view_parser = subparsers.add_parser("view", help="View a specific note")
    view_parser.add_argument("--id", type=int, required=True, help="Note ID")
    
    # Edit command
    edit_parser = subparsers.add_parser("edit", help="Edit a note")
    edit_parser.add_argument("--id", type=int, required=True, help="Note ID")
    edit_parser.add_argument("--title", help="New note title")
    edit_parser.add_argument("--description", help="New note description")
    
    # Delete command
    delete_parser = subparsers.add_parser("delete", help="Delete a note")
    delete_parser.add_argument("--id", type=int, required=True, help="Note ID")
    
    # Parse arguments
    args = parser.parse_args()
    
    # Initialize database
    db = NotesDB()
    
    # Execute commands
    if args.command == "add":
        note = Note(title=args.title, description=args.description)
        note_id = db.add_note(note)
        print(f"✅ Note added successfully with ID: {note_id}")
    
    elif args.command == "list":
        notes = db.get_all_notes()
        if not notes:
            print("📭 No notes found. Create one with: python main.py add --title \"...\" --description \"...\"")
        else:
            print("\n📋 Your Notes:\n")
            for note in notes:
                print(f"ID: {note['id']}")
                print(f"Title: {note['title']}")
                print(f"Description: {note['description']}")
                print(f"Created: {note['created_at']}")
                print("-" * 50)
    
    elif args.command == "view":
        note = db.get_note(args.id)
        if note:
            print(f"\n📝 Note ID: {note['id']}")
            print(f"Title: {note['title']}")
            print(f"Description: {note['description']}")
            print(f"Created: {note['created_at']}")
        else:
            print(f"❌ Note with ID {args.id} not found.")
            sys.exit(1)
    
    elif args.command == "edit":
        note = db.get_note(args.id)
        if not note:
            print(f"❌ Note with ID {args.id} not found.")
            sys.exit(1)
        
        # Use existing values if new ones not provided
        title = args.title if args.title else note['title']
        description = args.description if args.description else note['description']
        
        updated_note = Note(title=title, description=description)
        db.update_note(args.id, updated_note)
        print(f"✏️ Note {args.id} updated successfully.")
    
    elif args.command == "delete":
        note = db.get_note(args.id)
        if not note:
            print(f"❌ Note with ID {args.id} not found.")
            sys.exit(1)
        
        db.delete_note(args.id)
        print(f"🗑️ Note {args.id} deleted successfully.")
    
    else:
        parser.print_help()
        sys.exit(0)


if __name__ == "__main__":
    main()
