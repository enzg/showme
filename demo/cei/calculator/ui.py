from typing import Optional
from calculator.core import calculate, get_operations

def display_welcome() -> None:
    """Display welcome message and instructions."""
    print("=" * 50)
    print("Welcome to Command-Line Calculator")
    print("=" * 50)
    print("Commands:")
    print("  - Enter two numbers and an operator to calculate")
    print("  - 'h' or 'help' - Show help menu")
    print("  - 'q' or 'quit' - Exit calculator")
    print("=" * 50)

def display_help() -> None:
    """Display help information."""
    operations = get_operations()
    print("\nHelp Menu:")
    print("-" * 30)
    print("Available operations:")
    for op in operations:
        print(f"  {op} - {operations[op].__doc__}")
    print("\nUsage:")
    print("  1. Enter first number")
    print("  2. Enter operator (+, -, *, /)")
    print("  3. Enter second number")
    print("  4. View result")
    print("\nCommands:")
    print("  'h' or 'help' - Show this menu")
    print("  'q' or 'quit' - Exit calculator")
    print("-" * 30)

def get_number(prompt: str) -> Optional[float]:
    """Get a valid number from user input."""
    while True:
        user_input = input(prompt).strip()
        if user_input.lower() in ('q', 'quit'):
            return None
        try:
            return float(user_input)
        except ValueError:
            print("Invalid number. Please try again or 'q' to quit.")

def get_operator() -> Optional[str]:
    """Get a valid operator from user input."""
    operations = get_operations()
    valid_ops = list(operations.keys())
    prompt = f"Enter operator ({', '.join(valid_ops)}): "
    
    while True:
        user_input = input(prompt).strip()
        if user_input.lower() in ('q', 'quit'):
            return None
        if user_input in valid_ops:
            return user_input
        print(f"Invalid operator. Valid operators: {', '.join(valid_ops)}")

def format_result(num1: float, num2: float, operator: str, result: float) -> str:
    """Format calculation result for display."""
    # Format numbers to remove unnecessary decimal places
    num1_str = f"{num1:.10g}"
    num2_str = f"{num2:.10g}"
    result_str = f"{result:.10g}"
    return f"{num1_str} {operator} {num2_str} = {result_str}"

def run_calculator() -> None:
    """Main calculator loop - redirects to enhanced CLI."""
    # Import here to avoid circular imports
    from calculator.cli import run_enhanced_calculator
    run_enhanced_calculator()