import os
import json
from pathlib import Path
from filesystem import FileSystemManager
from rich.prompt import Prompt
from package import Package
from config import debug
from icecream import ic

class Workspace:
    def __init__(self):
        self.fs = FileSystemManager()
        self.package = Package(self.path / 'package.json')

        if not self.path.exists():
            self.fs.mkdir(self.path)
            self.package.create_new_package_file_json()
            ic(f"Created new package.json at {self.path}")
        elif (self.path / 'package.json').exists():
            self.package.load_package_json()
            ic(f"Loaded package.json from {self.path}")

    def run_script(self):
        script_name = Prompt.ask("Enter the script name: ")
        if script_name in self.package.scripts:
            os.system(self.package.scripts[script_name])
            ic(f"Running script {script_name}")

