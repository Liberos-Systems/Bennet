from models.classes.anvil_base import AnvilBase
from hodges.json.json_class import Json
from hodges.file_system.file_system_class import FileSystemManager
from common.common import ic
from common.config import debug
from rich.prompt import Prompt

class Anvil(AnvilBase):
    def __init__(self, filesystem, root="root", project_name="./project.bennet.json", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filesystem = filesystem
        self.root = root
        self.data = {self.root: {}}
        self.project = None
        self.project_file = project_name

        self.anvilJson = Json(self.filesystem, root=root)

        if debug:
            ic("----- Displaying All Items -----")
            self.display_all_items()
            ic("----- End of All Items -----")
            ic("----- Displaying __dict__ -----")
            ic(self.__dict__)
            ic("----- End of __dict__ -----")
            ic("----- Displaying scripts[0].__dict__ -----")
            ic(self.scripts[0].__dict__)
            ic("----- End of scripts[0].__dict__ -----")
            ic("----- Displaying repository.__dict__ -----")
            ic(self.repository.__dict__)
            ic("----- End of repository.__dict__ -----")
        
    def change_root(self, new_root):
        old_data = self.data[self.root]
        self.root = new_root
        self.data = {self.root: old_data}
        self.anvilJson.change_root(new_root)

    def init(self):
        self.interactive_init()

    def interactive_init(self):
        if debug: 
            ic("interactive_init")
            ic(self._properties.items())

        for key, obj in self._properties.items():
            if obj is not None:
                if not str(obj).startswith('<anvil_base/'):
                    value = obj.value if hasattr(obj, 'value') else obj
                    prompt = f"Current value of {key}: [red]{value}[/red]. Should I overwrite the value of {key}? (Y/N): "
                    overwrite = Prompt.ask(prompt, default="N")
                    if overwrite.lower() == "y":
                        new_value = Prompt.ask(f"Enter the new value for {key}: ", default=str(value))
                        if hasattr(obj, 'value'):
                            obj.value = new_value
                        else:
                            self._properties[key] = new_value
        
        # Save properties that are not Anvilbase to json file after changes
        non_anvilbase_properties = {k: str(v) for k, v in self._properties.items() if not str(v).startswith('<anvil_base/')}
        self.anvilJson.insert_init_data(non_anvilbase_properties)
        self.anvilJson.save(str(self.project_file))
        
    def display_all_items(self):
        for key, value in self.__dict__.items():
            ic(f"{key}: {value}")

    def load(self):
        try:
            self.anvilJson.load(self.project_file)
        except FileNotFoundError:
            return False
        except Exception as e:
            raise e
        return True

