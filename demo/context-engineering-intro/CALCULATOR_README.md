# Simple Command-Line Calculator

A Python command-line calculator that supports basic arithmetic operations with robust error handling.

## Features

- Basic arithmetic operations: addition (+), subtraction (-), multiplication (*), division (/)
- Interactive command-line interface
- Comprehensive error handling for invalid inputs and division by zero
- Help menu (type 'h' or 'help')
- Clean exit (type 'q' or 'quit')

## Installation

1. Clone this repository or download the files
2. Ensure Python 3.6+ is installed
3. No external dependencies required for the calculator
4. For running tests, install pytest: `pip install pytest`

## Usage

Run the calculator:

```bash
python calculator.py
```

### Example Session

```
========================================
Welcome to Simple Calculator!
========================================
Type 'h' for help or 'q' to quit

Enter first number: 10
Enter second number: 5
Enter operator (+, -, *, /): +

10.0 + 5.0 = 15.0

Enter first number: 20
Enter second number: 4
Enter operator (+, -, *, /): /

20.0 / 4.0 = 5.0

Enter first number: q

Goodbye!
```

### Commands

- `h` or `help`: Display help menu
- `q` or `quit`: Exit the calculator
- `Ctrl+C`: Force exit

## Project Structure

```
.
├── calculator.py    # Main application entry point
├── core.py         # Core calculation logic
├── ui.py           # User interface functions
├── tests/          # Test suite
│   ├── test_core.py
│   └── test_ui.py
└── README.md       # This file
```

## Development

### Running Tests

```bash
python -m pytest tests/ -v
```

### Code Style

This project follows PEP8 style guidelines with:
- Type hints for all functions
- Comprehensive docstrings
- Modular design for easy extension

### Extending the Calculator

To add new operations:

1. Add the operation function to `core.py`
2. Update the `calculate()` function in `core.py`
3. Update the help menu in `ui.py`
4. Add corresponding tests

## Error Handling

The calculator handles:
- Invalid numeric inputs
- Unknown operators
- Division by zero
- Keyboard interrupts (Ctrl+C)

## Future Enhancements

- Additional operations (power, square root, etc.)
- Expression parsing for complex calculations
- History of calculations
- GUI version using the existing modular structure