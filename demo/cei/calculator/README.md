# Calculator Application

A Python calculator with both CLI and GUI interfaces, featuring secure expression parsing without eval() and calculation history.

## Features

- **Dual Interface**: Command-line (CLI) and graphical (GUI) interfaces
- **Secure Expression Parser**: Evaluates mathematical expressions without using eval()
- **Calculation History**: Tracks and displays previous calculations
- **Order of Operations**: Follows PEMDAS rules
- **Parentheses Support**: Handles nested parentheses correctly
- **Keyboard Support**: Full keyboard shortcuts in GUI mode

## Installation

Requires Python 3.8+ with tkinter for GUI support.

```bash
# Clone the repository
git clone <repository-url>
cd calculator

# No additional dependencies required for basic functionality
# For testing: pip install pytest pytest-cov
```

## Usage

### GUI Mode (Default)
```bash
python -m calculator --gui
```

### CLI Mode
```bash
python -m calculator --cli
# or simply
python -m calculator
```

### CLI Features

The CLI supports two modes:

1. **Expression Mode** (default): Enter complete expressions
   ```
   Enter expression: 3+4*2
   Result: 3+4*2 = 11
   ```

2. **Step-by-step Mode**: Enter numbers and operators separately
   ```
   Enter first number: 10
   Enter operator (+, -, *, /): *
   Enter second number: 5
   Result: 10 * 5 = 50
   ```

Commands:
- `expr` - Toggle between expression and step-by-step modes
- `history` or `hist` - Show calculation history
- `clear history` - Clear all history
- `h` or `help` - Show help
- `q` or `quit` - Exit

### GUI Features

- Calculator buttons for digits and operations
- Display shows current expression and result
- History panel shows previous calculations
- Double-click history item to restore expression
- Full keyboard support

Keyboard shortcuts:
- Numbers: 0-9
- Operators: + - * /
- Parentheses: ( )
- Enter or = : Calculate
- Escape : Clear all
- Backspace : Delete last character
- Delete : Clear entry

## Architecture

```
calculator/
├── __init__.py
├── core.py        # Basic arithmetic operations
├── parser.py      # Expression parser (no eval!)
├── history.py     # Calculation history management
├── gui.py         # Tkinter GUI interface
├── cli.py         # Enhanced CLI interface
└── ui.py          # Original UI utilities
```

### Key Components

1. **Expression Parser** (`parser.py`)
   - Tokenizes expressions into numbers and operators
   - Converts infix to postfix notation
   - Evaluates expressions following PEMDAS
   - No use of eval() for security

2. **History Manager** (`history.py`)
   - Stores calculations with timestamps
   - Provides search and retrieval methods
   - Can save/load from JSON files

3. **GUI Interface** (`gui.py`)
   - Clean, intuitive calculator layout
   - Real-time expression display
   - Integrated history panel
   - Responsive to both mouse and keyboard

## Testing

Run tests with pytest:
```bash
pytest tests/ -v
pytest --cov=calculator tests/  # With coverage
```

## Security

This calculator does NOT use Python's eval() function, making it safe from code injection attacks. The custom expression parser only recognizes:
- Numbers (integers and decimals)
- Basic operators: + - * /
- Parentheses: ( )

Any other input is rejected as invalid.