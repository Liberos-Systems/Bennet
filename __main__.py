#!/usr/bin/env python3
import sys
from yard import Yard
from rich import print

version = "0.0.2"

if __name__ == "__main__":
    yard = Yard()
    if len(sys.argv) > 1:
        function_name = sys.argv[1]
        function = getattr(yard, function_name, None)
        if function:
            function()
        else:
            print(f"No such function: {function_name}")
    else:
        print("No function name provided in command line arguments.")

