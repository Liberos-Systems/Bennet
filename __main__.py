#!/usr/bin/env python3
import sys
from yard import Yard

if __name__ == "__main__":
    yard = Yard()
    function_name = sys.argv[1]
    function = getattr(yard, function_name, None)
    if function:
        function()
    else:
        print(f"No such function: {function_name}")
