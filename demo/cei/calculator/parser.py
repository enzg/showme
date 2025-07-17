"""
Expression parser for calculator without using eval().
Implements tokenization, infix to postfix conversion, and evaluation.
"""
from typing import List, Union, Optional, Tuple
from enum import Enum
import re
from calculator.core import add, subtract, multiply, divide


class TokenType(Enum):
    """Types of tokens in expressions."""
    NUMBER = "NUMBER"
    OPERATOR = "OPERATOR"
    LEFT_PAREN = "LEFT_PAREN"
    RIGHT_PAREN = "RIGHT_PAREN"


class Token:
    """Represents a token in the expression."""
    
    def __init__(self, type_: TokenType, value: Union[str, float]):
        self.type = type_
        self.value = value
    
    def __repr__(self):
        return f"Token({self.type}, {self.value})"


class ExpressionParser:
    """
    Parses and evaluates mathematical expressions without using eval().
    Supports +, -, *, / operators and parentheses.
    Follows PEMDAS order of operations.
    """
    
    def __init__(self):
        self.operators = {
            '+': (1, add),
            '-': (1, subtract),
            '*': (2, multiply),
            '/': (2, divide)
        }
    
    def tokenize(self, expression: str) -> List[Token]:
        """
        Convert expression string into list of tokens.
        
        Args:
            expression: Mathematical expression string
            
        Returns:
            List of Token objects
            
        Raises:
            ValueError: If expression contains invalid characters
        """
        tokens = []
        expression = expression.replace(' ', '')  # Remove whitespace
        
        # Pattern to match numbers (including decimals) and operators
        pattern = r'(\d+\.?\d*|[+\-*/()])'
        matches = re.findall(pattern, expression)
        
        # Verify we captured the entire expression
        if ''.join(matches) != expression:
            raise ValueError("Invalid characters in expression")
        
        for match in matches:
            if match in self.operators:
                tokens.append(Token(TokenType.OPERATOR, match))
            elif match == '(':
                tokens.append(Token(TokenType.LEFT_PAREN, match))
            elif match == ')':
                tokens.append(Token(TokenType.RIGHT_PAREN, match))
            else:
                # It's a number
                try:
                    value = float(match)
                    tokens.append(Token(TokenType.NUMBER, value))
                except ValueError:
                    raise ValueError(f"Invalid number: {match}")
        
        return tokens
    
    def infix_to_postfix(self, tokens: List[Token]) -> List[Token]:
        """
        Convert infix notation to postfix notation using Shunting Yard algorithm.
        
        Args:
            tokens: List of tokens in infix notation
            
        Returns:
            List of tokens in postfix notation
            
        Raises:
            ValueError: If parentheses are mismatched
        """
        output = []
        operator_stack = []
        
        for token in tokens:
            if token.type == TokenType.NUMBER:
                output.append(token)
            
            elif token.type == TokenType.OPERATOR:
                # Pop operators with higher or equal precedence
                while (operator_stack and 
                       operator_stack[-1].type == TokenType.OPERATOR and
                       self.operators[operator_stack[-1].value][0] >= self.operators[token.value][0]):
                    output.append(operator_stack.pop())
                operator_stack.append(token)
            
            elif token.type == TokenType.LEFT_PAREN:
                operator_stack.append(token)
            
            elif token.type == TokenType.RIGHT_PAREN:
                # Pop until we find the matching left parenthesis
                while operator_stack and operator_stack[-1].type != TokenType.LEFT_PAREN:
                    output.append(operator_stack.pop())
                
                if not operator_stack:
                    raise ValueError("Mismatched parentheses: extra closing parenthesis")
                
                # Pop the left parenthesis
                operator_stack.pop()
        
        # Pop remaining operators
        while operator_stack:
            if operator_stack[-1].type == TokenType.LEFT_PAREN:
                raise ValueError("Mismatched parentheses: unclosed opening parenthesis")
            output.append(operator_stack.pop())
        
        return output
    
    def evaluate_postfix(self, tokens: List[Token]) -> float:
        """
        Evaluate expression in postfix notation.
        
        Args:
            tokens: List of tokens in postfix notation
            
        Returns:
            Result of the expression
            
        Raises:
            ValueError: If expression is invalid
            ZeroDivisionError: If division by zero occurs
        """
        stack = []
        
        for token in tokens:
            if token.type == TokenType.NUMBER:
                stack.append(token.value)
            
            elif token.type == TokenType.OPERATOR:
                if len(stack) < 2:
                    raise ValueError("Invalid expression: not enough operands")
                
                # Pop two operands (note the order)
                b = stack.pop()
                a = stack.pop()
                
                # Get the operation function
                _, operation = self.operators[token.value]
                
                # Special handling for division by zero
                if token.value == '/' and b == 0:
                    raise ZeroDivisionError("Division by zero")
                
                result = operation(a, b)
                if result is None:  # Handle division by zero from core.py
                    raise ZeroDivisionError("Division by zero")
                
                stack.append(result)
        
        if len(stack) != 1:
            raise ValueError("Invalid expression: too many operands")
        
        return stack[0]
    
    def parse(self, expression: str) -> float:
        """
        Parse and evaluate a mathematical expression.
        
        Args:
            expression: Mathematical expression string
            
        Returns:
            Result of the expression
            
        Raises:
            ValueError: If expression is invalid
            ZeroDivisionError: If division by zero occurs
        """
        if not expression or expression.isspace():
            raise ValueError("Empty expression")
        
        # Tokenize the expression
        tokens = self.tokenize(expression)
        
        if not tokens:
            raise ValueError("Empty expression")
        
        # Convert to postfix notation
        postfix = self.infix_to_postfix(tokens)
        
        # Evaluate the postfix expression
        return self.evaluate_postfix(postfix)
    
    def validate_expression(self, expression: str) -> Tuple[bool, Optional[str]]:
        """
        Validate an expression without evaluating it.
        
        Args:
            expression: Mathematical expression string
            
        Returns:
            Tuple of (is_valid, error_message)
        """
        try:
            tokens = self.tokenize(expression)
            self.infix_to_postfix(tokens)
            return True, None
        except Exception as e:
            return False, str(e)