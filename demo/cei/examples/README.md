# Calculator Example Patterns

This directory contains Python calculator examples demonstrating best practices for CLI, error handling, and GUI implementations.

## Structure

- `cli_patterns/cli_basic_input.py` - REPL-style CLI calculator with input validation
- `error_handling/div_zero.py` - Safe division implementation with error handling
- `gui_patterns/tkinter_basic.py` - Basic GUI calculator using Tkinter

## Running Examples

```bash
# CLI Calculator
python examples/cli_patterns/cli_basic_input.py

# Division by Zero Handler
python examples/error_handling/div_zero.py

# GUI Calculator
python examples/gui_patterns/tkinter_basic.py
```

## Testing

Run tests with pytest:
```bash
python -m pytest tests/ -v
```