#!/usr/bin/env python3
"""Fix for GUI calculator buttons."""

import tkinter as tk
from tkinter import ttk
import sys
sys.path.insert(0, '.')

from calculator.parser import ExpressionParser
from calculator.history import HistoryManager

class SimpleCalculatorGUI:
    """Simplified calculator GUI for testing."""
    
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator - Fixed")
        
        self.parser = ExpressionParser()
        self.current_expression = ""
        
        # Create display
        self.display_var = tk.StringVar(value="0")
        display = ttk.Entry(
            master,
            textvariable=self.display_var,
            font=('Arial', 20),
            justify='right',
            state='readonly'
        )
        display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='ew')
        
        # Create buttons
        button_layout = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+'],
            ['C', '(', ')', '←']
        ]
        
        for row_idx, row in enumerate(button_layout):
            for col_idx, btn_text in enumerate(row):
                if btn_text == '=':
                    cmd = self.calculate
                elif btn_text == 'C':
                    cmd = self.clear
                elif btn_text == '←':
                    cmd = self.backspace
                else:
                    cmd = lambda x=btn_text: self.append_digit(x)
                
                btn = tk.Button(
                    master,
                    text=btn_text,
                    font=('Arial', 16),
                    width=5,
                    height=2,
                    command=cmd
                )
                btn.grid(row=row_idx+1, column=col_idx, padx=2, pady=2)
    
    def append_digit(self, digit):
        """Add digit to expression."""
        print(f"Appending: {digit}")
        if self.current_expression == "0":
            self.current_expression = digit
        else:
            self.current_expression += digit
        self.display_var.set(self.current_expression)
    
    def calculate(self):
        """Calculate the result."""
        print(f"Calculating: {self.current_expression}")
        try:
            result = self.parser.parse(self.current_expression)
            self.display_var.set(str(result))
            self.current_expression = str(result)
        except Exception as e:
            self.display_var.set("Error")
            print(f"Error: {e}")
    
    def clear(self):
        """Clear the display."""
        self.current_expression = "0"
        self.display_var.set("0")
    
    def backspace(self):
        """Remove last character."""
        if len(self.current_expression) > 1:
            self.current_expression = self.current_expression[:-1]
        else:
            self.current_expression = "0"
        self.display_var.set(self.current_expression)

if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleCalculatorGUI(root)
    print("Simple Calculator GUI started")
    print("Click buttons to test functionality")
    root.mainloop()