from common.config import debug
from common.common import ic
import os
import json
from rich import print

class Json:
    def __init__(self, filesystem, root="root"):
        self.filesystem = filesystem
        self.root = root
        self.data = {self.root: {}}

    def change_root(self, new_root):
        old_data = self.data[self.root]
        self.root = new_root
        self.data = {self.root: old_data}

    def insert_init_data(self, project):
        for key, value in project.items():
            ic(key, value)
            self.data[self.root][key] = value

    def save(self, filename):
        print(filename)
        filename = self.filesystem.combine_paths(self.filesystem.root_, filename)
        
        if os.path.exists(filename) and debug:
            ic(f"[Warning] Overwriting existing file: {filename}")
        
        with open(filename, "w") as f:
            json.dump(self.data, f, indent=4)
            
        if debug:
            ic(f"Saved data to: {filename}")

    def load(self, filename):
        filename = self.filesystem.combine_paths(self.filesystem.root_, filename)
        if not os.path.exists(filename) and debug:
            ic(f"[Error] File does not exist: {filename}")
            return
        with open(filename, "r") as f:
            self.data = json.load(f)
        if debug:
            ic(f"Loaded data from: {filename}")

    def get_data(self, key):
        data = self.data[self.root].get(key)

        if data is None and debug:
            ic("[Warning] Key does not exist in data.")
            return None

        return {id: data} if isinstance(data, dict) else data

    def add_data(self, key, value):
        if key in self.data[self.root] and debug:
            ic("[Warning] Overwriting existing key in data.")
        self.data[self.root][key] = value

    def remove_data(self, key):
        if key not in self.data[self.root] and debug:
            ic("[Error] Key does not exist in data.")
            return
        del self.data[self.root][key]

    def update_data(self, key, value):
        if key not in self.data[self.root] and debug:
            ic("[Error] Key does not exist in data.")
            return
        self.data[self.root][key] = value

    def sort_data(self, key):
        if key not in self.data[self.root] and debug:
            ic("[Error] Key does not exist in data.")
            return
        self.data[self.root] = dict(sorted(self.data[self.root].items(), key=lambda x: x[1][key]))

    def display_json_tree(self, data=None, indent=0):
        if data is None:
            data = self.data[self.root]
        for key, value in data.items():
            print('\t' * indent + str(key))
            if isinstance(value, dict):
                self.display_json_tree(value, indent+1)
            else:
                print('\t' * (indent+1) + str(value))
