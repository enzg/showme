#!/usr/bin/env python3
"""Calculator entry point with CLI and GUI support."""

import sys
import argparse
from calculator.ui import run_calculator


def main() -> None:
    """Main entry point for the calculator."""
    parser = argparse.ArgumentParser(
        description="Calculator with CLI and GUI interfaces"
    )
    parser.add_argument(
        "--gui",
        action="store_true",
        help="Launch GUI interface (default: CLI)"
    )
    parser.add_argument(
        "--cli",
        action="store_true",
        help="Force CLI interface"
    )
    
    args = parser.parse_args()
    
    # If GUI is requested or no specific mode is set, try GUI
    if args.gui or (not args.cli and not sys.stdin.isatty()):
        try:
            import tkinter
            from calculator.gui import main as gui_main
            gui_main()
        except ImportError:
            print("Error: Tkinter not available. Falling back to CLI mode.")
            run_calculator()
    else:
        # Default to CLI
        run_calculator()


if __name__ == "__main__":
    main()