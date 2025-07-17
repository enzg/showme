# PRP: Command-Line Calculator Implementation

## Project Overview
Build a modular, production-ready command-line calculator in Python that supports basic arithmetic operations with comprehensive error handling and user-friendly features.

## Requirements Summary
### Core Features
- Basic arithmetic operations: addition (+), subtraction (-), multiplication (*), division (/)
- Two-number input with operator selection
- Continuous calculation loop with 'q' to quit
- Help menu accessible with 'h'
- Clear output format: "3 + 4 = 7"

### Technical Requirements
- Python 3.x with type hints
- Modular architecture: core.py for logic, ui.py for interface
- PEP8 compliant code
- Comprehensive error handling
- Unit tests using pytest
- No global variables unless necessary

### Error Handling
- Invalid operators
- Non-numeric inputs
- Division by zero
- Keyboard interrupts

## Implementation Plan

### Phase 1: Project Setup (Confidence: 10/10)
**Tasks:**
1. Create project structure
   - `calculator/` - Main package directory
   - `calculator/core.py` - Business logic module
   - `calculator/ui.py` - User interface module
   - `calculator/__init__.py` - Package initialization
   - `tests/` - Test directory
   - `requirements.txt` - Dependencies (pytest)

**Validation Checkpoint:**
- Verify directory structure created
- Ensure all __init__.py files are in place
- Check requirements.txt contains pytest

### Phase 2: Core Logic Implementation (Confidence: 9/10)
**File: calculator/core.py**
```python
from typing import Optional, Dict, Callable

def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b

def subtract(a: float, b: float) -> float:
    """Subtract b from a."""
    return a - b

def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b

def divide(a: float, b: float) -> Optional[float]:
    """Divide a by b. Returns None if b is zero."""
    if b == 0:
        return None
    return a / b

def get_operations() -> Dict[str, Callable[[float, float], Optional[float]]]:
    """Return dictionary of available operations."""
    return {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide
    }

def calculate(num1: float, num2: float, operator: str) -> Optional[float]:
    """Perform calculation based on operator."""
    operations = get_operations()
    if operator not in operations:
        raise ValueError(f"Invalid operator: {operator}. Valid operators: {', '.join(operations.keys())}")
    return operations[operator](num1, num2)
```

**Validation Checkpoint:**
- All arithmetic functions have type hints
- Division function returns Optional[float]
- calculate function validates operators
- Functions have proper docstrings

### Phase 3: User Interface Implementation (Confidence: 9/10)
**File: calculator/ui.py**
```python
from typing import Optional
from calculator.core import calculate, get_operations

def display_welcome() -> None:
    """Display welcome message and instructions."""
    print("=" * 50)
    print("Welcome to Command-Line Calculator")
    print("=" * 50)
    print("Commands:")
    print("  - Enter two numbers and an operator to calculate")
    print("  - 'h' or 'help' - Show help menu")
    print("  - 'q' or 'quit' - Exit calculator")
    print("=" * 50)

def display_help() -> None:
    """Display help information."""
    operations = get_operations()
    print("\nHelp Menu:")
    print("-" * 30)
    print("Available operations:")
    for op in operations:
        print(f"  {op} - {operations[op].__doc__}")
    print("\nUsage:")
    print("  1. Enter first number")
    print("  2. Enter operator (+, -, *, /)")
    print("  3. Enter second number")
    print("  4. View result")
    print("\nCommands:")
    print("  'h' or 'help' - Show this menu")
    print("  'q' or 'quit' - Exit calculator")
    print("-" * 30)

def get_number(prompt: str) -> Optional[float]:
    """Get a valid number from user input."""
    while True:
        user_input = input(prompt).strip()
        if user_input.lower() in ('q', 'quit'):
            return None
        try:
            return float(user_input)
        except ValueError:
            print("Invalid number. Please try again or 'q' to quit.")

def get_operator() -> Optional[str]:
    """Get a valid operator from user input."""
    operations = get_operations()
    valid_ops = list(operations.keys())
    prompt = f"Enter operator ({', '.join(valid_ops)}): "
    
    while True:
        user_input = input(prompt).strip()
        if user_input.lower() in ('q', 'quit'):
            return None
        if user_input in valid_ops:
            return user_input
        print(f"Invalid operator. Valid operators: {', '.join(valid_ops)}")

def format_result(num1: float, num2: float, operator: str, result: float) -> str:
    """Format calculation result for display."""
    # Format numbers to remove unnecessary decimal places
    num1_str = f"{num1:.10g}"
    num2_str = f"{num2:.10g}"
    result_str = f"{result:.10g}"
    return f"{num1_str} {operator} {num2_str} = {result_str}"

def run_calculator() -> None:
    """Main calculator loop."""
    display_welcome()
    
    while True:
        try:
            # Get user command
            command = input("\nEnter command (or press Enter to calculate): ").strip().lower()
            
            if command in ('q', 'quit', 'exit'):
                print("Thank you for using Calculator. Goodbye!")
                break
            elif command in ('h', 'help'):
                display_help()
                continue
            
            # Get first number
            num1 = get_number("Enter first number: ")
            if num1 is None:
                print("Thank you for using Calculator. Goodbye!")
                break
            
            # Get operator
            operator = get_operator()
            if operator is None:
                print("Thank you for using Calculator. Goodbye!")
                break
            
            # Get second number
            num2 = get_number("Enter second number: ")
            if num2 is None:
                print("Thank you for using Calculator. Goodbye!")
                break
            
            # Perform calculation
            result = calculate(num1, num2, operator)
            
            if result is None:
                print("Error: Cannot divide by zero!")
            else:
                print(f"\nResult: {format_result(num1, num2, operator, result)}")
                
        except ValueError as e:
            print(f"Error: {e}")
        except KeyboardInterrupt:
            print("\n\nInterrupted. Thank you for using Calculator. Goodbye!")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            print("Please try again.")
```

**Validation Checkpoint:**
- All UI functions have proper type hints
- Input validation handles 'q' quit commands
- Help menu displays all operations
- Result formatting handles decimal places appropriately
- Comprehensive error handling in main loop

### Phase 4: Main Entry Point (Confidence: 10/10)
**File: calculator/__main__.py**
```python
#!/usr/bin/env python3
"""Command-line calculator entry point."""

from calculator.ui import run_calculator

def main() -> None:
    """Main entry point for the calculator."""
    run_calculator()

if __name__ == "__main__":
    main()
```

**Validation Checkpoint:**
- Entry point uses proper shebang
- Imports from correct module
- Can be run with `python -m calculator`

### Phase 5: Unit Tests Implementation (Confidence: 9/10)
**File: tests/test_core.py**
```python
import pytest
from calculator.core import add, subtract, multiply, divide, calculate

class TestArithmeticOperations:
    """Test basic arithmetic operations."""
    
    def test_addition(self):
        """Test addition operation."""
        assert add(2, 3) == 5
        assert add(-1, 1) == 0
        assert add(0.5, 0.5) == 1.0
        assert add(0, 0) == 0
    
    def test_subtraction(self):
        """Test subtraction operation."""
        assert subtract(5, 3) == 2
        assert subtract(0, 5) == -5
        assert subtract(1.5, 0.5) == 1.0
        assert subtract(-5, -3) == -2
    
    def test_multiplication(self):
        """Test multiplication operation."""
        assert multiply(4, 5) == 20
        assert multiply(-2, 3) == -6
        assert multiply(0, 100) == 0
        assert multiply(2.5, 2) == 5.0
    
    def test_division(self):
        """Test division operation."""
        assert divide(10, 2) == 5
        assert divide(7, 2) == 3.5
        assert divide(-6, 3) == -2
        assert divide(0, 5) == 0
    
    def test_division_by_zero(self):
        """Test division by zero returns None."""
        assert divide(5, 0) is None
        assert divide(-10, 0) is None
        assert divide(0, 0) is None

class TestCalculateFunction:
    """Test the main calculate function."""
    
    def test_valid_operations(self):
        """Test calculate with valid operations."""
        assert calculate(10, 5, '+') == 15
        assert calculate(10, 5, '-') == 5
        assert calculate(10, 5, '*') == 50
        assert calculate(10, 5, '/') == 2
    
    def test_invalid_operator(self):
        """Test calculate with invalid operator."""
        with pytest.raises(ValueError, match="Invalid operator"):
            calculate(1, 2, '^')
        with pytest.raises(ValueError, match="Invalid operator"):
            calculate(1, 2, '%')
    
    def test_division_by_zero_in_calculate(self):
        """Test calculate handles division by zero."""
        result = calculate(10, 0, '/')
        assert result is None
```

**File: tests/test_ui.py**
```python
import pytest
from unittest.mock import patch, call
from calculator.ui import get_number, format_result, get_operator

class TestGetNumber:
    """Test number input function."""
    
    @patch('builtins.input', side_effect=['42'])
    def test_valid_input(self, mock_input):
        """Test valid number input."""
        result = get_number("Enter number: ")
        assert result == 42.0
    
    @patch('builtins.input', side_effect=['abc', '3.14'])
    def test_invalid_then_valid(self, mock_input):
        """Test invalid input followed by valid input."""
        with patch('builtins.print') as mock_print:
            result = get_number("Enter number: ")
            assert result == 3.14
            mock_print.assert_called_with("Invalid number. Please try again or 'q' to quit.")
    
    @patch('builtins.input', side_effect=['q'])
    def test_quit_command(self, mock_input):
        """Test quit command returns None."""
        result = get_number("Enter number: ")
        assert result is None

class TestGetOperator:
    """Test operator input function."""
    
    @patch('builtins.input', side_effect=['+'])
    def test_valid_operator(self, mock_input):
        """Test valid operator input."""
        result = get_operator()
        assert result == '+'
    
    @patch('builtins.input', side_effect=['%', '*'])
    def test_invalid_then_valid(self, mock_input):
        """Test invalid operator followed by valid."""
        with patch('builtins.print') as mock_print:
            result = get_operator()
            assert result == '*'
    
    @patch('builtins.input', side_effect=['q'])
    def test_quit_command(self, mock_input):
        """Test quit command returns None."""
        result = get_operator()
        assert result is None

class TestFormatResult:
    """Test result formatting."""
    
    def test_integer_results(self):
        """Test formatting with integer results."""
        assert format_result(3, 4, '+', 7) == "3 + 4 = 7"
        assert format_result(10, 5, '-', 5) == "10 - 5 = 5"
    
    def test_decimal_results(self):
        """Test formatting with decimal results."""
        assert format_result(7, 2, '/', 3.5) == "7 / 2 = 3.5"
        assert format_result(0.1, 0.2, '+', 0.3) == "0.1 + 0.2 = 0.3"
    
    def test_removes_trailing_zeros(self):
        """Test formatting removes unnecessary zeros."""
        assert format_result(5.0, 2.0, '*', 10.0) == "5 * 2 = 10"
```

**Validation Checkpoint:**
- Comprehensive test coverage for all operations
- Tests for edge cases (division by zero, invalid inputs)
- Mock-based tests for user input functions
- All tests follow pytest conventions

### Phase 6: Integration and Final Testing (Confidence: 10/10)
**Tasks:**
1. Create setup.py for package installation
2. Update requirements.txt
3. Run full test suite
4. Manual testing of all features
5. Code formatting check (PEP8)

**File: setup.py**
```python
from setuptools import setup, find_packages

setup(
    name="calculator",
    version="1.0.0",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'calculator=calculator.__main__:main',
        ],
    },
    python_requires='>=3.6',
)
```

**Validation Checkpoint:**
- All tests pass: `pytest tests/`
- Code follows PEP8: `flake8 calculator/`
- Calculator runs: `python -m calculator`
- All features work as expected

## Risk Assessment
1. **User Input Handling** (Low Risk): Comprehensive validation implemented
2. **Division by Zero** (Low Risk): Properly handled with Optional return type
3. **Type Safety** (Low Risk): Full type hints throughout
4. **Test Coverage** (Low Risk): Comprehensive test suite
5. **Future Extensibility** (Low Risk): Modular design supports GUI addition

## Success Criteria Validation
- [x] Supports all four basic operations
- [x] Handles invalid operators with clear error messages
- [x] Handles non-numeric inputs with retry logic
- [x] Handles division by zero gracefully
- [x] Continuous loop with 'q' to quit
- [x] Clear output format (e.g., "3 + 4 = 7")
- [x] Help menu accessible with 'h'
- [x] Modular code structure for future GUI extension
- [x] Comprehensive pytest test suite
- [x] PEP8 compliant code
- [x] Type hints throughout
- [x] Proper docstrings

## Next Steps
1. Execute implementation following this plan
2. Run validation checkpoints after each phase
3. Perform comprehensive testing
4. Document any deviations from plan
5. Consider future enhancements (GUI, advanced operations, history)