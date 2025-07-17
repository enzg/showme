#!/usr/bin/env python3
"""
Unit tests for CLI basic input calculator.
"""

import pytest
from unittest.mock import patch
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from examples.cli_patterns.cli_basic_input import get_number, calculate


class TestCalculate:
    """Test the calculate function."""
    
    def test_addition(self):
        """Test addition operation."""
        assert calculate(2, 3, '+') == 5
        assert calculate(-1, 1, '+') == 0
        assert calculate(0.5, 0.5, '+') == 1.0
    
    def test_subtraction(self):
        """Test subtraction operation."""
        assert calculate(5, 3, '-') == 2
        assert calculate(0, 5, '-') == -5
        assert calculate(1.5, 0.5, '-') == 1.0
    
    def test_multiplication(self):
        """Test multiplication operation."""
        assert calculate(4, 5, '*') == 20
        assert calculate(-2, 3, '*') == -6
        assert calculate(0, 100, '*') == 0
    
    def test_division(self):
        """Test division operation."""
        assert calculate(10, 2, '/') == 5
        assert calculate(7, 2, '/') == 3.5
        assert calculate(-6, 3, '/') == -2
    
    def test_division_by_zero(self):
        """Test division by zero raises exception."""
        with pytest.raises(ZeroDivisionError):
            calculate(5, 0, '/')
    
    def test_invalid_operation(self):
        """Test invalid operation raises ValueError."""
        with pytest.raises(ValueError, match="Invalid operation"):
            calculate(1, 2, '^')


class TestGetNumber:
    """Test the get_number function."""
    
    @patch('builtins.input', side_effect=['42'])
    def test_valid_input(self, mock_input):
        """Test valid number input."""
        result = get_number("Enter number: ")
        assert result == 42.0
    
    @patch('builtins.input', side_effect=['abc', '3.14'])
    def test_invalid_then_valid(self, mock_input):
        """Test invalid input followed by valid input."""
        with patch('builtins.print') as mock_print:
            result = get_number("Enter number: ")
            assert result == 3.14
            mock_print.assert_called_with("Invalid number. Please try again.")


if __name__ == "__main__":
    pytest.main([__file__])