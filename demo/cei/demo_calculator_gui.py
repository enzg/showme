#!/usr/bin/env python3
"""
Demo script to showcase calculator functionality.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from calculator.parser import ExpressionParser
from calculator.history import HistoryManager

def demo_parser():
    """Demonstrate expression parser capabilities."""
    print("=== Expression Parser Demo ===\n")
    
    parser = ExpressionParser()
    
    test_expressions = [
        ("3+4", "Simple addition"),
        ("10-5", "Simple subtraction"),
        ("6*7", "Simple multiplication"),
        ("20/4", "Simple division"),
        ("3+4*2", "Order of operations"),
        ("(3+4)*2", "Parentheses"),
        ("((3+4)*2)+1", "Nested parentheses"),
        ("100/(4*5)+3*7", "Complex expression"),
    ]
    
    for expr, description in test_expressions:
        try:
            result = parser.parse(expr)
            print(f"{description:25} {expr:20} = {result:.10g}")
        except Exception as e:
            print(f"{description:25} {expr:20} ERROR: {e}")
    
    print("\n=== Error Handling Demo ===\n")
    
    error_expressions = [
        ("10/0", "Division by zero"),
        ("3++4", "Invalid syntax"),
        ("(3+4", "Mismatched parentheses"),
        ("", "Empty expression"),
    ]
    
    for expr, description in error_expressions:
        try:
            result = parser.parse(expr)
            print(f"{description:25} {expr:20} = {result}")
        except Exception as e:
            print(f"{description:25} {expr:20} ERROR: {type(e).__name__}: {e}")

def demo_history():
    """Demonstrate history manager capabilities."""
    print("\n\n=== History Manager Demo ===\n")
    
    history = HistoryManager(max_entries=5)
    
    # Add some calculations
    calculations = [
        ("3+4", 7),
        ("10*5", 50),
        ("100/4", 25),
        ("2+2", 4),
        ("15-8", 7),
        ("9*9", 81),  # This will push out the oldest entry
    ]
    
    print("Adding calculations to history...")
    for expr, result in calculations:
        history.add_entry(expr, result)
        print(f"  Added: {expr} = {result}")
    
    print(f"\nHistory size: {history.size()} (max: 5)")
    print("\nFormatted history display:")
    print(history.format_history_display())
    
    print("\nSearching for calculations with '+':")
    results = history.search("+")
    for entry in results:
        print(f"  Found: {entry.format_display()}")

def main():
    """Run the demo."""
    print("Calculator Implementation Demo\n")
    print("This calculator features:")
    print("- Secure expression parsing (no eval!)")
    print("- PEMDAS order of operations")
    print("- Calculation history tracking")
    print("- Both CLI and GUI interfaces\n")
    
    demo_parser()
    demo_history()
    
    print("\n\nTo run the calculator:")
    print("  GUI mode: python -m calculator --gui")
    print("  CLI mode: python -m calculator --cli")

if __name__ == "__main__":
    main()