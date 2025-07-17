#!/usr/bin/env python3
"""Debug display issue in calculator GUI."""

import tkinter as tk
import sys
sys.path.insert(0, '.')

# Test 1: Simple StringVar and Entry test
def test_simple_display():
    print("Test 1: Simple StringVar and Entry")
    root = tk.Tk()
    root.title("Display Test")
    
    # Create StringVar and Entry
    var = tk.StringVar(value="Initial")
    entry = tk.Entry(root, textvariable=var, font=('Arial', 16), state='readonly')
    entry.pack(padx=20, pady=20)
    
    # Test buttons
    def update_text(text):
        current = var.get()
        var.set(current + text)
        print(f"StringVar value: '{var.get()}'")
        entry.update_idletasks()  # Force update
    
    btn_frame = tk.Frame(root)
    btn_frame.pack()
    
    for i in range(1, 4):
        btn = tk.Button(btn_frame, text=str(i), command=lambda x=str(i): update_text(x))
        btn.pack(side='left', padx=5)
    
    print("Click buttons to test...")
    root.mainloop()

# Test 2: Check the actual calculator display
def test_calculator_display():
    print("\nTest 2: Calculator Display Issue")
    from calculator.gui import CalculatorGUI
    
    root = tk.Tk()
    calc = CalculatorGUI(root)
    
    # Override methods to add detailed logging
    original_append = calc._append_to_expression
    def debug_append(value):
        print(f"\n=== BEFORE APPEND ===")
        print(f"Current expression: '{calc.current_expression}'")
        print(f"Expression var: '{calc.expression_var.get()}'")
        print(f"Expression display state: {calc.expression_display['state']}")
        
        original_append(value)
        
        print(f"\n=== AFTER APPEND ===")
        print(f"Current expression: '{calc.current_expression}'")
        print(f"Expression var: '{calc.expression_var.get()}'")
        print(f"Display widget exists: {calc.expression_display.winfo_exists()}")
        print(f"Display widget visible: {calc.expression_display.winfo_viewable()}")
        
        # Try different update methods
        calc.expression_display.update()
        calc.expression_display.update_idletasks()
        calc.master.update()
        
        # Check if the Entry is actually showing the value
        try:
            actual_display = calc.expression_display.get()
            print(f"Actual Entry content: '{actual_display}'")
        except:
            print("Could not get Entry content")
    
    calc._append_to_expression = debug_append
    
    # Test programmatically
    print("\nClicking '5' programmatically...")
    calc._append_to_expression('5')
    
    root.mainloop()

if __name__ == "__main__":
    print("Which test to run?")
    print("1. Simple display test")
    print("2. Calculator display debug")
    choice = input("Enter 1 or 2 (default: 2): ").strip() or "2"
    
    if choice == "1":
        test_simple_display()
    else:
        test_calculator_display()