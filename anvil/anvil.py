from models.classes.anvil_base import AnvilBase
from hodges.json.json_class import Json
from hodges.file_system.file_system_class import FileSystemManager
from common.common import ic
from common.config import debug
from rich.prompt import Prompt

class Anvil(AnvilBase):
    def __init__(self, filesystem, root="root", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filesystem = FileSystemManager()
        self.root = root
        self.data = {self.root: {}}
        self.project = None
        self.project_file = "./project.bennet.json"

        #self.anvilJson = Json(self.fs)
        #self.anvilJson.change_root(root)

        if debug:
            print("----- Displaying All Items -----")
            self.display_all_items()
            print("----- End of All Items -----")
            print("----- Displaying __dict__ -----")
            ic(self.__dict__)
            print("----- End of __dict__ -----")
            print("----- Displaying scripts[0].__dict__ -----")
            ic(self.scripts[0].__dict__)
            print("----- End of scripts[0].__dict__ -----")
            print("----- Displaying repository.__dict__ -----")
            ic(self.repository.__dict__)
            print("----- End of repository.__dict__ -----")
        
    def change_root(self, new_root):
        old_data = self.data[self.root]
        self.root = new_root
        self.data = {self.root: old_data}
        self.anvilJson.change_root(new_root)

    def init(self):
        self.interactive_init()
        self.anvilJson.insert_project_data(self.project)


    def interactive_init(self):
        for key, value in self.__dict__.items():
            if isinstance(value, (dict, list)):
                continue
            prompt = f"Should I overwrite the value of {key}? (Y/N): "
            overwrite = Prompt.ask(prompt, default="N")
            if overwrite.lower() == "y":
                self.project.name.value = Prompt.ask(f"Enter the new value for {key}: ", default=value)

        self.anvilJson.save(self.filesystem.combine_paths(self.filesystem.root_, self.project_file))
        self.anvilJson.load(self.filesystem.combine_paths(self.filesystem.root_, self.project_file))
        if self.filesystem.exists(self.filesystem.combine_paths(self.filesystem.root_, self.project_file)) and debug:
            ic(f"[Warning] File already exists: {self.filesystem.combine_paths(self.filesystem.root_, self.project_file)}")
            return
    def display_all_items(self):
        for key, value in self.__dict__.items():
            print(f"{key}: {value}")


