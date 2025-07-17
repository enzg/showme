#!/usr/bin/env python3
"""
Unit tests for safe division function.
"""

import pytest
import sys
import os
from unittest.mock import patch

# Add parent directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from examples.error_handling.div_zero import safe_divide


class TestSafeDivide:
    """Test the safe_divide function."""
    
    def test_normal_division(self):
        """Test normal division cases."""
        assert safe_divide(10, 2) == 5.0
        assert safe_divide(7, 2) == 3.5
        assert safe_divide(-6, 3) == -2.0
        assert safe_divide(0, 5) == 0.0
    
    def test_division_by_zero(self):
        """Test division by zero returns None."""
        with patch('builtins.print') as mock_print:
            result = safe_divide(5, 0)
            assert result is None
            mock_print.assert_called_with("Warning: Division by zero attempted")
    
    def test_float_division(self):
        """Test division with float numbers."""
        assert safe_divide(10.5, 2.5) == 4.2
        result = safe_divide(1, 3)
        assert abs(result - 0.333333) < 0.00001
    
    def test_negative_numbers(self):
        """Test division with negative numbers."""
        assert safe_divide(-10, 2) == -5.0
        assert safe_divide(10, -2) == -5.0
        assert safe_divide(-10, -2) == 5.0
    
    def test_edge_cases(self):
        """Test edge cases."""
        # Very small divisor (not zero)
        result = safe_divide(1, 0.000001)
        assert result == 1000000.0
        
        # Zero dividend
        assert safe_divide(0, 10) == 0.0
        
        # Division by zero with different dividends
        assert safe_divide(100, 0) is None
        assert safe_divide(-50, 0) is None
        assert safe_divide(0, 0) is None


if __name__ == "__main__":
    pytest.main([__file__])