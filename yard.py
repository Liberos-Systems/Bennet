#!/usr/bin/env python3
from rich import print
from config import version, debug
from filesystem.filesystem import FileSystemManager
from icecream import ic

class Yard:
    def __init__(self):
        print(f"YARD version: {version}")
        self.fs = FileSystemManager()
        ic(self.fs.root_) if debug else None
        
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
        ic("yard.json file does not exist in the current directory.") if not self.fs.file_exists(yard_file) and debug else ic("yard.json file exists in the current directory.") if debug else None

    def add(self):
        ic("Add function called") if debug else None

    def delete(self):
        ic("Delete function called") if debug else None

    def help(self):
        ic("Help function called") if debug else None

