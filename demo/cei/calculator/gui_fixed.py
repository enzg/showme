"""
Fixed GUI Calculator using Labels for display.
"""
import tkinter as tk
from tkinter import ttk, messagebox
from typing import Optional
from calculator.parser import ExpressionParser
from calculator.history import HistoryManager


class CalculatorGUI:
    """
    Fixed calculator GUI using Labels instead of Entry widgets for display.
    """
    
    def __init__(self, master: tk.Tk):
        self.master = master
        self.master.title("Calculator")
        self.master.resizable(False, False)
        
        # Initialize components
        self.parser = ExpressionParser()
        self.history_manager = HistoryManager(max_entries=50)
        
        # State variables
        self.current_expression = ""
        self.last_result = ""
        self.error_state = False
        
        # Create GUI components
        self._create_display_frame()
        self._create_button_frame()
        self._create_history_frame()
        
        # Bind keyboard events
        self._bind_keyboard_events()
        
        # Configure main window grid
        self.master.columnconfigure(0, weight=1)
        self.master.columnconfigure(1, weight=0)
        
        # Focus on the window
        self.master.focus_set()
    
    def _create_display_frame(self):
        """Create the display area using Labels."""
        display_frame = tk.Frame(self.master, bg='white', relief='solid', bd=1)
        display_frame.grid(row=0, column=0, sticky="ew", padx=10, pady=10)
        
        # Expression display - using Label
        self.expression_var = tk.StringVar(value="")
        self.expression_display = tk.Label(
            display_frame,
            textvariable=self.expression_var,
            font=('Arial', 16),
            anchor='e',
            bg='white',
            fg='black',
            height=2,
            padx=10
        )
        self.expression_display.pack(fill='x', pady=(5, 0))
        
        # Separator
        separator = tk.Frame(display_frame, height=1, bg='#ddd')
        separator.pack(fill='x', padx=10)
        
        # Result display - using Label
        self.result_var = tk.StringVar(value="0")
        self.result_display = tk.Label(
            display_frame,
            textvariable=self.result_var,
            font=('Arial', 20, 'bold'),
            anchor='e',
            bg='white',
            fg='black',
            height=2,
            padx=10
        )
        self.result_display.pack(fill='x', pady=(0, 5))
    
    def _create_button_frame(self):
        """Create the calculator button grid."""
        button_frame = tk.Frame(self.master)
        button_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=(0, 10))
        
        # Button layout
        buttons = [
            # Row 0
            [('C', self._clear_display, '#f44336'), 
             ('CE', self._clear_entry, '#f44336'),
             ('(', lambda: self._append_to_expression('('), '#2196F3'),
             (')', lambda: self._append_to_expression(')'), '#2196F3')],
            # Row 1
            [('7', lambda: self._append_to_expression('7'), '#e0e0e0'),
             ('8', lambda: self._append_to_expression('8'), '#e0e0e0'),
             ('9', lambda: self._append_to_expression('9'), '#e0e0e0'),
             ('/', lambda: self._append_to_expression('/'), '#ff9500')],
            # Row 2
            [('4', lambda: self._append_to_expression('4'), '#e0e0e0'),
             ('5', lambda: self._append_to_expression('5'), '#e0e0e0'),
             ('6', lambda: self._append_to_expression('6'), '#e0e0e0'),
             ('*', lambda: self._append_to_expression('*'), '#ff9500')],
            # Row 3
            [('1', lambda: self._append_to_expression('1'), '#e0e0e0'),
             ('2', lambda: self._append_to_expression('2'), '#e0e0e0'),
             ('3', lambda: self._append_to_expression('3'), '#e0e0e0'),
             ('-', lambda: self._append_to_expression('-'), '#ff9500')],
            # Row 4
            [('0', lambda: self._append_to_expression('0'), '#e0e0e0'),
             ('.', lambda: self._append_to_expression('.'), '#e0e0e0'),
             ('=', self._calculate, '#4CAF50'),
             ('+', lambda: self._append_to_expression('+'), '#ff9500')]
        ]
        
        # Create buttons
        for row_idx, row in enumerate(buttons):
            for col_idx, (text, command, color) in enumerate(row):
                btn = tk.Button(
                    button_frame,
                    text=text,
                    command=command,
                    font=('Arial', 14, 'bold') if text in '+-*/=' else ('Arial', 14),
                    width=5,
                    height=2,
                    bg=color,
                    fg='white' if color != '#e0e0e0' else 'black',
                    activebackground=color,
                    relief='flat',
                    bd=1
                )
                btn.grid(row=row_idx, column=col_idx, padx=1, pady=1, sticky="nsew")
        
        # Configure grid weights
        for i in range(4):
            button_frame.columnconfigure(i, weight=1)
            button_frame.rowconfigure(i, weight=1)
        button_frame.rowconfigure(4, weight=1)
    
    def _create_history_frame(self):
        """Create the history panel."""
        self.history_frame = tk.LabelFrame(self.master, text="History", font=('Arial', 10, 'bold'))
        self.history_frame.grid(row=0, column=1, rowspan=2, sticky="nsew", padx=(0, 10), pady=10)
        
        # History listbox
        self.history_listbox = tk.Listbox(
            self.history_frame,
            font=('Arial', 10),
            width=30,
            height=15,
            selectmode=tk.SINGLE,
            bg='#f5f5f5'
        )
        self.history_listbox.pack(side='left', fill='both', expand=True, padx=5, pady=5)
        
        # Scrollbar
        scrollbar = tk.Scrollbar(self.history_frame, orient="vertical", 
                                command=self.history_listbox.yview)
        scrollbar.pack(side='right', fill='y')
        self.history_listbox.config(yscrollcommand=scrollbar.set)
        
        # Bind double-click to restore expression
        self.history_listbox.bind('<Double-Button-1>', self._restore_from_history)
        
        # Clear history button
        clear_btn = tk.Button(
            self.master,
            text="Clear History",
            command=self._clear_history,
            font=('Arial', 10),
            bg='#f44336',
            fg='white',
            relief='flat'
        )
        clear_btn.grid(row=2, column=1, padx=(0, 10), pady=(0, 10), sticky="ew")
    
    def _bind_keyboard_events(self):
        """Bind keyboard shortcuts."""
        # Number keys
        for i in range(10):
            self.master.bind(str(i), lambda e, n=str(i): self._append_to_expression(n))
        
        # Operators
        self.master.bind('+', lambda e: self._append_to_expression('+'))
        self.master.bind('-', lambda e: self._append_to_expression('-'))
        self.master.bind('*', lambda e: self._append_to_expression('*'))
        self.master.bind('/', lambda e: self._append_to_expression('/'))
        
        # Parentheses
        self.master.bind('(', lambda e: self._append_to_expression('('))
        self.master.bind(')', lambda e: self._append_to_expression(')'))
        
        # Decimal point
        self.master.bind('.', lambda e: self._append_to_expression('.'))
        
        # Special keys
        self.master.bind('<Return>', lambda e: self._calculate())
        self.master.bind('<KP_Enter>', lambda e: self._calculate())
        self.master.bind('=', lambda e: self._calculate())
        self.master.bind('<Escape>', lambda e: self._clear_display())
        self.master.bind('<BackSpace>', lambda e: self._backspace())
    
    def _append_to_expression(self, value: str):
        """Append a value to the current expression."""
        if self.error_state:
            self._clear_display()
        
        self.current_expression += value
        self.expression_var.set(self.current_expression)
        print(f"Expression updated: {self.current_expression}")  # Debug
    
    def _backspace(self):
        """Remove the last character from the expression."""
        if self.current_expression:
            self.current_expression = self.current_expression[:-1]
            self.expression_var.set(self.current_expression)
    
    def _clear_display(self):
        """Clear the entire display."""
        self.current_expression = ""
        self.expression_var.set("")
        self.result_var.set("0")
        self.error_state = False
    
    def _clear_entry(self):
        """Clear the current entry (CE functionality)."""
        self.current_expression = ""
        self.expression_var.set("")
        if not self.error_state:
            self.result_var.set(self.last_result if self.last_result else "0")
    
    def _calculate(self):
        """Calculate the result of the current expression."""
        if not self.current_expression:
            return
        
        try:
            result = self.parser.parse(self.current_expression)
            result_str = f"{result:.10g}"  # Remove trailing zeros
            
            self.result_var.set(result_str)
            self.last_result = result_str
            
            # Add to history
            self.history_manager.add_entry(self.current_expression, result)
            self._update_history_display()
            
            # Clear expression for next calculation
            self.current_expression = ""
            self.expression_var.set("")
            self.error_state = False
            
        except ZeroDivisionError:
            self.result_var.set("Error: Division by zero")
            self.error_state = True
        except Exception as e:
            self.result_var.set(f"Error: {str(e)}")
            self.error_state = True
    
    def _update_history_display(self):
        """Update the history listbox."""
        self.history_listbox.delete(0, tk.END)
        
        history = self.history_manager.get_history()
        for entry in reversed(history):  # Show most recent first
            display_text = f"{entry.format_display()}"
            self.history_listbox.insert(0, display_text)
    
    def _restore_from_history(self, event):
        """Restore an expression from history."""
        selection = self.history_listbox.curselection()
        if selection:
            index = selection[0]
            history = self.history_manager.get_history()
            entry_index = len(history) - 1 - index  # Reverse the index
            
            if 0 <= entry_index < len(history):
                entry = history[entry_index]
                self.current_expression = entry.expression
                self.expression_var.set(self.current_expression)
    
    def _clear_history(self):
        """Clear the calculation history."""
        self.history_manager.clear_history()
        self.history_listbox.delete(0, tk.END)
        print("History cleared")


def run_gui():
    """Run the calculator GUI."""
    root = tk.Tk()
    app = CalculatorGUI(root)
    print("Calculator GUI (Fixed Version) started")
    print("Using Labels instead of Entry widgets for display")
    root.mainloop()


if __name__ == "__main__":
    run_gui()