#!/usr/bin/env python3
"""Tests for GUI calculator."""

import pytest
import sys
import os
import tkinter as tk
from unittest.mock import Mock, patch

# Add parent directory to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import gui_calculator


class TestCalculatorGUI:
    """Test GUI calculator functionality."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.root = tk.Tk()
        self.calculator = gui_calculator.CalculatorGUI(self.root)
        
    def teardown_method(self):
        """Clean up after tests."""
        self.root.destroy()
        
    def test_initial_state(self):
        """Test initial calculator state."""
        assert self.calculator.current_number == ""
        assert self.calculator.previous_number is None
        assert self.calculator.operator is None
        assert self.calculator.should_reset_display is False
        assert self.calculator.display.get() == "0"
        
    def test_number_click(self):
        """Test number button clicks."""
        self.calculator.number_click("5")
        assert self.calculator.current_number == "5"
        assert self.calculator.display.get() == "5"
        
        self.calculator.number_click("3")
        assert self.calculator.current_number == "53"
        assert self.calculator.display.get() == "53"
        
    def test_decimal_point(self):
        """Test decimal point handling."""
        self.calculator.number_click("3")
        self.calculator.number_click(".")
        self.calculator.number_click("1")
        self.calculator.number_click("4")
        assert self.calculator.current_number == "3.14"
        assert self.calculator.display.get() == "3.14"
        
        # Test multiple decimal points (should be ignored)
        self.calculator.number_click(".")
        assert self.calculator.current_number == "3.14"
        
    def test_operator_click(self):
        """Test operator button clicks."""
        self.calculator.number_click("5")
        self.calculator.operator_click("+")
        assert self.calculator.previous_number == 5.0
        assert self.calculator.operator == "+"
        assert self.calculator.current_number == ""
        
    def test_simple_calculation(self):
        """Test simple addition."""
        self.calculator.number_click("5")
        self.calculator.operator_click("+")
        self.calculator.number_click("3")
        self.calculator.equals()
        assert self.calculator.display.get() == "8"
        assert len(self.calculator.history) == 1
        assert "5.0 + 3.0 = 8" in self.calculator.history[0]
        
    def test_floating_point_calculation(self):
        """Test floating point calculation."""
        self.calculator.number_click("0")
        self.calculator.number_click(".")
        self.calculator.number_click("1")
        self.calculator.operator_click("+")
        self.calculator.number_click("0")
        self.calculator.number_click(".")
        self.calculator.number_click("2")
        self.calculator.equals()
        # Check that result is properly formatted
        result = self.calculator.display.get()
        assert result == "0.3"  # Should display as 0.3, not 0.30000000000000004
        
    def test_division_by_zero(self):
        """Test division by zero handling."""
        self.calculator.number_click("5")
        self.calculator.operator_click("/")
        self.calculator.number_click("0")
        self.calculator.equals()
        assert "Error" in self.calculator.display.get()
        # Should clear state after error
        assert self.calculator.current_number == ""
        assert self.calculator.previous_number is None
        
    def test_clear_button(self):
        """Test clear functionality."""
        self.calculator.number_click("5")
        self.calculator.operator_click("+")
        self.calculator.number_click("3")
        self.calculator.clear()
        
        assert self.calculator.current_number == ""
        assert self.calculator.previous_number is None
        assert self.calculator.operator is None
        assert self.calculator.display.get() == "0"
        
    def test_consecutive_calculations(self):
        """Test chaining calculations."""
        # 5 + 3 = 8
        self.calculator.number_click("5")
        self.calculator.operator_click("+")
        self.calculator.number_click("3")
        self.calculator.equals()
        
        # 8 * 2 = 16
        self.calculator.operator_click("*")
        self.calculator.number_click("2")
        self.calculator.equals()
        assert self.calculator.display.get() == "16"
        
    def test_integer_display(self):
        """Test that whole numbers display without decimal."""
        self.calculator.number_click("4")
        self.calculator.operator_click("/")
        self.calculator.number_click("2")
        self.calculator.equals()
        assert self.calculator.display.get() == "2"  # Not "2.0"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])