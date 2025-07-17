#!/usr/bin/env python3
"""Interactive test for GUI calculator."""

import tkinter as tk
import sys
sys.path.insert(0, '.')

from calculator.gui import CalculatorGUI

def test_gui_with_logging():
    """Test GUI with debug logging."""
    
    # Create root window
    root = tk.Tk()
    
    # Create calculator
    calc = CalculatorGUI(root)
    
    # Override _append_to_expression to add logging
    original_append = calc._append_to_expression
    def logged_append(value):
        print(f"Button pressed: {value}")
        print(f"Before - Expression: '{calc.current_expression}'")
        original_append(value)
        print(f"After - Expression: '{calc.current_expression}'")
        print(f"Display shows: '{calc.expression_var.get()}'")
        print("-" * 40)
    
    calc._append_to_expression = logged_append
    
    # Override _calculate to add logging
    original_calculate = calc._calculate
    def logged_calculate():
        print("Calculate button pressed!")
        print(f"Expression to calculate: '{calc.current_expression}'")
        original_calculate()
        print(f"Result display: '{calc.result_var.get()}'")
        print("=" * 40)
    
    calc._calculate = logged_calculate
    
    print("GUI Calculator Test Started")
    print("Click buttons and watch the console for debug output")
    print("=" * 40)
    
    # Test programmatically
    print("\nProgrammatic test - simulating button clicks:")
    print("Clicking: 2")
    calc._append_to_expression('2')
    
    print("Clicking: +")
    calc._append_to_expression('+')
    
    print("Clicking: 3")
    calc._append_to_expression('3')
    
    print("Clicking: =")
    calc._calculate()
    
    root.mainloop()

if __name__ == "__main__":
    test_gui_with_logging()