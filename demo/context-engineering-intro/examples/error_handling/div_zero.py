#!/usr/bin/env python3
"""Safe division function with zero error handling."""

from typing import Union, Tuple


def safe_divide(dividend: float, divisor: float) -> Tuple[bool, Union[float, str]]:
    """Perform division with zero error handling.
    
    Args:
        dividend: The number to be divided.
        divisor: The number to divide by.
        
    Returns:
        Tuple of (success, result/error_message).
    """
    try:
        if divisor == 0:
            return False, "Cannot divide by zero"
        
        result = dividend / divisor
        return True, result
        
    except TypeError:
        return False, "Invalid input types - numbers required"
    except Exception as e:
        return False, f"Unexpected error: {type(e).__name__}"


def main() -> None:
    """Demonstrate safe division with various test cases."""
    test_cases = [
        (10, 2),    # Normal division
        (10, 0),    # Division by zero
        (0, 5),     # Zero dividend
        (10.5, 2.5),  # Float division
    ]
    
    print("Safe Division Examples:")
    print("-" * 40)
    
    for dividend, divisor in test_cases:
        success, result = safe_divide(dividend, divisor)
        
        if success:
            print(f"{dividend} ÷ {divisor} = {result}")
        else:
            print(f"{dividend} ÷ {divisor} = ERROR: {result}")


if __name__ == "__main__":
    main()