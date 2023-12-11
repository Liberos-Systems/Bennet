import os
import json
from rich.prompt import Prompt

class Package:
    def __init__(self, package_path):
        self.package_path = package_path
        if os.path.exists(self.package_path):
            self.load_package_json()
        else:
            self.create_new_package_file_json()

    def add_new_field(self, field_name, field_content):
        setattr(self, field_name, field_content)
        self.save_package_json()  # Save changes to json file after adding new field

    def load_package_json(self):
        with open(self.package_path, 'r') as json_file:
            package_data = json.load(json_file)
            for key, value in package_data.items():
                if isinstance(value, dict):
                    for sub_key, sub_value in value.items():
                        setattr(self, sub_key, sub_value)
                else:
                    setattr(self, key, value)

    def create_new_package_file_json(self):
        self.name = Prompt.ask("question name: ", default=os.path.basename(os.getcwd()))
        self.version = Prompt.ask("question version (1.0.0): ", default="1.0.0")
        self.description = Prompt.ask("question description: ")
        self.main = Prompt.ask("question entry point (index.js): ", default="index.js")
        self.repository_url = Prompt.ask("question repository url: ")
        self.author = Prompt.ask("question author: ")
        self.license = Prompt.ask("question license (MIT): ", default="MIT")
        self.private = Prompt.ask("question private: ", default=False)
        self.build = ""
        self.dependencies = {}
        self.scripts = {}
        self.buildsystem = ""
        self.save_package_json()
        print("Created package.json")

    def save_package_json(self):
        package_data = {attr: getattr(self, attr) for attr in self.__dict__}
        with open(self.package_path, 'w') as json_file:
            json.dump(package_data, json_file, indent=4)

    def print_attributes(self):
        for attr, value in self.__dict__.items():
            if isinstance(value, str):
                print(f"{attr}: {value}")
            else:
                for sub_attr, sub_value in value.items():
                    print(f"{attr}.{sub_attr}: {sub_value}")
