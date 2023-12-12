from filesystem import FileSystemManager
from icecream import ic
import os
import subprocess
from package.package import Package
from config import debug

class Debian(Package):
    def __init__(self, package_path):
        super().__init__(package_path)
        self.target_dir = "target"
        self.package_dir = ""
        self.fs = FileSystemManager()
        self.check_dependencies()

    def check_dependencies(self):
        if debug: ic("[INFO] Checking for necessary tools...")
        tools = ["dpkg-deb"]
        for tool in tools:
            if not self.is_tool_installed(tool):
                if debug: ic(f"[WARNING] {tool} is not installed. Do you want to install it? (y/n)")
                response = input()
                if response.lower() == 'y':
                    self.install_tool(tool)
                else:
                    if debug: ic(f"[ERROR] {tool} is not installed and installation declined. Exiting.")
                    return

    def is_tool_installed(self, tool):
        try:
            subprocess.check_output(["which", tool])
            return True
        except subprocess.CalledProcessError:
            return False
    
    def copy_files(self, source, destination):
        if debug: ic(f"[INFO] Copying files from {source} to {destination}...")
        self.fs.cp(source, self.fs.join(self.package_dir, destination))

    def create_script_file(self, script_name, content):
        if debug: ic(f"[INFO] Creating {script_name} script...")
        with open(self.fs.join(self.package_dir, "DEBIAN", script_name), "w") as script_file:
            script_file.write(content)

    def install_tool(self, tool):
        if debug: ic(f"[INFO] Installing {tool}...")
        os.system(f"sudo apt-get install {tool}")

    def create_package_structure(self):
        if debug: ic("[INFO] Creating package structure...")
        self.fs.mkdir(self.package_dir)
        self.fs.mkdir(self.fs.join(self.package_dir, "DEBIAN"))
        self.fs.mkdir(self.fs.join(self.package_dir, "usr"))
        self.fs.mkdir(self.fs.join(self.package_dir, "usr", "bin"))
        self.fs.mkdir(self.fs.join(self.package_dir, "usr", "share"))
        self.fs.mkdir(self.fs.join(self.package_dir, "usr", "share", self.name))
        self.create_script_file("postinst", "#!/bin/sh\necho 'Post-install script'")
        self.create_script_file("preinst", "#!/bin/sh\necho 'Pre-install script'")
        self.create_script_file("prerm", "#!/bin/sh\necho 'Pre-remove script'")
        self.create_script_file("postrm", "#!/bin/sh\necho 'Post-remove script'")
        os.chmod(self.fs.join(self.package_dir, "DEBIAN", script_name), 0o755)

    def create_control_file(self):
        if debug: ic("[INFO] Creating control file...")
        control_content = f"""Package: {self.name}
        Version: {self.version}
        Architecture: {self.architecture}
        Maintainer: {self.author}
        Description: {self.description}
        """
        if debug: ic(f"[INFO] Control content before writing: {control_content}")
        with open(self.fs.join(self.package_dir, "DEBIAN", "control"), "w") as control_file:
            control_file.write(control_content)

    def build_package(self):
        if debug: ic("[INFO] Building package...")
        os.system(f"dpkg-deb --build {self.package_dir}")
        self.fs.mv(f"{self.name}_{self.version}_{self.architecture}.deb", self.target_dir)
        if debug: ic(f"[INFO] Package {self.name}_{self.version}_{self.architecture}.deb built and moved to {self.target_dir}")

    def create_and_build_package(self):
        self.create_package_structure()
        self.build_package()
