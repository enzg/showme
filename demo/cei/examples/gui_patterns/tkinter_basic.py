#!/usr/bin/env python3
"""Basic GUI calculator using Tkinter."""
import tkinter as tk

class Calculator:
    """Simple calculator GUI using Tkinter."""
    def __init__(self, root: tk.Tk) -> None:
        """Initialize the calculator."""
        self.root = root
        self.root.title("Simple Calculator")
        self.current = ""
        self.display_var = tk.StringVar(value="0")
        # Display
        display = tk.Entry(root, textvariable=self.display_var,
                          font=("Arial", 16), justify="right", state="readonly")
        display.grid(row=0, column=0, columnspan=4, sticky="ew", padx=5, pady=5)
        # Create buttons
        buttons = "789/456*123-0C=+"
        positions = [(r+1, c) for r in range(4) for c in range(4)]
        for btn_text, (row, col) in zip(buttons, positions):
            tk.Button(root, text=btn_text, font=("Arial", 14), width=5, height=2,
                     command=lambda t=btn_text: self._click(t)).grid(
                     row=row, column=col, padx=2, pady=2)
    
    def _click(self, value: str) -> None:
        """Handle button clicks."""
        if value == 'C':
            self.current = ""
            self.display_var.set("0")
        elif value == '=':
            try:
                result = eval(self.current)  # Simple eval for demo
                self.display_var.set(str(result))
                self.current = str(result)
            except:
                self.display_var.set("Error")
                self.current = ""
        else:
            self.current += value
            self.display_var.set(self.current)

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()