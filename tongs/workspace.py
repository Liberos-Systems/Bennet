import os
import json
from pathlib import Path
from filesystem import FileSystemManager
from rich.prompt import Prompt
from package import Package
from config import debug
from common.common import ic

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

    def run(self):
        workspaces = self.package.workspaces
        for index, workspace in enumerate(workspaces, start=1):
            print(f"{index}. {workspace}")
        workspace_index = Prompt.ask("Enter the number of the workspace you want to select: ", int)
        selected_workspace = workspaces[workspace_index - 1]
        ic(f"Selected workspace: {selected_workspace}")

    def focus(self):
        workspace_name = Prompt.ask("Enter the workspace name: ")
        if workspace_name in self.package.workspaces:
            os.system(f"yarn workspace {workspace_name} install")
            ic(f"Installing workspace {workspace_name} and its dependencies")

    def foreach(self):
        command = Prompt.ask("Enter the command to run on all workspaces: ")
        os.system(f"yarn workspaces foreach {command}")
        ic(f"Running command {command} on all workspaces")

    def list(self):
        os.system("yarn workspaces list")
        ic("Listing all available workspaces")

