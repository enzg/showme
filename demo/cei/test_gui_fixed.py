#!/usr/bin/env python3
"""Test the fixed GUI calculator."""

import sys
sys.path.insert(0, '.')

print("Starting GUI Calculator with fixes...")
print("- Display boxes now use tk.Entry for better compatibility")
print("- Button text changed to black for better visibility")
print("- Force update added to ensure display refreshes")
print("=" * 50)

from calculator.gui import CalculatorGUI
import tkinter as tk

root = tk.Tk()
calc = CalculatorGUI(root)

# Test programmatically
print("\nProgrammatic test:")
print("Setting expression to '123'...")
calc.expression_var.set("123")
calc.expression_display.update()
print(f"Expression display shows: '{calc.expression_var.get()}'")

print("\nClicking buttons: 4 + 5 =")
calc._append_to_expression('4')
calc._append_to_expression('+')
calc._append_to_expression('5')
calc._calculate()

print("\nGUI Calculator is running. Try clicking buttons!")
root.mainloop()