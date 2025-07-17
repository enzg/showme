#!/usr/bin/env python3
"""
Simple test to verify GUI calculator can be launched.
"""

import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    import tkinter
    from calculator.gui import CalculatorGUI
    print("✓ Tkinter imported successfully")
    print("✓ CalculatorGUI imported successfully")
    
    # Test parser and history imports
    from calculator.parser import ExpressionParser
    from calculator.history import HistoryManager
    print("✓ Parser imported successfully")
    print("✓ History manager imported successfully")
    
    # Test basic expression parsing
    parser = ExpressionParser()
    result = parser.parse("3+4*2")
    assert result == 11, f"Expected 11, got {result}"
    print("✓ Basic expression parsing works: 3+4*2 = 11")
    
    result = parser.parse("(3+4)*2")
    assert result == 14, f"Expected 14, got {result}"
    print("✓ Parentheses parsing works: (3+4)*2 = 14")
    
    # Test history manager
    history = HistoryManager()
    history.add_entry("3+4", 7)
    assert history.size() == 1
    print("✓ History manager works")
    
    print("\nAll imports and basic functionality verified!")
    print("You can now run: python -m calculator --gui")
    
except ImportError as e:
    print(f"✗ Import error: {e}")
    print("Make sure you're in the project directory")
except Exception as e:
    print(f"✗ Error: {e}")