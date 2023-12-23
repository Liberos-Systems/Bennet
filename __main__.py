#!/usr/bin/env python3
import sys
from bennet import Bennet
from rich import print
from config import debug
from icecream import ic

if __name__ == "__main__":
    bennet = Bennet()
    if len(sys.argv) > 1:
        function_name = sys.argv[1]
        function = getattr(bennet, function_name, None)
        if function:
            function()
        else:
            if not debug:
                ic(f"No such function: {function_name}")
            
    else:
        if not debug: 
            ic("No function name provided in command line arguments.")

