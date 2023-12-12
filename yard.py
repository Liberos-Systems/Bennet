#!/usr/bin/env python3
from rich import print
from config import version, debug
from filesystem.filesystem import FileSystemManager

class Yard:
    def __init__(self):
        print(f"YARD version: {version}")
        self.fs = FileSystemManager()
        print(self.fs.root_)
        
        if debug:
            #print(self.fs.pwd())
            self.root_dir = "./yard_develop_space"
            if self.fs.file_exists(self.root_dir):
                self.fs.rmdir(self.root_dir)
            
            self.fs.mkdir(self.root_dir)
            
            print(self.root_dir)
            self.fs.cd(self.root_dir)
            print(self.fs.pwd())


    def init(self):
        yard_file = "yard.json"
        if not self.fs.file_exists(yard_file):
            print("yard.json file does not exist in the current directory.")
        else:
            print("yard.json file exists in the current directory.")

    def add(self):
        print("Add function called")

    def delete(self):
        print("Delete function called")

    def help(self):
        print("Help function called")

