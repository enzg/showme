"""
Tests for the history manager module.
"""
import pytest
import json
import tempfile
import os
from datetime import datetime, timedelta
from calculator.history import HistoryEntry, HistoryManager


class TestHistoryEntry:
    """Test cases for HistoryEntry class."""
    
    def test_create_entry(self):
        """Test creating a history entry."""
        entry = HistoryEntry("3+4", 7.0)
        assert entry.expression == "3+4"
        assert entry.result == 7.0
        assert isinstance(entry.timestamp, datetime)
    
    def test_create_entry_with_timestamp(self):
        """Test creating entry with specific timestamp."""
        timestamp = datetime(2024, 1, 1, 12, 0, 0)
        entry = HistoryEntry("5*2", 10.0, timestamp)
        assert entry.timestamp == timestamp
    
    def test_format_display(self):
        """Test formatting entry for display."""
        entry = HistoryEntry("3+4", 7.0)
        assert entry.format_display() == "3+4 = 7"
        
        # Test decimal formatting
        entry2 = HistoryEntry("10/3", 3.333333333)
        assert entry2.format_display() == "10/3 = 3.333333333"
    
    def test_to_dict(self):
        """Test converting entry to dictionary."""
        timestamp = datetime(2024, 1, 1, 12, 0, 0)
        entry = HistoryEntry("3+4", 7.0, timestamp)
        data = entry.to_dict()
        
        assert data['expression'] == "3+4"
        assert data['result'] == 7.0
        assert data['timestamp'] == timestamp.isoformat()
    
    def test_from_dict(self):
        """Test creating entry from dictionary."""
        data = {
            'expression': "3+4",
            'result': 7.0,
            'timestamp': "2024-01-01T12:00:00"
        }
        entry = HistoryEntry.from_dict(data)
        
        assert entry.expression == "3+4"
        assert entry.result == 7.0
        assert entry.timestamp == datetime(2024, 1, 1, 12, 0, 0)


class TestHistoryManager:
    """Test cases for HistoryManager class."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.manager = HistoryManager(max_entries=10)
    
    def test_add_entry(self):
        """Test adding entries to history."""
        self.manager.add_entry("3+4", 7.0)
        assert self.manager.size() == 1
        
        self.manager.add_entry("5*2", 10.0)
        assert self.manager.size() == 2
    
    def test_get_history(self):
        """Test retrieving history."""
        # Add some entries
        self.manager.add_entry("3+4", 7.0)
        self.manager.add_entry("5*2", 10.0)
        self.manager.add_entry("10/2", 5.0)
        
        # Get all history
        history = self.manager.get_history()
        assert len(history) == 3
        assert history[0].expression == "3+4"
        assert history[2].expression == "10/2"
    
    def test_get_history_with_limit(self):
        """Test retrieving limited history."""
        # Add 5 entries
        for i in range(5):
            self.manager.add_entry(f"{i}+1", i+1)
        
        # Get last 3
        history = self.manager.get_history(limit=3)
        assert len(history) == 3
        assert history[0].expression == "2+1"
        assert history[2].expression == "4+1"
    
    def test_get_recent(self):
        """Test getting recent entries."""
        # Add 5 entries
        for i in range(5):
            self.manager.add_entry(f"{i}+1", i+1)
        
        recent = self.manager.get_recent(count=2)
        assert len(recent) == 2
        assert recent[0].expression == "3+1"
        assert recent[1].expression == "4+1"
    
    def test_max_entries_limit(self):
        """Test that max_entries limit is enforced."""
        manager = HistoryManager(max_entries=3)
        
        # Add 5 entries
        for i in range(5):
            manager.add_entry(f"{i}+1", i+1)
        
        # Should only keep last 3
        assert manager.size() == 3
        history = manager.get_history()
        assert history[0].expression == "2+1"
        assert history[2].expression == "4+1"
    
    def test_clear_history(self):
        """Test clearing history."""
        self.manager.add_entry("3+4", 7.0)
        self.manager.add_entry("5*2", 10.0)
        assert self.manager.size() == 2
        
        self.manager.clear_history()
        assert self.manager.size() == 0
        assert self.manager.is_empty()
    
    def test_is_empty(self):
        """Test checking if history is empty."""
        assert self.manager.is_empty()
        
        self.manager.add_entry("3+4", 7.0)
        assert not self.manager.is_empty()
    
    def test_search(self):
        """Test searching history."""
        self.manager.add_entry("3+4", 7.0)
        self.manager.add_entry("5*2", 10.0)
        self.manager.add_entry("10/2", 5.0)
        self.manager.add_entry("2+5", 7.0)
        
        # Search by expression
        results = self.manager.search("+")
        assert len(results) == 2
        assert all("+" in r.expression for r in results)
        
        # Search by result
        results = self.manager.search("7")
        assert len(results) == 2
        assert all(r.result == 7.0 for r in results)
    
    def test_get_by_index(self):
        """Test getting entry by index."""
        self.manager.add_entry("3+4", 7.0)
        self.manager.add_entry("5*2", 10.0)
        
        # Positive index
        entry = self.manager.get_by_index(0)
        assert entry.expression == "3+4"
        
        # Negative index
        entry = self.manager.get_by_index(-1)
        assert entry.expression == "5*2"
        
        # Out of range
        entry = self.manager.get_by_index(10)
        assert entry is None
    
    def test_save_and_load_file(self):
        """Test saving and loading history from file."""
        # Add some entries
        self.manager.add_entry("3+4", 7.0)
        self.manager.add_entry("5*2", 10.0)
        
        # Save to temporary file
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json') as f:
            filepath = f.name
        
        try:
            self.manager.save_to_file(filepath)
            
            # Create new manager and load
            new_manager = HistoryManager()
            new_manager.load_from_file(filepath)
            
            # Verify loaded data
            assert new_manager.size() == 2
            assert new_manager.max_entries == 10
            history = new_manager.get_history()
            assert history[0].expression == "3+4"
            assert history[1].expression == "5*2"
        finally:
            # Clean up
            os.unlink(filepath)
    
    def test_load_nonexistent_file(self):
        """Test loading from non-existent file."""
        with pytest.raises(FileNotFoundError):
            self.manager.load_from_file("nonexistent.json")
    
    def test_format_history_display(self):
        """Test formatting history for display."""
        # Empty history
        display = self.manager.format_history_display()
        assert display == "No calculation history"
        
        # Add entries
        self.manager.add_entry("3+4", 7.0)
        self.manager.add_entry("5*2", 10.0)
        
        display = self.manager.format_history_display()
        assert "Calculation History:" in display
        assert "3+4 = 7" in display
        assert "5*2 = 10" in display
        assert "[" in display  # Time format
        
    def test_format_history_display_with_limit(self):
        """Test formatting limited history display."""
        # Add 5 entries
        for i in range(5):
            self.manager.add_entry(f"{i}+1", i+1)
        
        display = self.manager.format_history_display(limit=2)
        lines = display.split('\n')
        # Header + separator + 2 entries
        assert len(lines) == 4
        assert "3+1 = 4" in display
        assert "4+1 = 5" in display