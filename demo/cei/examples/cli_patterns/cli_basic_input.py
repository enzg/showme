#!/usr/bin/env python3
"""Basic CLI calculator with continuous input loop and error handling."""

def get_number(prompt: str) -> float:
    """Get a valid number from user input."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number. Please try again.")

def calculate(num1: float, num2: float, operation: str) -> float:
    """Perform calculation based on operation."""
    operations = {'+': num1 + num2, '-': num1 - num2, 
                  '*': num1 * num2, '/': num1 / num2}
    if operation not in operations:
        raise ValueError(f"Invalid operation: {operation}")
    return operations[operation]

def main() -> None:
    """Main calculator loop."""
    print("Simple Calculator (type 'quit' to exit)")
    while True:
        try:
            command = input("\nEnter 'calculate' or 'quit': ").strip().lower()
            if command in ('quit', 'exit'):
                print("Goodbye!")
                break
            elif command == 'calculate':
                num1 = get_number("Enter first number: ")
                op = input("Enter operation (+, -, *, /): ").strip()
                num2 = get_number("Enter second number: ")
                result = calculate(num1, num2, op)
                print(f"Result: {num1} {op} {num2} = {result}")
            else:
                print("Invalid command. Try 'calculate' or 'quit'.")
        except ZeroDivisionError:
            print("Error: Cannot divide by zero!")
        except ValueError as e:
            print(f"Error: {e}")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break

if __name__ == "__main__":
    main()