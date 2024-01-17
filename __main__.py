#!/usr/bin/env python3
import sys
import argparse
from bennet import Bennet
from rich import print
from common.config import debug
from common.common import ic

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Bennet is a tool inspired by Yarn, designed specifically for building Linux projects in C/C++, Python, JavaScript, and GTK environments. It seamlessly manages workspaces, packages, and builds for diverse language and build system combinations.")
    parser.add_argument("operation", nargs='?', help="Operation to perform")
    parser.add_argument("extra_args", nargs=argparse.REMAINDER, help="Extra arguments for the operation")
    args = parser.parse_args()
    
    bennet = Bennet()
    operation = args.operation if args.operation else 'init'
    
    if operation == 'build':
        bennet.build(*args.extra_args)
    elif operation == 'update':
        bennet.update(*args.extra_args)
    elif operation == 'install':
        bennet.install(*args.extra_args)
    elif operation == 'init':
        bennet.init(*args.extra_args)
    elif operation == 'help':
        bennet.help(*args.extra_args)
    else:
        bennet.script(operation, *args.extra_args)


