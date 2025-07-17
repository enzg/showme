#!/usr/bin/env python3
"""Manual test for expression parser."""

import sys
sys.path.insert(0, '.')

from calculator.parser import ExpressionParser

def test_parser():
    """Test the expression parser with various expressions."""
    parser = ExpressionParser()
    
    test_cases = [
        # Basic operations
        ("2+3", 5),
        ("10-4", 6),
        ("3*4", 12),
        ("15/3", 5),
        
        # Order of operations
        ("2+3*4", 14),
        ("10-2*3", 4),
        ("12/3+2", 6),
        ("2*3+4*5", 26),
        
        # Parentheses
        ("(2+3)*4", 20),
        ("2*(3+4)", 14),
        ("(10-4)/2", 3),
        ("((2+3)*4)+1", 21),
        
        # Complex expressions
        ("100/(4*5)+3*7", 26),
        ("(5+3)*(10-6)/2", 16),
        ("2.5*4+3.5", 13.5),
        ("10/4", 2.5),
        
        # Edge cases
        ("5", 5),
        ("-5+10", 5),
        ("10+-5", 5),
        ("3.14*2", 6.28),
    ]
    
    passed = 0
    failed = 0
    
    print("Testing Expression Parser:")
    print("-" * 50)
    
    for expression, expected in test_cases:
        try:
            result = parser.parse(expression)
            if abs(result - expected) < 0.0001:  # Float comparison tolerance
                print(f"✓ {expression:<20} = {result:<10} (expected {expected})")
                passed += 1
            else:
                print(f"✗ {expression:<20} = {result:<10} (expected {expected})")
                failed += 1
        except Exception as e:
            print(f"✗ {expression:<20} ERROR: {str(e)}")
            failed += 1
    
    # Test error cases
    print("\nTesting Error Cases:")
    print("-" * 50)
    
    error_cases = [
        "3++4",
        "(2+3",
        "2+3)",
        "10/0",
        "",
        "2 3",
        "abc",
        "2^3",  # Unsupported operator
    ]
    
    for expression in error_cases:
        try:
            result = parser.parse(expression)
            print(f"✗ {expression:<20} should have raised error but got {result}")
            failed += 1
        except Exception as e:
            print(f"✓ {expression:<20} raised: {type(e).__name__}: {str(e)}")
            passed += 1
    
    print("\n" + "=" * 50)
    print(f"Results: {passed} passed, {failed} failed")
    return failed == 0

if __name__ == "__main__":
    success = test_parser()
    sys.exit(0 if success else 1)