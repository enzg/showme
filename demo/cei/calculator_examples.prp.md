# Calculator Example Patterns Implementation Guide

## Overview
Create Python calculator example patterns demonstrating best practices for CLI, error handling, and GUI implementations.

## Project Structure
```
examples/
├── cli_patterns/
│   └── cli_basic_input.py
├── error_handling/
│   └── div_zero.py
└── gui_patterns/
    └── tkinter_basic.py
```

## Implementation Requirements

### General Guidelines
- Keep all examples under 50 lines
- Follow PEP8 style guide
- Include type hints for all functions
- Add descriptive docstrings
- Ensure all files are immediately testable without errors
- Include helpful comments explaining key concepts

### 1. CLI Basic Input Pattern (`cli_patterns/cli_basic_input.py`)
**Purpose**: Demonstrate a simple command-line calculator with input validation and error handling

**Requirements**:
- Implement a continuous input loop (REPL style)
- Support basic operations: +, -, *, /
- Handle invalid inputs gracefully
- Provide clear user prompts and error messages
- Include exit command (e.g., 'quit' or 'exit')
- Use try-except blocks for error handling

**Example Structure**:
```python
def get_number(prompt: str) -> float:
    """Get a valid number from user input."""
    
def calculate(num1: float, num2: float, operation: str) -> float:
    """Perform calculation based on operation."""
    
def main() -> None:
    """Main calculator loop."""
```

### 2. Division by Zero Handler (`error_handling/div_zero.py`)
**Purpose**: Demonstrate safe division with proper error handling

**Requirements**:
- Create a `safe_divide` function with type hints
- Handle division by zero gracefully
- Return Optional[float] to handle error cases
- Include comprehensive docstring
- Add example usage in `if __name__ == "__main__"` block
- Show both successful and error cases

**Example Structure**:
```python
from typing import Optional

def safe_divide(dividend: float, divisor: float) -> Optional[float]:
    """Safely divide two numbers, handling division by zero."""
```

### 3. Tkinter Basic Calculator (`gui_patterns/tkinter_basic.py`)
**Purpose**: Demonstrate basic GUI calculator layout with Tkinter

**Requirements**:
- Create a simple calculator UI with number buttons (0-9)
- Include basic operation buttons (+, -, *, /)
- Add display field for showing input/results
- Implement clear/reset functionality
- Use grid layout for button organization
- Include basic event handling
- Keep UI responsive and user-friendly

**Key Components**:
- Display widget (Entry or Label)
- Number button grid
- Operation buttons
- Clear and equals buttons
- Basic calculation logic

## Testing Requirements

### Unit Tests
Each example should have corresponding pytest tests:
- `tests/test_cli_basic_input.py`
- `tests/test_div_zero.py`
- `tests/test_tkinter_basic.py` (for testable functions)

### Test Coverage
- Test happy path scenarios
- Test edge cases (division by zero, invalid inputs)
- Test error handling
- Mock user input for CLI testing

## Code Quality Standards

### Documentation
- Module-level docstring explaining the example's purpose
- Function docstrings with parameters and return types
- Inline comments for complex logic

### Error Handling
- Use specific exception types
- Provide helpful error messages
- Never let the program crash unexpectedly

### Type Hints
```python
def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b
```

## Example Implementation Pattern

```python
#!/usr/bin/env python3
"""
Module description explaining the example's purpose.
"""

from typing import Optional

def example_function(param: type) -> return_type:
    """
    Brief description.
    
    Args:
        param: Description of parameter.
        
    Returns:
        Description of return value.
        
    Raises:
        ExceptionType: When this happens.
    """
    # Implementation with comments
    pass

if __name__ == "__main__":
    # Example usage demonstrating the pattern
    pass
```

## Validation Checklist
- [ ] All files under 50 lines
- [ ] PEP8 compliant (use `flake8` or `black`)
- [ ] Type hints on all functions
- [ ] Docstrings present and descriptive
- [ ] Error handling implemented
- [ ] Files run without errors
- [ ] Examples are self-contained and educational
- [ ] Comments explain key concepts
- [ ] Unit tests pass