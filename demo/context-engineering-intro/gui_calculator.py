#!/usr/bin/env python3
"""GUI Calculator using Tkinter."""

import tkinter as tk
from tkinter import font
from typing import Optional
import core


class CalculatorGUI:
    """GUI Calculator application."""
    
    def __init__(self, master: tk.Tk) -> None:
        """Initialize the calculator GUI.
        
        Args:
            master: The root Tkinter window.
        """
        self.master = master
        self.master.title("Calculator")
        self.master.geometry("400x600")
        self.master.resizable(False, False)
        
        # Calculator state
        self.current_number: str = ""
        self.previous_number: Optional[float] = None
        self.operator: Optional[str] = None
        self.should_reset_display: bool = False
        self.history: list[str] = []
        
        # Create GUI components
        self._create_display()
        self._create_history()
        self._create_buttons()
        
    def _create_display(self) -> None:
        """Create the calculator display."""
        # Main display frame
        display_frame = tk.Frame(self.master, bg="lightgray")
        display_frame.pack(fill=tk.X, padx=10, pady=10)
        
        # Display entry
        self.display = tk.Entry(
            display_frame,
            font=font.Font(size=24),
            justify=tk.RIGHT,
            bd=5,
            relief=tk.SUNKEN
        )
        self.display.pack(fill=tk.X, padx=5, pady=5)
        self.display.insert(0, "0")
        
    def _create_history(self) -> None:
        """Create the history display."""
        history_frame = tk.Frame(self.master)
        history_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # History label
        tk.Label(history_frame, text="History:", font=font.Font(size=12)).pack(anchor=tk.W)
        
        # History listbox with scrollbar
        scrollbar = tk.Scrollbar(history_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.history_listbox = tk.Listbox(
            history_frame,
            yscrollcommand=scrollbar.set,
            height=5,
            font=font.Font(size=10)
        )
        self.history_listbox.pack(fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.history_listbox.yview)
        
    def _create_buttons(self) -> None:
        """Create calculator buttons."""
        button_frame = tk.Frame(self.master)
        button_frame.pack(padx=10, pady=10)
        
        # Button configuration
        button_config = {
            'width': 5,
            'height': 2,
            'font': font.Font(size=16),
            'bd': 3,
            'relief': tk.RAISED
        }
        
        # Create Clear button
        tk.Button(
            button_frame,
            text="C",
            command=self.clear,
            bg="lightcoral",
            **button_config
        ).grid(row=0, column=0, columnspan=2, sticky="ew", padx=2, pady=2)
        
        # Create operator buttons
        operators = [
            ('/', 0, 2),
            ('*', 0, 3),
            ('-', 1, 3),
            ('+', 2, 3),
        ]
        
        for op, row, col in operators:
            tk.Button(
                button_frame,
                text=op,
                command=lambda o=op: self.operator_click(o),
                bg="lightblue",
                **button_config
            ).grid(row=row, column=col, padx=2, pady=2)
        
        # Number button layout
        button_layout = [
            ['7', '8', '9'],
            ['4', '5', '6'],
            ['1', '2', '3'],
            ['0', '.', '=']
        ]
        
        for row_idx, row in enumerate(button_layout, start=1):
            for col_idx, btn_text in enumerate(row):
                if btn_text == '=':
                    btn = tk.Button(
                        button_frame,
                        text=btn_text,
                        command=self.equals,
                        bg="lightgreen",
                        **button_config
                    )
                elif btn_text == '.':
                    btn = tk.Button(
                        button_frame,
                        text=btn_text,
                        command=lambda: self.number_click('.'),
                        **button_config
                    )
                else:
                    btn = tk.Button(
                        button_frame,
                        text=btn_text,
                        command=lambda n=btn_text: self.number_click(n),
                        **button_config
                    )
                btn.grid(row=row_idx, column=col_idx, padx=2, pady=2)
        
    def number_click(self, number: str) -> None:
        """Handle number button clicks.
        
        Args:
            number: The number or decimal point clicked.
        """
        if self.should_reset_display:
            self.current_number = ""
            self.should_reset_display = False
            
        # Handle decimal point
        if number == '.' and '.' in self.current_number:
            return
            
        self.current_number += number
        self.update_display(self.current_number or "0")
        
    def operator_click(self, operator: str) -> None:
        """Handle operator button clicks.
        
        Args:
            operator: The operator clicked (+, -, *, /).
        """
        if self.current_number:
            if self.previous_number is not None and self.operator:
                self.equals()
            self.previous_number = float(self.current_number)
            self.operator = operator
            self.current_number = ""
            self.should_reset_display = True
            
    def equals(self) -> None:
        """Calculate and display the result."""
        if (self.previous_number is not None and 
            self.operator and 
            self.current_number):
            try:
                current = float(self.current_number)
                success, result = core.calculate(
                    self.previous_number,
                    current,
                    self.operator
                )
                
                if success:
                    # Format result to avoid floating point display issues
                    if isinstance(result, float) and result.is_integer():
                        result_str = str(int(result))
                    else:
                        result_str = f"{result:.10g}"  # Remove trailing zeros
                    
                    # Add to history
                    history_entry = f"{self.previous_number} {self.operator} {current} = {result_str}"
                    self.history.append(history_entry)
                    self.history_listbox.insert(tk.END, history_entry)
                    self.history_listbox.see(tk.END)
                    
                    # Update display
                    self.update_display(result_str)
                    self.current_number = result_str
                    self.previous_number = None
                    self.operator = None
                    self.should_reset_display = True
                else:
                    self.update_display("Error: " + str(result))
                    self.clear()
            except ValueError:
                self.update_display("Error: Invalid input")
                self.clear()
                
    def clear(self) -> None:
        """Clear the calculator."""
        self.current_number = ""
        self.previous_number = None
        self.operator = None
        self.should_reset_display = False
        self.update_display("0")
        
    def update_display(self, value: str) -> None:
        """Update the display with a new value.
        
        Args:
            value: The value to display.
        """
        self.display.delete(0, tk.END)
        self.display.insert(0, value)


def main() -> None:
    """Run the calculator application."""
    root = tk.Tk()
    app = CalculatorGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()