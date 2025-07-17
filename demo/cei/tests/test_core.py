import pytest
from calculator.core import add, subtract, multiply, divide, calculate

class TestArithmeticOperations:
    """Test basic arithmetic operations."""
    
    def test_addition(self):
        """Test addition operation."""
        assert add(2, 3) == 5
        assert add(-1, 1) == 0
        assert add(0.5, 0.5) == 1.0
        assert add(0, 0) == 0
    
    def test_subtraction(self):
        """Test subtraction operation."""
        assert subtract(5, 3) == 2
        assert subtract(0, 5) == -5
        assert subtract(1.5, 0.5) == 1.0
        assert subtract(-5, -3) == -2
    
    def test_multiplication(self):
        """Test multiplication operation."""
        assert multiply(4, 5) == 20
        assert multiply(-2, 3) == -6
        assert multiply(0, 100) == 0
        assert multiply(2.5, 2) == 5.0
    
    def test_division(self):
        """Test division operation."""
        assert divide(10, 2) == 5
        assert divide(7, 2) == 3.5
        assert divide(-6, 3) == -2
        assert divide(0, 5) == 0
    
    def test_division_by_zero(self):
        """Test division by zero returns None."""
        assert divide(5, 0) is None
        assert divide(-10, 0) is None
        assert divide(0, 0) is None

class TestCalculateFunction:
    """Test the main calculate function."""
    
    def test_valid_operations(self):
        """Test calculate with valid operations."""
        assert calculate(10, 5, '+') == 15
        assert calculate(10, 5, '-') == 5
        assert calculate(10, 5, '*') == 50
        assert calculate(10, 5, '/') == 2
    
    def test_invalid_operator(self):
        """Test calculate with invalid operator."""
        with pytest.raises(ValueError, match="Invalid operator"):
            calculate(1, 2, '^')
        with pytest.raises(ValueError, match="Invalid operator"):
            calculate(1, 2, '%')
    
    def test_division_by_zero_in_calculate(self):
        """Test calculate handles division by zero."""
        result = calculate(10, 0, '/')
        assert result is None