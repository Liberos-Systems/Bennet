import os
import json
from rich import print
from config import debug

class Json:
    def __init__(self, filename):
        self.filename = filename
        self.data = {}

    def save(self):
        if os.path.exists(self.filename) and debug:
            print("[Warning] Overwriting existing file.")
        with open(self.filename, "w") as f:
            json.dump(self.data, f)

    def load(self):
        if not os.path.exists(self.filename) and debug:
            print("[Error] File does not exist.")
            return
        with open(self.filename, "r") as f:
            self.data = json.load(f)

    def get_data(self, key):
        data = self.data.get(key)

        if data is None and debug:
            print("[Warning] Key does not exist in data.")
            return None

        return {id: data} if isinstance(data, dict) else data

    def add_data(self, key, value):
        if key in self.data and debug:
            print("[Warning] Overwriting existing key in data.")
        self.data[key] = value

    def remove_data(self, key):
        if key not in self.data and debug:
            print("[Error] Key does not exist in data.")
            return
        del self.data[key]

    def update_data(self, key, value):
        if key not in self.data and debug:
            print("[Error] Key does not exist in data.")
            return
        self.data[key] = value

    def sort_data(self, key):
        if key not in self.data and debug:
            print("[Error] Key does not exist in data.")
            return
        self.data = sorted(self.data.items(), key=lambda x: x[1][key])

    def generate_report(self):
        if debug:
            for key, value in self.data.items():
                print(f"{key}: {value}")

    def display_json_tree(self):
        def display_dict(d, indent=0):
            for key, value in d.items():
                print(' ' * indent + str(key))
                if isinstance(value, dict):
                    display_dict(value, indent+4)

        display_dict(self.data)

