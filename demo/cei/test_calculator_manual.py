#!/usr/bin/env python3
"""Manual test script for calculator without pytest dependency."""

from calculator.core import add, subtract, multiply, divide, calculate

def test_arithmetic_operations():
    """Test basic arithmetic operations."""
    print("Testing arithmetic operations...")
    
    # Test addition
    assert add(2, 3) == 5, "Addition failed: 2 + 3"
    assert add(-1, 1) == 0, "Addition failed: -1 + 1"
    assert add(0.5, 0.5) == 1.0, "Addition failed: 0.5 + 0.5"
    print("✓ Addition tests passed")
    
    # Test subtraction
    assert subtract(5, 3) == 2, "Subtraction failed: 5 - 3"
    assert subtract(0, 5) == -5, "Subtraction failed: 0 - 5"
    assert subtract(1.5, 0.5) == 1.0, "Subtraction failed: 1.5 - 0.5"
    print("✓ Subtraction tests passed")
    
    # Test multiplication
    assert multiply(4, 5) == 20, "Multiplication failed: 4 * 5"
    assert multiply(-2, 3) == -6, "Multiplication failed: -2 * 3"
    assert multiply(0, 100) == 0, "Multiplication failed: 0 * 100"
    print("✓ Multiplication tests passed")
    
    # Test division
    assert divide(10, 2) == 5, "Division failed: 10 / 2"
    assert divide(7, 2) == 3.5, "Division failed: 7 / 2"
    assert divide(-6, 3) == -2, "Division failed: -6 / 3"
    assert divide(0, 5) == 0, "Division failed: 0 / 5"
    print("✓ Division tests passed")
    
    # Test division by zero
    assert divide(5, 0) is None, "Division by zero should return None"
    assert divide(-10, 0) is None, "Division by zero should return None"
    print("✓ Division by zero tests passed")

def test_calculate_function():
    """Test the main calculate function."""
    print("\nTesting calculate function...")
    
    # Test valid operations
    assert calculate(10, 5, '+') == 15, "Calculate failed: 10 + 5"
    assert calculate(10, 5, '-') == 5, "Calculate failed: 10 - 5"
    assert calculate(10, 5, '*') == 50, "Calculate failed: 10 * 5"
    assert calculate(10, 5, '/') == 2, "Calculate failed: 10 / 5"
    print("✓ Valid operations tests passed")
    
    # Test invalid operator
    try:
        calculate(1, 2, '^')
        assert False, "Should have raised ValueError for invalid operator"
    except ValueError as e:
        assert "Invalid operator" in str(e), "Wrong error message"
    print("✓ Invalid operator test passed")
    
    # Test division by zero
    result = calculate(10, 0, '/')
    assert result is None, "Division by zero should return None"
    print("✓ Division by zero in calculate test passed")

def test_ui_formatting():
    """Test UI formatting functions."""
    from calculator.ui import format_result
    
    print("\nTesting UI formatting...")
    
    # Test integer results
    assert format_result(3, 4, '+', 7) == "3 + 4 = 7", "Format failed"
    assert format_result(10, 5, '-', 5) == "10 - 5 = 5", "Format failed"
    print("✓ Integer formatting tests passed")
    
    # Test decimal results
    assert format_result(7, 2, '/', 3.5) == "7 / 2 = 3.5", "Format failed"
    print("✓ Decimal formatting tests passed")
    
    # Test trailing zeros removal
    assert format_result(5.0, 2.0, '*', 10.0) == "5 * 2 = 10", "Format failed"
    print("✓ Trailing zeros removal test passed")

def main():
    """Run all tests."""
    print("Running calculator tests...\n")
    
    try:
        test_arithmetic_operations()
        test_calculate_function()
        test_ui_formatting()
        print("\n✅ All tests passed!")
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        return 1
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())