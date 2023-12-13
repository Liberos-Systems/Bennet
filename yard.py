#!/usr/bin/env python3
from rich import print
from config import version, debug
from filesystem.filesystem import FileSystemManager
from icecream import ic
from yardjson.json import Json
from rich.prompt import Prompt
from data.structures.project import Project

class Yard:
    def __init__(self):
        print(f"YARD version: {version}")
        self.fs = FileSystemManager()

        self.project = Project()
        self.projectJson = Json(self.fs)

        #self.lockJson = Json(self.fs.root_dir / "lock.yard")
        ic(self.fs.root_) if debug else None
        
        if debug:
            self.root_dir = "./yard_develop_space"
            print(self.root_dir)
            print("------------------------")
            if self.fs.file_exists(self.root_dir):
                self.fs.rmdir(self.root_dir)
            
            if(self.fs.mkdir(self.root_dir)):
                self.fs.cd(self.root_dir)

            self.init()

        else:
            print("no debug")


    def init(self):
        self.interactive_init()
        self.projectJson.insert_project_data(self.project)
        self.projectJson.display_json_tree(self.projectJson.data)
        self.projectJson.save("./project.yard.json")
        #self.lock.save()

    def interactive_init(self):
        self.project.name.value = Prompt.ask("Enter the project name: ", default=self.project.name.default_value)
        self.project.version.value = Prompt.ask("Enter the project version: ", default=self.project.version.default_value)
        self.project.description.value = Prompt.ask("Enter the project description: ", default=self.project.description.default_value)
        self.project.main.value = Prompt.ask("Enter the main file: ", default=self.project.main.default_value)
        self.project.author.value = Prompt.ask("Enter the author name: ", default=self.project.author.default_value)
        self.project.license.value = Prompt.ask("Enter the license: ", default=self.project.license.default_value)

    def add(self):
        ic("Add function called") if debug else None

    def delete(self):
        ic("Delete function called") if debug else None

    def help(self):
        ic("Help function called") if debug else None

