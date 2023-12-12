#!/usr/bin/env python3
from rich import print
from config import version, debug
from filesystem.filesystem import FileSystemManager

class Yard:
    def __init__(self):
        print(f"YARD version: {version}")
        self.fs = FileSystemManager()
        if debug: print(self.fs.root_)
        
        if debug:
            self.root_dir = "./yard_develop_space"
            if self.fs.file_exists(self.root_dir):
                self.fs.rmdir(self.root_dir)
            
            self.fs.mkdir(self.root_dir)
            
            self.fs.cd(self.root_dir)

        else:
            print("no debug")


    def init(self):
        yard_file = "yard.json"
        if not self.fs.file_exists(yard_file):
            if debug: print("yard.json file does not exist in the current directory.")
        else:
            if debug: print("yard.json file exists in the current directory.")

    def add(self):
        if debug: print("Add function called")

    def delete(self):
        if debug: print("Delete function called")

    def help(self):
        if debug: print("Help function called")

