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