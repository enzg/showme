# Initial Feature Request: Build a Basic Command-Line Calculator

## FEATURE
Develop a simple command-line calculator in Python that supports addition (+), subtraction (-), multiplication (*), and division (/). 
- User inputs: two numbers and an operator.
- Handle errors: invalid operators, non-numeric inputs, division by zero.
- Loop for multiple calculations until user quits with 'q'.
- Output results clearly, e.g., "3 + 4 = 7".

## EXAMPLES
Reference examples/cli_patterns/cli_basic_input.py for input loop patterns.
Reference examples/error_handling/div_zero.py for division error handling.

## DOCUMENTATION
- Use Python's built-in input() and float() for parsing.
- Follow PEP8: https://peps.python.org/pep-0008/
- For testing, use pytest: https://docs.pytest.org/en/stable/

## OTHER CONSIDERATIONS
- Make it user-friendly: add a help menu with 'h'.
- Ensure code is modular for future GUI extension.
- Success criteria: Passes tests for all operations and errors.