"""
Unit tests for the Notes CLI application.
"""

import os
import pytest
import sqlite3
from notes import Note, NotesDB


@pytest.fixture
def test_db():
    """Create a test database for each test."""
    # Use a test database file
    test_db_file = "test_notes.db"
    
    # Remove if exists
    if os.path.exists(test_db_file):
        os.remove(test_db_file)
    
    # Temporarily override the DB_FILE
    original_db_file = NotesDB.DB_FILE
    NotesDB.DB_FILE = test_db_file
    
    db = NotesDB()
    
    yield db
    
    # Cleanup
    db.close()
    if os.path.exists(test_db_file):
        os.remove(test_db_file)
    
    # Restore original DB_FILE
    NotesDB.DB_FILE = original_db_file


class TestNote:
    """Test cases for the Note class."""
    
    def test_note_creation(self):
        """Test creating a note."""
        note = Note(title="Test Title", description="Test Description")
        assert note.title == "Test Title"
        assert note.description == "Test Description"
        assert note.created_at is not None
    
    def test_note_to_dict(self):
        """Test converting a note to dictionary."""
        note = Note(title="Test Title", description="Test Description")
        note_dict = note.to_dict()
        assert note_dict["title"] == "Test Title"
        assert note_dict["description"] == "Test Description"
        assert "created_at" in note_dict


class TestNotesDB:
    """Test cases for the NotesDB class."""
    
    def test_database_creation(self, test_db):
        """Test that database is created successfully."""
        assert os.path.exists("test_notes.db")
    
    def test_add_note(self, test_db):
        """Test adding a note to the database."""
        note = Note(title="Test Note", description="This is a test note")
        note_id = test_db.add_note(note)
        assert note_id == 1
    
    def test_get_all_notes(self, test_db):
        """Test retrieving all notes."""
        note1 = Note(title="Note 1", description="Description 1")
        note2 = Note(title="Note 2", description="Description 2")
        
        test_db.add_note(note1)
        test_db.add_note(note2)
        
        notes = test_db.get_all_notes()
        assert len(notes) == 2
        assert notes[0]["title"] == "Note 1"
        assert notes[1]["title"] == "Note 2"
    
    def test_get_note_by_id(self, test_db):
        """Test retrieving a specific note by ID."""
        note = Note(title="Test Note", description="Test Description")
        note_id = test_db.add_note(note)
        
        retrieved_note = test_db.get_note(note_id)
        assert retrieved_note is not None
        assert retrieved_note["title"] == "Test Note"
        assert retrieved_note["description"] == "Test Description"
    
    def test_get_nonexistent_note(self, test_db):
        """Test retrieving a note that doesn't exist."""
        note = test_db.get_note(999)
        assert note is None
    
    def test_update_note(self, test_db):
        """Test updating a note."""
        note = Note(title="Original Title", description="Original Description")
        note_id = test_db.add_note(note)
        
        updated_note = Note(title="Updated Title", description="Updated Description")
        test_db.update_note(note_id, updated_note)
        
        retrieved_note = test_db.get_note(note_id)
        assert retrieved_note["title"] == "Updated Title"
        assert retrieved_note["description"] == "Updated Description"
    
    def test_delete_note(self, test_db):
        """Test deleting a note."""
        note = Note(title="Test Note", description="Test Description")
        note_id = test_db.add_note(note)
        
        test_db.delete_note(note_id)
        
        retrieved_note = test_db.get_note(note_id)
        assert retrieved_note is None
    
    def test_empty_database(self, test_db):
        """Test retrieving notes from an empty database."""
        notes = test_db.get_all_notes()
        assert len(notes) == 0
