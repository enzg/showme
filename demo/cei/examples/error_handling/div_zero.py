#!/usr/bin/env python3
"""Safe division implementation with proper error handling."""

from typing import Optional

def safe_divide(dividend: float, divisor: float) -> Optional[float]:
    """Safely divide two numbers, handling division by zero.
    
    Args:
        dividend: The number to be divided.
        divisor: The number to divide by.
        
    Returns:
        The result of division if successful, None if division by zero.
    """
    if divisor == 0:
        print("Warning: Division by zero attempted")
        return None
    return dividend / divisor

if __name__ == "__main__":
    # Example usage demonstrating both successful and error cases
    print("Safe Division Examples:")
    print("-" * 30)
    
    # Successful division examples
    result = safe_divide(10, 2)
    print(f"10 ÷ 2 = {result}")
    
    result = safe_divide(15.5, 3.1)
    print(f"15.5 ÷ 3.1 = {result:.2f}" if result else "Division failed")
    
    # Division by zero examples
    result = safe_divide(5, 0)
    print(f"5 ÷ 0 = {result}")
    
    # Practical example with error checking
    dividend = 100
    divisor = 0
    result = safe_divide(dividend, divisor)
    if result is not None:
        print(f"Result: {result}")
    else:
        print(f"Cannot divide {dividend} by {divisor}")