#!/usr/bin/env python3
import sys
from bennet import Bennet
from rich import print
from common.config import debug
from common.common import ic

if __name__ == "__main__":
    bennet = Bennet()
    if len(sys.argv) > 1:
        function_name = sys.argv[1]
        if function_name in ['-h', 'help']:
            bennet.help()
        else:
            function = getattr(bennet, function_name, None)
            if function:
                function()
            else:
                if not debug:
                    ic(f"No such function: {function_name}")
            
    else:
        if not debug: 
            ic("No function name provided in command line arguments.")

