#!/usr/bin/env python3
"""Tests for UI module."""

import pytest
import sys
import os
from unittest.mock import patch
from io import StringIO

# Add parent directory to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import ui


class TestInputFunctions:
    """Test user input functions."""
    
    @patch('builtins.input', side_effect=['5', '3'])
    def test_get_numbers_valid(self, mock_input):
        """Test getting valid numbers."""
        num1, num2, error = ui.get_numbers()
        assert num1 == 5.0
        assert num2 == 3.0
        assert error is None
        
    @patch('builtins.input', side_effect=['q'])
    def test_get_numbers_quit_first(self, mock_input):
        """Test quit on first number."""
        num1, num2, error = ui.get_numbers()
        assert num1 is None
        assert num2 is None
        assert error == 'quit'
        
    @patch('builtins.input', side_effect=['5', 'quit'])
    def test_get_numbers_quit_second(self, mock_input):
        """Test quit on second number."""
        num1, num2, error = ui.get_numbers()
        assert num1 is None
        assert num2 is None
        assert error == 'quit'
        
    @patch('builtins.input', side_effect=['h'])
    def test_get_numbers_help(self, mock_input):
        """Test help command."""
        num1, num2, error = ui.get_numbers()
        assert num1 is None
        assert num2 is None
        assert error == 'help'
        
    @patch('builtins.input', side_effect=['abc', '5'])
    def test_get_numbers_invalid(self, mock_input):
        """Test invalid number input."""
        num1, num2, error = ui.get_numbers()
        assert num1 is None
        assert num2 is None
        assert error == "Invalid input: Please enter numeric values"
        
    @patch('builtins.input', side_effect=['+'])
    def test_get_operator_valid(self, mock_input):
        """Test getting valid operator."""
        operator, error = ui.get_operator()
        assert operator == '+'
        assert error is None
        
    @patch('builtins.input', side_effect=['q'])
    def test_get_operator_quit(self, mock_input):
        """Test quit command for operator."""
        operator, error = ui.get_operator()
        assert operator is None
        assert error == 'quit'
        
    @patch('builtins.input', side_effect=['%'])
    def test_get_operator_invalid(self, mock_input):
        """Test invalid operator."""
        operator, error = ui.get_operator()
        assert operator is None
        assert "Invalid operator" in error


class TestDisplayFunctions:
    """Test display functions."""
    
    def test_display_result(self, capsys):
        """Test result display."""
        ui.display_result(10, 5, '+', 15)
        captured = capsys.readouterr()
        assert "10 + 5 = 15" in captured.out
        
    def test_display_help(self, capsys):
        """Test help display."""
        ui.display_help()
        captured = capsys.readouterr()
        assert "Calculator Help Menu" in captured.out
        assert "Addition" in captured.out
        assert "quit : Exit calculator" in captured.out
        
    def test_display_error(self, capsys):
        """Test error display."""
        ui.display_error("Test error message")
        captured = capsys.readouterr()
        assert "Error: Test error message" in captured.out
        
    def test_display_welcome(self, capsys):
        """Test welcome display."""
        ui.display_welcome()
        captured = capsys.readouterr()
        assert "Welcome to Simple Calculator!" in captured.out


class TestInputValidation:
    """Test input validation edge cases."""
    
    @patch('builtins.input', side_effect=['  5.5  ', '  -3.2  '])
    def test_whitespace_handling(self, mock_input):
        """Test handling of whitespace in input."""
        num1, num2, error = ui.get_numbers()
        assert num1 == 5.5
        assert num2 == -3.2
        assert error is None
        
    @patch('builtins.input', side_effect=['QUIT'])
    def test_case_insensitive_commands(self, mock_input):
        """Test case insensitive command handling."""
        num1, num2, error = ui.get_numbers()
        assert error == 'quit'
        
    @patch('builtins.input', side_effect=['  +  '])
    def test_operator_whitespace(self, mock_input):
        """Test operator with whitespace."""
        operator, error = ui.get_operator()
        assert operator == '+'
        assert error is None