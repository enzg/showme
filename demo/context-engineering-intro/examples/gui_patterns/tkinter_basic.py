#!/usr/bin/env python3
"""Basic Tkinter button layout example for calculator."""

import tkinter as tk
from typing import Callable


def create_button(parent: tk.Widget, text: str, row: int, col: int, 
                 command: Callable) -> tk.Button:
    """Create and place a button in the grid.
    
    Args:
        parent: Parent widget.
        text: Button text.
        row: Grid row position.
        col: Grid column position.
        command: Function to call on click.
        
    Returns:
        Created button widget.
    """
    button = tk.Button(parent, text=text, width=5, height=2, command=command)
    button.grid(row=row, column=col, padx=2, pady=2)
    return button


def on_button_click(value: str) -> None:
    """Handle button click events.
    
    Args:
        value: The button value that was clicked.
    """
    print(f"Button clicked: {value}")


def main() -> None:
    """Create main calculator GUI window."""
    root = tk.Tk()
    root.title("Calculator Button Layout")
    root.geometry("250x300")
    
    # Create number buttons (0-9) in calculator layout
    button_layout = [
        ['7', '8', '9'],
        ['4', '5', '6'],
        ['1', '2', '3'],
        ['0', '.', '=']
    ]
    
    for row_idx, row in enumerate(button_layout):
        for col_idx, btn_text in enumerate(row):
            create_button(root, btn_text, row_idx, col_idx,
                         lambda v=btn_text: on_button_click(v))
    
    root.mainloop()


if __name__ == "__main__":
    main()