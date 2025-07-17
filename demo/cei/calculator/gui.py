"""
GUI Calculator using Tkinter.
Provides a graphical interface for the calculator with expression parsing.
"""
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from typing import Optional, Callable
from calculator.parser import ExpressionParser
from calculator.history import HistoryManager


class CalculatorGUI:
    """
    Main GUI calculator application.
    Features a display, number/operation buttons, and calculation history.
    """
    
    def __init__(self, master: tk.Tk):
        """
        Initialize the calculator GUI.
        
        Args:
            master: The root Tkinter window
        """
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
        
        # Configure styles
        self._configure_styles()
        
        # Create GUI components
        self._create_menu()
        self._create_display_frame()
        self._create_button_frame()
        self._create_history_frame()
        
        # Bind keyboard events
        self._bind_keyboard_events()
        
        # Configure main window grid
        self.master.columnconfigure(0, weight=1)
        self.master.columnconfigure(1, weight=0)
        self.master.rowconfigure(0, weight=1)
        self.master.rowconfigure(1, weight=1)
        
        # Focus on the window
        self.master.focus_set()
    
    def _configure_styles(self):
        """Configure GUI styles and colors."""
        self.style = ttk.Style()
        
        # Configure button styles
        self.style.configure('Number.TButton', font=('Arial', 14))
        self.style.configure('Operator.TButton', font=('Arial', 14, 'bold'))
        self.style.configure('Equals.TButton', font=('Arial', 14, 'bold'))
        self.style.configure('Clear.TButton', font=('Arial', 12))
        
        # Colors
        self.bg_color = '#f0f0f0'
        self.display_bg = '#ffffff'
        self.button_bg = '#e0e0e0'
        self.operator_bg = '#ff9500'
        self.equals_bg = '#4CAF50'
        self.clear_bg = '#f44336'
        
        self.master.configure(bg=self.bg_color)
    
    def _create_menu(self):
        """Create the menu bar."""
        menubar = tk.Menu(self.master)
        self.master.config(menu=menubar)
        
        # File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Clear History", command=self._clear_history)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.master.quit)
        
        # Edit menu
        edit_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Clear", command=self._clear_display, accelerator="Esc")
        edit_menu.add_command(label="Clear Entry", command=self._clear_entry, accelerator="CE")
        
        # View menu
        view_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="View", menu=view_menu)
        self.show_history = tk.BooleanVar(value=True)
        view_menu.add_checkbutton(label="Show History", variable=self.show_history, 
                                  command=self._toggle_history)
        
        # Help menu
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=self._show_about)
        help_menu.add_command(label="Keyboard Shortcuts", command=self._show_shortcuts)
    
    def _create_display_frame(self):
        """Create the display area for expressions and results."""
        display_frame = ttk.Frame(self.master, padding="10")
        display_frame.grid(row=0, column=0, sticky="ew")
        
        # Expression display - using Label for better compatibility
        self.expression_var = tk.StringVar(value="")
        self.expression_frame = tk.Frame(display_frame, bg='white', relief='solid', bd=1)
        self.expression_frame.grid(row=0, column=0, sticky="ew", pady=(0, 5))
        self.expression_display = tk.Label(
            self.expression_frame,
            textvariable=self.expression_var,
            font=('Arial', 16),
            anchor='e',
            bg='white',
            fg='black',
            padx=10,
            pady=5
        )
        self.expression_display.pack(fill='x')
        
        # Result display - using Label for better compatibility
        self.result_frame = tk.Frame(display_frame, bg='#f5f5f5', relief='solid', bd=1)
        self.result_frame.grid(row=1, column=0, sticky="ew")
        self.result_var = tk.StringVar(value="0")
        self.result_display = tk.Label(
            self.result_frame,
            textvariable=self.result_var,
            font=('Arial', 20, 'bold'),
            anchor='e',
            bg='#f5f5f5',
            fg='black',
            padx=10,
            pady=8
        )
        self.result_display.pack(fill='x')
        
        # Configure grid weights
        display_frame.columnconfigure(0, weight=1)
    
    def _create_button_frame(self):
        """Create the calculator button grid."""
        button_frame = ttk.Frame(self.master, padding="10")
        button_frame.grid(row=1, column=0, sticky="nsew")
        
        # Button layout
        buttons = [
            # Row 0
            [('C', self._clear_display, 'Clear.TButton'), 
             ('CE', self._clear_entry, 'Clear.TButton'),
             ('(', lambda: self._append_to_expression('('), 'Operator.TButton'),
             (')', lambda: self._append_to_expression(')'), 'Operator.TButton')],
            # Row 1
            [('7', lambda: self._append_to_expression('7'), 'Number.TButton'),
             ('8', lambda: self._append_to_expression('8'), 'Number.TButton'),
             ('9', lambda: self._append_to_expression('9'), 'Number.TButton'),
             ('/', lambda: self._append_to_expression('/'), 'Operator.TButton')],
            # Row 2
            [('4', lambda: self._append_to_expression('4'), 'Number.TButton'),
             ('5', lambda: self._append_to_expression('5'), 'Number.TButton'),
             ('6', lambda: self._append_to_expression('6'), 'Number.TButton'),
             ('*', lambda: self._append_to_expression('*'), 'Operator.TButton')],
            # Row 3
            [('1', lambda: self._append_to_expression('1'), 'Number.TButton'),
             ('2', lambda: self._append_to_expression('2'), 'Number.TButton'),
             ('3', lambda: self._append_to_expression('3'), 'Number.TButton'),
             ('-', lambda: self._append_to_expression('-'), 'Operator.TButton')],
            # Row 4
            [('0', lambda: self._append_to_expression('0'), 'Number.TButton'),
             ('.', lambda: self._append_to_expression('.'), 'Number.TButton'),
             ('=', self._calculate, 'Equals.TButton'),
             ('+', lambda: self._append_to_expression('+'), 'Operator.TButton')]
        ]
        
        # Create buttons
        for row_idx, row in enumerate(buttons):
            for col_idx, (text, command, style) in enumerate(row):
                # Use tk.Button instead of ttk.Button for better compatibility
                if style == 'Number.TButton':
                    btn = tk.Button(
                        button_frame,
                        text=text,
                        command=command,
                        font=('Arial', 14),
                        width=5,
                        height=2,
                        bg='#e0e0e0'
                    )
                elif style == 'Operator.TButton':
                    btn = tk.Button(
                        button_frame,
                        text=text,
                        command=command,
                        font=('Arial', 14, 'bold'),
                        width=5,
                        height=2,
                        bg='#ff9500',
                        fg='black'  # Changed from white to black for better visibility
                    )
                elif style == 'Equals.TButton':
                    btn = tk.Button(
                        button_frame,
                        text=text,
                        command=command,
                        font=('Arial', 14, 'bold'),
                        width=5,
                        height=2,
                        bg='#4CAF50',
                        fg='black'  # Changed from white to black for better visibility
                    )
                else:  # Clear buttons
                    btn = tk.Button(
                        button_frame,
                        text=text,
                        command=command,
                        font=('Arial', 12),
                        width=5,
                        height=2,
                        bg='#f44336',
                        fg='black'  # Changed from white to black for better visibility
                    )
                btn.grid(row=row_idx, column=col_idx, padx=2, pady=2, sticky="nsew")
        
        # Configure grid weights
        for i in range(4):
            button_frame.columnconfigure(i, weight=1)
        for i in range(5):
            button_frame.rowconfigure(i, weight=1)
    
    def _create_history_frame(self):
        """Create the history panel."""
        self.history_frame = ttk.LabelFrame(self.master, text="History", padding="10")
        self.history_frame.grid(row=0, column=1, rowspan=2, sticky="nsew", padx=(0, 10), pady=10)
        
        # History list
        self.history_listbox = tk.Listbox(
            self.history_frame,
            font=('Arial', 10),
            width=30,
            height=15,
            selectmode=tk.SINGLE
        )
        self.history_listbox.grid(row=0, column=0, sticky="nsew")
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(self.history_frame, orient="vertical", 
                                  command=self.history_listbox.yview)
        scrollbar.grid(row=0, column=1, sticky="ns")
        self.history_listbox.config(yscrollcommand=scrollbar.set)
        
        # Bind double-click to restore expression
        self.history_listbox.bind('<Double-Button-1>', self._restore_from_history)
        
        # Clear history button
        clear_btn = tk.Button(
            self.history_frame,
            text="Clear History",
            command=self._clear_history,
            font=('Arial', 10),
            bg='#f44336',
            fg='black'  # Changed from white to black for better visibility
        )
        clear_btn.grid(row=1, column=0, columnspan=2, pady=(5, 0), sticky="ew")
        
        # Configure grid weights
        self.history_frame.columnconfigure(0, weight=1)
        self.history_frame.rowconfigure(0, weight=1)
    
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
        self.master.bind('<Delete>', lambda e: self._clear_entry())
    
    def _append_to_expression(self, value: str):
        """Append a value to the current expression."""
        if self.error_state:
            self._clear_display()
        
        self.current_expression += value
        self.expression_var.set(self.current_expression)
        print(f"Button clicked: {value}, Expression: {self.current_expression}")  # Debug
    
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
        self.error_state = False
    
    def _calculate(self):
        """Calculate the current expression."""
        if not self.current_expression:
            return
        
        try:
            # Parse and evaluate expression
            result = self.parser.parse(self.current_expression)
            
            # Format result
            result_str = f"{result:.10g}"
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
        
        # Get recent history
        history = self.history_manager.get_recent(20)
        
        # Add entries to listbox (most recent at top)
        for entry in reversed(history):
            display_text = entry.format_display()
            self.history_listbox.insert(0, display_text)
    
    def _restore_from_history(self, event):
        """Restore an expression from history."""
        selection = self.history_listbox.curselection()
        if selection:
            # Get the selected history entry
            index = selection[0]
            # History is displayed in reverse order
            history = self.history_manager.get_recent(20)
            entry_index = len(history) - 1 - index
            
            if 0 <= entry_index < len(history):
                entry = history[entry_index]
                self.current_expression = entry.expression
                self.expression_var.set(self.current_expression)
    
    def _clear_history(self):
        """Clear calculation history."""
        if messagebox.askyesno("Clear History", 
                               "Are you sure you want to clear all calculation history?"):
            self.history_manager.clear_history()
            self._update_history_display()
    
    def _toggle_history(self):
        """Toggle history panel visibility."""
        if self.show_history.get():
            self.history_frame.grid(row=0, column=1, rowspan=2, sticky="nsew", 
                                    padx=(0, 10), pady=10)
        else:
            self.history_frame.grid_forget()
    
    def _show_about(self):
        """Show about dialog."""
        messagebox.showinfo(
            "About Calculator",
            "GUI Calculator\n\n"
            "A secure calculator with expression parsing\n"
            "and calculation history.\n\n"
            "Built with Python and Tkinter"
        )
    
    def _show_shortcuts(self):
        """Show keyboard shortcuts."""
        shortcuts = """
        Keyboard Shortcuts:
        
        Numbers: 0-9
        Operators: + - * /
        Parentheses: ( )
        Decimal: .
        
        Enter/= : Calculate
        Escape : Clear all
        Backspace : Delete last character
        Delete : Clear entry
        
        Double-click history item to restore
        """
        messagebox.showinfo("Keyboard Shortcuts", shortcuts)


def main():
    """Run the calculator GUI."""
    root = tk.Tk()
    app = CalculatorGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()