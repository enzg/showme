#!/usr/bin/env python3
"""Manual test for history manager."""

import sys
sys.path.insert(0, '.')

from calculator.history import HistoryManager
import tempfile
import os

def test_history():
    """Test the history manager functionality."""
    print("Testing History Manager:")
    print("-" * 50)
    
    # Test 1: Basic operations
    history = HistoryManager(max_entries=3)
    
    # Add entries
    history.add_entry("2+2", 4)
    history.add_entry("5*5", 25)
    history.add_entry("10/2", 5)
    
    # Check size
    assert len(history._history) == 3
    print("✓ Added 3 entries successfully")
    
    # Add one more (should remove oldest)
    history.add_entry("7+3", 10)
    assert len(history._history) == 3
    assert history._history[0].expression == "5*5"  # Oldest entry was removed
    print("✓ Max entries limit working correctly")
    
    # Test 2: Get history
    recent = history.get_history(2)
    assert len(recent) == 2
    assert recent[1].expression == "7+3"  # Most recent last
    print("✓ Get history returns correct entries")
    
    # Test 3: Search
    results = history.search("5")
    assert len(results) == 2  # "5*5" and "10/2=5"
    print("✓ Search functionality working")
    
    # Test 4: Format display
    display = history.format_history_display()
    assert "Calculation History:" in display
    assert "7+3 = 10" in display
    print("✓ Format display working")
    
    # Test 5: Clear history
    history.clear_history()
    assert len(history._history) == 0
    print("✓ Clear history working")
    
    # Test 6: Save and load
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        temp_file = f.name
    
    try:
        # Add some entries
        history.add_entry("1+1", 2)
        history.add_entry("2+2", 4)
        
        # Save
        history.save_to_file(temp_file)
        print("✓ Save to file working")
        
        # Create new instance and load
        new_history = HistoryManager()
        new_history.load_from_file(temp_file)
        
        assert len(new_history._history) == 2
        assert new_history._history[0].expression == "1+1"
        print("✓ Load from file working")
        
    finally:
        os.unlink(temp_file)
    
    # Test 7: Empty history handling
    empty_history = HistoryManager()
    assert empty_history.get_history() == []
    assert empty_history.search("test") == []
    assert "No calculation history" in empty_history.format_history_display()
    print("✓ Empty history handling working")
    
    print("\n" + "=" * 50)
    print("All history tests passed!")
    return True

if __name__ == "__main__":
    success = test_history()
    sys.exit(0 if success else 1)