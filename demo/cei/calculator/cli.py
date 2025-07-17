"""
Enhanced CLI interface for calculator with expression parsing support.
"""
from typing import Optional
from calculator.core import calculate, get_operations
from calculator.parser import ExpressionParser
from calculator.history import HistoryManager
from calculator.ui import (
    display_welcome, display_help, get_number, get_operator, 
    format_result
)


def display_enhanced_help() -> None:
    """Display enhanced help information."""
    display_help()
    print("\nEnhanced Features:")
    print("-" * 30)
    print("Expression Mode:")
    print("  Enter complete expressions like '3+4*2'")
    print("  Supports parentheses: '(3+4)*2'")
    print("  Type 'expr' to toggle expression mode")
    print("\nHistory Commands:")
    print("  'history' or 'hist' - Show calculation history")
    print("  'clear history' - Clear all history")
    print("-" * 30)


def run_enhanced_calculator() -> None:
    """Run the enhanced calculator with expression parsing."""
    parser = ExpressionParser()
    history = HistoryManager(max_entries=50)
    expression_mode = True  # Default to expression mode
    
    # Display welcome with mode info
    display_welcome()
    print(f"\nMode: {'Expression' if expression_mode else 'Step-by-step'}")
    print("Type 'expr' to toggle modes, 'h' for help\n")
    
    while True:
        try:
            # Get user input
            if expression_mode:
                user_input = input("Enter expression (or command): ").strip()
            else:
                user_input = input("Enter command (or press Enter to calculate): ").strip()
            
            # Handle commands
            lower_input = user_input.lower()
            
            if lower_input in ('q', 'quit', 'exit'):
                print("Thank you for using Calculator. Goodbye!")
                break
            
            elif lower_input in ('h', 'help'):
                display_enhanced_help()
                continue
            
            elif lower_input == 'expr':
                expression_mode = not expression_mode
                print(f"\nSwitched to {'Expression' if expression_mode else 'Step-by-step'} mode\n")
                continue
            
            elif lower_input in ('history', 'hist'):
                print("\n" + history.format_history_display(limit=10))
                continue
            
            elif lower_input == 'clear history':
                confirm = input("Clear all history? (y/n): ").lower()
                if confirm == 'y':
                    history.clear_history()
                    print("History cleared.\n")
                continue
            
            # Handle calculation based on mode
            if expression_mode and user_input and not user_input.isspace():
                # Expression mode - parse and evaluate
                try:
                    result = parser.parse(user_input)
                    result_str = f"{result:.10g}"
                    print(f"Result: {user_input} = {result_str}\n")
                    
                    # Add to history
                    history.add_entry(user_input, result)
                    
                except ZeroDivisionError:
                    print("Error: Cannot divide by zero!\n")
                except Exception as e:
                    print(f"Error: {e}\n")
            
            elif not expression_mode:
                # Step-by-step mode (original functionality)
                # Get first number
                num1 = get_number("Enter first number: ")
                if num1 is None:
                    print("Thank you for using Calculator. Goodbye!")
                    break
                
                # Get operator
                operator = get_operator()
                if operator is None:
                    print("Thank you for using Calculator. Goodbye!")
                    break
                
                # Get second number
                num2 = get_number("Enter second number: ")
                if num2 is None:
                    print("Thank you for using Calculator. Goodbye!")
                    break
                
                # Perform calculation
                result = calculate(num1, num2, operator)
                
                if result is None:
                    print("Error: Cannot divide by zero!\n")
                else:
                    expression = format_result(num1, num2, operator, result)
                    print(f"\nResult: {expression}\n")
                    
                    # Add to history
                    history.add_entry(f"{num1:.10g}{operator}{num2:.10g}", result)
                
        except KeyboardInterrupt:
            print("\n\nInterrupted. Thank you for using Calculator. Goodbye!")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            print("Please try again.\n")