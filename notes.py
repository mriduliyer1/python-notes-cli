"""
Database and Note model for the Notes CLI application.
"""

import sqlite3
from datetime import datetime
from pathlib import Path


class Note:
    """Represents a single note."""
    
    def __init__(self, title, description):
        """
        Initialize a Note.
        
        Args:
            title (str): The title of the note
            description (str): The description/content of the note
        """
        self.title = title
        self.description = description
        self.created_at = datetime.now().isoformat()
    
    def to_dict(self):
        """Convert note to dictionary."""
        return {
            "title": self.title,
            "description": self.description,
            "created_at": self.created_at
        }


class NotesDB:
    """Manages the SQLite database for notes."""
    
    DB_FILE = "notes.db"
    
    def __init__(self):
        """Initialize the database connection and create table if needed."""
        self.connection = sqlite3.connect(self.DB_FILE)
        self.connection.row_factory = sqlite3.Row  # Return rows as dictionaries
        self.create_table()
    
    def create_table(self):
        """Create the notes table if it doesn't exist."""
        cursor = self.connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS notes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT NOT NULL,
                created_at TEXT NOT NULL
            )
        """)
        self.connection.commit()
    
    def add_note(self, note):
        """
        Add a new note to the database.
        
        Args:
            note (Note): The note to add
        
        Returns:
            int: The ID of the added note
        """
        cursor = self.connection.cursor()
        cursor.execute("""
            INSERT INTO notes (title, description, created_at)
            VALUES (?, ?, ?)
        """, (note.title, note.description, note.created_at))
        self.connection.commit()
        return cursor.lastrowid
    
    def get_all_notes(self):
        """
        Retrieve all notes from the database.
        
        Returns:
            list: List of note dictionaries
        """
        cursor = self.connection.cursor()
        cursor.execute("SELECT id, title, description, created_at FROM notes")
        return [dict(row) for row in cursor.fetchall()]
    
    def get_note(self, note_id):
        """
        Retrieve a specific note by ID.
        
        Args:
            note_id (int): The ID of the note
        
        Returns:
            dict: The note as a dictionary, or None if not found
        """
        cursor = self.connection.cursor()
        cursor.execute("SELECT id, title, description, created_at FROM notes WHERE id = ?", (note_id,))
        row = cursor.fetchone()
        return dict(row) if row else None
    
    def update_note(self, note_id, note):
        """
        Update an existing note.
        
        Args:
            note_id (int): The ID of the note to update
            note (Note): The updated note object
        """
        cursor = self.connection.cursor()
        cursor.execute("""
            UPDATE notes
            SET title = ?, description = ?
            WHERE id = ?
        """, (note.title, note.description, note_id))
        self.connection.commit()
    
    def delete_note(self, note_id):
        """
        Delete a note by ID.
        
        Args:
            note_id (int): The ID of the note to delete
        """
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM notes WHERE id = ?", (note_id,))
        self.connection.commit()
    
    def close(self):
        """Close the database connection."""
        self.connection.close()
