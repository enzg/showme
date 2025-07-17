#!/usr/bin/env python3
"""Demo script to show calculator functionality without interactive input."""

from calculator.core import calculate
from calculator.ui import format_result

def demo():
    """Demonstrate calculator functionality."""
    print("Calculator Demo")
    print("=" * 30)
    
    # Demo calculations
    examples = [
        (10, 5, '+', "Addition"),
        (15, 7, '-', "Subtraction"),
        (6, 8, '*', "Multiplication"),
        (20, 4, '/', "Division"),
        (7, 2, '/', "Division with decimal"),
        (5, 0, '/', "Division by zero")
    ]
    
    for num1, num2, op, desc in examples:
        print(f"\n{desc}:")
        try:
            result = calculate(num1, num2, op)
            if result is None:
                print(f"  {num1} {op} {num2} = Error: Cannot divide by zero!")
            else:
                print(f"  {format_result(num1, num2, op, result)}")
        except ValueError as e:
            print(f"  Error: {e}")
    
    print("\n" + "=" * 30)
    print("To run the interactive calculator:")
    print("  python -m calculator")

if __name__ == "__main__":
    demo()