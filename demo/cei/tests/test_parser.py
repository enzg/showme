"""
Tests for the expression parser module.
"""
import pytest
from calculator.parser import ExpressionParser, Token, TokenType


class TestExpressionParser:
    """Test cases for ExpressionParser class."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.parser = ExpressionParser()
    
    def test_tokenize_simple_expression(self):
        """Test tokenization of simple expressions."""
        tokens = self.parser.tokenize("3+4")
        assert len(tokens) == 3
        assert tokens[0].type == TokenType.NUMBER
        assert tokens[0].value == 3.0
        assert tokens[1].type == TokenType.OPERATOR
        assert tokens[1].value == '+'
        assert tokens[2].type == TokenType.NUMBER
        assert tokens[2].value == 4.0
    
    def test_tokenize_with_decimals(self):
        """Test tokenization with decimal numbers."""
        tokens = self.parser.tokenize("3.14*2.5")
        assert len(tokens) == 3
        assert tokens[0].value == 3.14
        assert tokens[2].value == 2.5
    
    def test_tokenize_with_parentheses(self):
        """Test tokenization with parentheses."""
        tokens = self.parser.tokenize("(3+4)*2")
        assert len(tokens) == 7
        assert tokens[0].type == TokenType.LEFT_PAREN
        assert tokens[4].type == TokenType.RIGHT_PAREN
    
    def test_tokenize_with_spaces(self):
        """Test that spaces are handled correctly."""
        tokens1 = self.parser.tokenize("3 + 4 * 2")
        tokens2 = self.parser.tokenize("3+4*2")
        assert len(tokens1) == len(tokens2)
    
    def test_tokenize_invalid_characters(self):
        """Test that invalid characters raise ValueError."""
        with pytest.raises(ValueError, match="Invalid characters"):
            self.parser.tokenize("3+4x")
    
    def test_parse_simple_addition(self):
        """Test parsing simple addition."""
        result = self.parser.parse("3+4")
        assert result == 7
    
    def test_parse_simple_subtraction(self):
        """Test parsing simple subtraction."""
        result = self.parser.parse("10-3")
        assert result == 7
    
    def test_parse_simple_multiplication(self):
        """Test parsing simple multiplication."""
        result = self.parser.parse("3*4")
        assert result == 12
    
    def test_parse_simple_division(self):
        """Test parsing simple division."""
        result = self.parser.parse("12/3")
        assert result == 4
    
    def test_parse_order_of_operations(self):
        """Test that PEMDAS order is followed."""
        # Multiplication before addition
        assert self.parser.parse("3+4*2") == 11
        # Division before subtraction
        assert self.parser.parse("10-6/2") == 7
        # Multiple operations
        assert self.parser.parse("2*3+4*5") == 26
    
    def test_parse_parentheses(self):
        """Test that parentheses override order of operations."""
        assert self.parser.parse("(3+4)*2") == 14
        assert self.parser.parse("2*(3+4)") == 14
        assert self.parser.parse("(10-6)/2") == 2
    
    def test_parse_nested_parentheses(self):
        """Test nested parentheses."""
        assert self.parser.parse("((3+4)*2)+1") == 15
        assert self.parser.parse("2*((3+4)+(5+6))") == 36
    
    def test_parse_decimal_results(self):
        """Test expressions that result in decimals."""
        assert self.parser.parse("10/3") == pytest.approx(3.333333, rel=1e-5)
        assert self.parser.parse("1.5*2") == 3.0
    
    def test_parse_division_by_zero(self):
        """Test that division by zero raises ZeroDivisionError."""
        with pytest.raises(ZeroDivisionError):
            self.parser.parse("10/0")
        with pytest.raises(ZeroDivisionError):
            self.parser.parse("5/(3-3)")
    
    def test_parse_empty_expression(self):
        """Test that empty expressions raise ValueError."""
        with pytest.raises(ValueError, match="Empty expression"):
            self.parser.parse("")
        with pytest.raises(ValueError, match="Empty expression"):
            self.parser.parse("   ")
    
    def test_parse_mismatched_parentheses(self):
        """Test that mismatched parentheses raise ValueError."""
        with pytest.raises(ValueError, match="Mismatched parentheses"):
            self.parser.parse("(3+4")
        with pytest.raises(ValueError, match="Mismatched parentheses"):
            self.parser.parse("3+4)")
        with pytest.raises(ValueError, match="Mismatched parentheses"):
            self.parser.parse("((3+4)")
    
    def test_parse_invalid_expression(self):
        """Test various invalid expressions."""
        # Missing operand
        with pytest.raises(ValueError):
            self.parser.parse("3+")
        # Missing operator
        with pytest.raises(ValueError):
            self.parser.parse("3 4")
        # Double operator
        with pytest.raises(ValueError):
            self.parser.parse("3++4")
    
    def test_validate_expression(self):
        """Test expression validation without evaluation."""
        # Valid expressions
        valid, error = self.parser.validate_expression("3+4")
        assert valid is True
        assert error is None
        
        valid, error = self.parser.validate_expression("(3+4)*2")
        assert valid is True
        assert error is None
        
        # Invalid expressions
        valid, error = self.parser.validate_expression("3+")
        assert valid is False
        assert "Invalid expression" in error
        
        valid, error = self.parser.validate_expression("(3+4")
        assert valid is False
        assert "Mismatched parentheses" in error
    
    def test_complex_expressions(self):
        """Test complex real-world expressions."""
        # Scientific calculator type expressions
        assert self.parser.parse("((12+8)*3)/4-5") == 10
        assert self.parser.parse("100/(4*5)+3*7") == 26
        assert self.parser.parse("(15-3)/(2+2)*5") == 15
    
    def test_associativity(self):
        """Test left-to-right associativity for same precedence operators."""
        # Left-to-right for subtraction
        assert self.parser.parse("10-5-2") == 3  # (10-5)-2 = 3
        # Left-to-right for division
        assert self.parser.parse("20/4/5") == 1  # (20/4)/5 = 1
    
    def test_large_numbers(self):
        """Test handling of large numbers."""
        result = self.parser.parse("1000000*1000000")
        assert result == 1e12
        
        result = self.parser.parse("999999+1")
        assert result == 1000000
    
    def test_small_numbers(self):
        """Test handling of small decimal numbers."""
        result = self.parser.parse("0.001*0.001")
        assert result == pytest.approx(0.000001)
        
        result = self.parser.parse("0.1+0.2")
        assert result == pytest.approx(0.3)