#!/usr/bin/env python3
"""Basic CLI input loop example for calculator operations."""

from typing import Optional


def get_user_input() -> Optional[str]:
    """Get user input with basic validation.
    
    Returns:
        User input string or None if user wants to exit.
    """
    try:
        user_input = input("\nEnter calculation (e.g., 2+2) or 'quit' to exit: ")
        return user_input.strip().lower()
    except (KeyboardInterrupt, EOFError):
        print("\nExiting...")
        return None


def process_calculation(expression: str) -> None:
    """Process and evaluate the calculation.
    
    Args:
        expression: Mathematical expression to evaluate.
    """
    try:
        # Basic safety check - only allow digits and operators
        allowed_chars = set('0123456789+-*/()., ')
        if all(c in allowed_chars for c in expression):
            result = eval(expression)
            print(f"Result: {result}")
        else:
            print("Error: Invalid characters in expression")
    except ZeroDivisionError:
        print("Error: Division by zero")
    except Exception as e:
        print(f"Error: Invalid expression - {type(e).__name__}")


def main() -> None:
    """Main CLI loop for calculator."""
    print("Simple Calculator CLI")
    print("Type 'quit' to exit")
    
    while True:
        user_input = get_user_input()
        if user_input is None or user_input == 'quit':
            break
        
        if user_input:
            process_calculation(user_input)


if __name__ == "__main__":
    main()