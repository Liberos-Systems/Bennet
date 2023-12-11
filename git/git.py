import uuid
from git import Repo
from git.repo_data import RepoData
from rich.console import Console
from rich.prompt import Prompt
from filesystem.filesystem import FileSystemManager

console = Console()
fs = FileSystemManager()

class GitRepo:
    def __init__(self, origin_url=None, json_file=None):
        self.json_file = json_file
        self.working_dir = f".{uuid.uuid4().hex[:8]}_yard"
        fs.mkdir(self.working_dir)
        if origin_url:
            self.origin = RepoData(origin_url)
            self.target = RepoData(origin_url)
            self.origin_info = self.extract_info(origin_url)
        elif json_file:
            self.json = RepoData(json_file=json_file)
            self.origin_info = self.load_info()

    def clear_all(self):
        yarn_folders = [folder for folder in fs.ls() if folder.endswith("_yarn")]
        for folder in yarn_folders:
            if Prompt.ask(f"Are you sure you want to delete the {folder}? (Y/n)"):
                fs.rm(folder, recursive=True)
                console.print(f"Deleted {folder}")

    def clear_all(self):
        for folder in fs.ls():
            if folder.endswith("_yarn"):
                fs.rm(folder, recursive=True)
                console.print(f"Deleted {folder}")

    def extract_info(self, url):
        repo = RepoData(url)
        info = {
            "origin": repo.origin,
            "target": repo.target,
            "branch": repo.branch,
            "latest_commit": repo.latest_commit,
            "repo_name": repo.repo_name,
            "repo_size": repo.repo_size,
            "repo_owner": repo.repo_owner,
            "repo_last_updated": repo.repo_last_updated,
            "repo_description": repo.repo_description,
            "repo_language": repo.repo_language,
            "repo_license": repo.repo_license,
            "repo_forks_count": repo.repo_forks_count,
            "repo_stars_count": repo.repo_stars_count,
            "repo_watchers_count": repo.repo_watchers_count,
            "repo_open_issues_count": repo.repo_open_issues_count,
            "repo_has_issues": repo.repo_has_issues,
            "repo_has_projects": repo.repo_has_projects,
            "repo_is_public": repo.repo_is_public,
            "repo_visibility": repo.repo_visibility,
            "repo_collaborators_count": repo.repo_collaborators_count,
            "repo_file_count": repo.repo_file_count,
            "repo_line_count": repo.repo_line_count,
            "repo_commit_count": repo.repo_commit_count,
            "repo_contributor_count": repo.repo_contributor_count,
            "repo_last_commit_timestamp": repo.repo_last_commit_timestamp,
            "repo_push_count_last_week": repo.repo_push_count_last_week,
            "repo_pull_request_count_last_week": repo.repo_pull_request_count_last_week
        }
        console.print(info)
        return RepoData(data=info)

    def clone(self):
        console.print("Cloning repository...")
        with console.status("[bold green]Cloning...") as status:
            self.target_repo = Repo.clone_from(self.origin.origin, self.working_dir)
            console.print("Repository cloned successfully.")
            
    def save_info(self, info):
        if self.json_file:
            info.save_to_json(self.json_file)
        else:
            console.print("No JSON file specified for saving info.")

    def load_info(self):
        if self.json_file:
            repo = RepoData(json_file=self.json_file)
            return repo.load_from_json(self.json_file)
        else:
            console.print("No JSON file specified for loading info.")

    def change_json_file(self, new_json_file):
        fs.mv(self.json_file, new_json_file)
        self.json_file = new_json_file

    def change_target_repo(self, new_repo_url):
        self.target.target = new_repo_url
        self.target_repo = Repo(self.target.target)
        self.target_info = self.extract_info(new_repo_url)
        self.save_info(self.target_info)

    def push_changes(self):
        self.target_repo.git.push()

    def pull_changes(self):
        self.target_repo.git.pull()

