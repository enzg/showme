import pytest
from unittest.mock import patch, call
from calculator.ui import get_number, format_result, get_operator

class TestGetNumber:
    """Test number input function."""
    
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
            mock_print.assert_called_with("Invalid number. Please try again or 'q' to quit.")
    
    @patch('builtins.input', side_effect=['q'])
    def test_quit_command(self, mock_input):
        """Test quit command returns None."""
        result = get_number("Enter number: ")
        assert result is None

class TestGetOperator:
    """Test operator input function."""
    
    @patch('builtins.input', side_effect=['+'])
    def test_valid_operator(self, mock_input):
        """Test valid operator input."""
        result = get_operator()
        assert result == '+'
    
    @patch('builtins.input', side_effect=['%', '*'])
    def test_invalid_then_valid(self, mock_input):
        """Test invalid operator followed by valid."""
        with patch('builtins.print') as mock_print:
            result = get_operator()
            assert result == '*'
    
    @patch('builtins.input', side_effect=['q'])
    def test_quit_command(self, mock_input):
        """Test quit command returns None."""
        result = get_operator()
        assert result is None

class TestFormatResult:
    """Test result formatting."""
    
    def test_integer_results(self):
        """Test formatting with integer results."""
        assert format_result(3, 4, '+', 7) == "3 + 4 = 7"
        assert format_result(10, 5, '-', 5) == "10 - 5 = 5"
    
    def test_decimal_results(self):
        """Test formatting with decimal results."""
        assert format_result(7, 2, '/', 3.5) == "7 / 2 = 3.5"
        assert format_result(0.1, 0.2, '+', 0.3) == "0.1 + 0.2 = 0.3"
    
    def test_removes_trailing_zeros(self):
        """Test formatting removes unnecessary zeros."""
        assert format_result(5.0, 2.0, '*', 10.0) == "5 * 2 = 10"