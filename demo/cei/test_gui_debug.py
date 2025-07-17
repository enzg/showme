#!/usr/bin/env python3
"""Debug script for GUI calculator buttons."""

import tkinter as tk
from tkinter import ttk
import sys
sys.path.insert(0, '.')

def test_basic_gui():
    """Test basic GUI functionality."""
    root = tk.Tk()
    root.title("GUI Debug Test")
    
    # Test variable
    test_var = tk.StringVar(value="Click a button")
    
    # Display
    display = ttk.Entry(root, textvariable=test_var, font=('Arial', 16), state='readonly')
    display.pack(padx=10, pady=10)
    
    # Frame for buttons
    button_frame = ttk.Frame(root)
    button_frame.pack(padx=10, pady=10)
    
    # Test buttons
    def button_click(value):
        current = test_var.get()
        if current == "Click a button":
            test_var.set(value)
        else:
            test_var.set(current + value)
        print(f"Button clicked: {value}, Display: {test_var.get()}")
    
    # Create test buttons
    buttons = ['1', '2', '3', '+', '4', '5', '6', '-']
    for i, btn_text in enumerate(buttons):
        row = i // 4
        col = i % 4
        btn = ttk.Button(
            button_frame,
            text=btn_text,
            command=lambda t=btn_text: button_click(t)
        )
        btn.grid(row=row, column=col, padx=2, pady=2)
    
    # Clear button
    def clear_display():
        test_var.set("Click a button")
        print("Display cleared")
    
    clear_btn = ttk.Button(button_frame, text="Clear", command=clear_display)
    clear_btn.grid(row=2, column=0, columnspan=4, pady=5)
    
    print("GUI Debug Test started. Click buttons to test.")
    root.mainloop()

def test_calculator_gui():
    """Test the actual calculator GUI."""
    try:
        from calculator.gui import CalculatorGUI
        root = tk.Tk()
        
        # Add debug print to button creation
        print("Creating Calculator GUI...")
        calc = CalculatorGUI(root)
        
        # Test if components exist
        print(f"Expression var initialized: {hasattr(calc, 'expression_var')}")
        print(f"Current expression: '{calc.current_expression}'")
        print(f"Parser initialized: {hasattr(calc, 'parser')}")
        
        # Try to manually trigger a button click
        print("\nManually adding '5' to expression...")
        calc._append_to_expression('5')
        print(f"Expression after adding '5': '{calc.current_expression}'")
        print(f"Display value: '{calc.expression_var.get()}'")
        
        root.mainloop()
    except Exception as e:
        print(f"Error loading calculator GUI: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    print("1. Testing basic GUI...")
    # Uncomment to test basic GUI
    # test_basic_gui()
    
    print("\n2. Testing Calculator GUI...")
    test_calculator_gui()