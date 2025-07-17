#!/usr/bin/env python3
"""User interface module for calculator."""

from typing import Optional, Tuple


def get_numbers() -> Tuple[Optional[float], Optional[float], Optional[str]]:
    """Get two numbers from user input.
    
    Returns:
        Tuple of (number1, number2, error_message).
        If successful, error_message is None.
    """
    try:
        first = input("Enter first number: ").strip()
        if first.lower() in ('q', 'quit'):
            return None, None, 'quit'
        elif first.lower() in ('h', 'help'):
            return None, None, 'help'
            
        second = input("Enter second number: ").strip()
        if second.lower() in ('q', 'quit'):
            return None, None, 'quit'
        elif second.lower() in ('h', 'help'):
            return None, None, 'help'
            
        num1 = float(first)
        num2 = float(second)
        return num1, num2, None
        
    except ValueError:
        return None, None, "Invalid input: Please enter numeric values"


def get_operator() -> Tuple[Optional[str], Optional[str]]:
    """Get operator from user input.
    
    Returns:
        Tuple of (operator, error_message).
        If successful, error_message is None.
    """
    valid_operators = ['+', '-', '*', '/']
    operator = input("Enter operator (+, -, *, /): ").strip()
    
    if operator.lower() in ('q', 'quit'):
        return None, 'quit'
    elif operator.lower() in ('h', 'help'):
        return None, 'help'
    elif operator in valid_operators:
        return operator, None
    else:
        return None, f"Invalid operator. Please use one of: {', '.join(valid_operators)}"


def display_result(num1: float, num2: float, operator: str, result: float) -> None:
    """Display calculation result.
    
    Args:
        num1: First number.
        num2: Second number.
        operator: Mathematical operator.
        result: Calculation result.
    """
    print(f"\n{num1} {operator} {num2} = {result}\n")


def display_help() -> None:
    """Display help menu."""
    print("\n" + "="*40)
    print("Calculator Help Menu")
    print("="*40)
    print("Operations:")
    print("  + : Addition")
    print("  - : Subtraction")
    print("  * : Multiplication")
    print("  / : Division")
    print("\nCommands:")
    print("  h or help : Show this help menu")
    print("  q or quit : Exit calculator")
    print("\nUsage:")
    print("  1. Enter first number")
    print("  2. Enter second number")
    print("  3. Enter operator")
    print("  4. View result")
    print("="*40 + "\n")


def display_error(error_message: str) -> None:
    """Display error message.
    
    Args:
        error_message: Error message to display.
    """
    print(f"\nError: {error_message}\n")


def display_welcome() -> None:
    """Display welcome message."""
    print("\n" + "="*40)
    print("Welcome to Simple Calculator!")
    print("="*40)
    print("Type 'h' for help or 'q' to quit\n")