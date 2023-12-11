#!/usr/bin/env python3
from rich import print
from __main__ import version

class Yard:
    def __init__(self):
        print(f"YARD version: {version}")

    def add(self):
        print("Add function called")

    def delete(self):
        print("Delete function called")

    def help(self):
        print("Help function called")
