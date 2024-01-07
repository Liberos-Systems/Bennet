#!/usr/bin/env python3
import sys
import argparse
from bennet import Bennet
from rich import print
from common.config import debug
from common.common import ic

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Bennet is a tool inspired by Yarn, designed specifically for building Linux projects in C/C++, Python, JavaScript, and GTK environments. It seamlessly manages workspaces, packages, and builds for diverse language and build system combinations.")
    parser.add_argument("operation", choices=['build', 'update', 'install', 'init', 'help'], nargs='?', default='init', help="Operation to perform")
    args = parser.parse_args()
    
    bennet = Bennet()
    operation = args.operation
    
    if operation == 'build':
        bennet.build()
    elif operation == 'update':
        bennet.updated()
    elif operation == 'install':
        bennet.install()
    elif operation == 'init':
        bennet.init()
    elif operation == 'help':
        bennet.help()
    else:
        if not debug: 
            ic("No valid operation provided in command line arguments.")


