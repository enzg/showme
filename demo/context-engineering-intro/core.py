#!/usr/bin/env python3
"""Core calculator logic module."""

from typing import Tuple, Union


def add(a: float, b: float) -> float:
    """Add two numbers.
    
    Args:
        a: First number.
        b: Second number.
        
    Returns:
        Sum of a and b.
    """
    return a + b


def subtract(a: float, b: float) -> float:
    """Subtract b from a.
    
    Args:
        a: First number.
        b: Second number.
        
    Returns:
        Difference of a and b.
    """
    return a - b


def multiply(a: float, b: float) -> float:
    """Multiply two numbers.
    
    Args:
        a: First number.
        b: Second number.
        
    Returns:
        Product of a and b.
    """
    return a * b


def divide(a: float, b: float) -> Tuple[bool, Union[float, str]]:
    """Safely divide a by b.
    
    Args:
        a: Dividend.
        b: Divisor.
        
    Returns:
        Tuple of (success, result/error_message).
    """
    if b == 0:
        return False, "Cannot divide by zero"
    
    return True, a / b


def calculate(a: float, b: float, operator: str) -> Tuple[bool, Union[float, str]]:
    """Perform calculation based on operator.
    
    Args:
        a: First number.
        b: Second number.
        operator: Mathematical operator (+, -, *, /).
        
    Returns:
        Tuple of (success, result/error_message).
    """
    operations = {
        '+': add,
        '-': subtract,
        '*': multiply
    }
    
    if operator in operations:
        result = operations[operator](a, b)
        return True, result
    elif operator == '/':
        return divide(a, b)
    else:
        return False, f"Invalid operator: {operator}"