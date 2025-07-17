#!/usr/bin/env python3
"""Tests for core calculator logic."""

import pytest
import sys
import os
import math

# Add parent directory to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import core


class TestArithmeticOperations:
    """Test basic arithmetic operations."""
    
    def test_add(self):
        """Test addition function."""
        assert core.add(2, 3) == 5
        assert core.add(-1, 1) == 0
        assert core.add(0, 0) == 0
        assert core.add(1.5, 2.5) == 4.0
        # Test floating point precision
        assert math.isclose(core.add(0.1, 0.2), 0.3, rel_tol=1e-9)
        
    def test_subtract(self):
        """Test subtraction function."""
        assert core.subtract(5, 3) == 2
        assert core.subtract(-1, -1) == 0
        assert core.subtract(0, 5) == -5
        assert core.subtract(10.5, 0.5) == 10.0
        
    def test_multiply(self):
        """Test multiplication function."""
        assert core.multiply(3, 4) == 12
        assert core.multiply(-2, 3) == -6
        assert core.multiply(0, 100) == 0
        assert core.multiply(2.5, 4) == 10.0
        
    def test_divide(self):
        """Test division function."""
        success, result = core.divide(10, 2)
        assert success is True
        assert result == 5.0
        
        success, result = core.divide(7, 2)
        assert success is True
        assert result == 3.5
        
        success, result = core.divide(-10, 2)
        assert success is True
        assert result == -5.0
        
    def test_divide_by_zero(self):
        """Test division by zero handling."""
        success, result = core.divide(10, 0)
        assert success is False
        assert result == "Cannot divide by zero"
        
        success, result = core.divide(0, 0)
        assert success is False
        assert result == "Cannot divide by zero"


class TestCalculateDispatcher:
    """Test calculate dispatcher function."""
    
    def test_calculate_addition(self):
        """Test calculate with addition."""
        success, result = core.calculate(2, 3, '+')
        assert success is True
        assert result == 5
        
    def test_calculate_subtraction(self):
        """Test calculate with subtraction."""
        success, result = core.calculate(10, 3, '-')
        assert success is True
        assert result == 7
        
    def test_calculate_multiplication(self):
        """Test calculate with multiplication."""
        success, result = core.calculate(4, 5, '*')
        assert success is True
        assert result == 20
        
    def test_calculate_division(self):
        """Test calculate with division."""
        success, result = core.calculate(20, 4, '/')
        assert success is True
        assert result == 5.0
        
    def test_calculate_division_by_zero(self):
        """Test calculate with division by zero."""
        success, result = core.calculate(10, 0, '/')
        assert success is False
        assert result == "Cannot divide by zero"
        
    def test_calculate_invalid_operator(self):
        """Test calculate with invalid operator."""
        success, result = core.calculate(10, 5, '%')
        assert success is False
        assert result == "Invalid operator: %"
        
        success, result = core.calculate(10, 5, 'x')
        assert success is False
        assert result == "Invalid operator: x"


class TestEdgeCases:
    """Test edge cases and special scenarios."""
    
    def test_large_numbers(self):
        """Test operations with large numbers."""
        assert core.add(1e10, 1e10) == 2e10
        assert core.multiply(1e5, 1e5) == 1e10
        
    def test_very_small_numbers(self):
        """Test operations with very small numbers."""
        success, result = core.divide(1, 1000000)
        assert success is True
        assert result == 1e-6
        
    def test_negative_numbers(self):
        """Test operations with negative numbers."""
        assert core.add(-5, -3) == -8
        assert core.subtract(-5, -3) == -2
        assert core.multiply(-4, -5) == 20
        assert core.multiply(-4, 5) == -20
        
    def test_floating_point_precision(self):
        """Test floating point precision issues."""
        # Classic 0.1 + 0.2 != 0.3 problem
        result = core.add(0.1, 0.2)
        assert math.isclose(result, 0.3, rel_tol=1e-9)
        
        # Other problematic calculations
        assert math.isclose(core.subtract(1.0, 0.9), 0.1, rel_tol=1e-9)
        assert math.isclose(core.multiply(0.1, 0.2), 0.02, rel_tol=1e-9)
        
        success, result = core.divide(1.0, 3.0)
        assert success is True
        assert math.isclose(result * 3, 1.0, rel_tol=1e-9)