import os
import json
from rich import print
from config import debug
from icecream import ic

from data.field import Field
from dataclasses import asdict

class Json:
    def __init__(self, filesystem):
        self.filesystem = filesystem
        self.data = {"root": {}}

    def insert_project_data(self, project):
        if project:
            for field in project:
                self.data["root"][field[1].name] = field[1].value

    def save(self, filename):
        filename = os.path.join(self.filesystem.root_, filename)
        if os.path.exists(filename) and debug:
            ic(f"[Warning] Overwriting existing file: {filename}")
        
        with open(filename, "w") as f:
            json.dump(self.data, f, indent=4)
        if debug:
            ic(f"Saved data to: {filename}")

    def load(self, filename):
        filename = os.path.join(self.filesystem.root_, filename)
        if not os.path.exists(filename) and debug:
            ic(f"[Error] File does not exist: {filename}")
            return
        with open(filename, "r") as f:
            self.data = json.load(f)
        if debug:
            ic(f"Loaded data from: {filename}")

    def get_data(self, key):
        data = self.data["root"].get(key)

        if data is None and debug:
            ic("[Warning] Key does not exist in data.")
            return None

        return {id: data} if isinstance(data, dict) else data

    def add_data(self, key, value):
        if key in self.data["root"] and debug:
            ic("[Warning] Overwriting existing key in data.")
        self.data["root"][key] = value

    def remove_data(self, key):
        if key not in self.data["root"] and debug:
            ic("[Error] Key does not exist in data.")
            return
        del self.data["root"][key]

    def update_data(self, key, value):
        if key not in self.data["root"] and debug:
            ic("[Error] Key does not exist in data.")
            return
        self.data["root"][key] = value

    def sort_data(self, key):
        if key not in self.data["root"] and debug:
            ic("[Error] Key does not exist in data.")
            return
        self.data["root"] = dict(sorted(self.data["root"].items(), key=lambda x: x[1][key]))

    def generate_report(self):
        if debug:
            for key, value in self.data["root"].items():
                ic(f"{key}: {value}")

    def display_json_tree(self, data, indent=0):
        for key, value in data.items():
            print('\t' * indent + str(key))
            if isinstance(value, dict):
                self.display_json_tree(value, indent+1)
            else:
                print('\t' * (indent+1) + str(value))
