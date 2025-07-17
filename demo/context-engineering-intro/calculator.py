#!/usr/bin/env python3
"""Main calculator application."""

import sys
from typing import NoReturn

import core
import ui


def main() -> NoReturn:
    """Run the calculator application."""
    ui.display_welcome()
    
    while True:
        try:
            # Get numbers from user
            num1, num2, status = ui.get_numbers()
            
            if status == 'quit':
                print("\nGoodbye!")
                sys.exit(0)
            elif status == 'help':
                ui.display_help()
                continue
            elif status is not None:  # Error message
                ui.display_error(status)
                continue
                
            # Get operator from user
            operator, status = ui.get_operator()
            
            if status == 'quit':
                print("\nGoodbye!")
                sys.exit(0)
            elif status == 'help':
                ui.display_help()
                continue
            elif status is not None:  # Error message
                ui.display_error(status)
                continue
                
            # Perform calculation
            success, result = core.calculate(num1, num2, operator)
            
            if success:
                ui.display_result(num1, num2, operator, result)
            else:
                ui.display_error(result)
                
        except KeyboardInterrupt:
            print("\n\nInterrupted. Goodbye!")
            sys.exit(0)
        except Exception as e:
            ui.display_error(f"Unexpected error: {type(e).__name__}")


if __name__ == "__main__":
    main()