#!/usr/bin/env python3
from common.common import ic, nf
from hodges.file_system.file_system_class import FileSystemManager
from anvil.anvil import Anvil
from common.config import version, debug
from models.classes.git_base import GitRepo
class Bennet:
    def __init__(self):
        ic(f"BENNET version: {version}")
        self.fs = FileSystemManager()
        self.project_name = "./project.bennet.json"
        self.project = Anvil(filesystem=self.fs, root="project", project_name=self.project_name)
        
        ic(self.fs.root_) if debug else None

        if debug:
            self.root_dir = "./bennet_develop_space"

            if self.fs.exists(self.root_dir):
                self.fs.cd(self.root_dir)

    def build(self):
        ic("Running build function") if debug else None
        if not self.project.load():
            nf()
            return
        
        self.project.data = self.project.anvilJson.get_data()
        ic(self.project.data)

    def update(self):
        ic("Running update function") if debug else None
        if not self.project.load():
            nf()
            return

    def install(self):
        ic("Running install function") if debug else None
        if not self.project.load():
            nf()
            return

    def script(self, operation):
        ic("Running script function") if debug else None
        if not self.project.load():
            nf()
            return

    def init(self):
        ic("Running init function") if debug else None

        if debug:
            self.root_dir = "./bennet_develop_space"
            self.fs.cd("..")
            if self.fs.exists(self.root_dir):
                self.fs.rmdir(self.root_dir)

            if not self.fs.exists(self.root_dir):
                self.fs.mkdir(self.root_dir)
                self.fs.cd(self.root_dir)

        self.project.init()

    def interactive_init(self):
        ic("Running interactive_init function") if debug else None
        self.project.interactive_init()

    def change_root(self):
        ic("Running change_root function") if debug else None
        self.project.change_root()

    def help(self):
        ic("Running Help function") if debug else None

    def abba(self):
        git_base = GitRepo('https://github.com/elementary/switchboard-plug-network.git')
        repo_info = git_base.get_repo_info()
        ic(repo_info) if debug else None

