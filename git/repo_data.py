from json.json import Json
from config import debug

class RepoData:
    def __init__(self, data=None, json_file=None, key=None):
        self.json_handler = Json(json_file) if json_file else None
        if debug:
            print("Initializing RepoData")
        if data:
            self.origin = data.get('origin')
            self.target = data.get('target', self.origin)
            self.branch = data.get('branch')
            self.latest_commit = data.get('latest_commit')
            self.repo_name = data.get('repo_name')
            self.repo_size = data.get('repo_size')
            self.repo_owner = data.get('repo_owner')
            self.repo_last_updated = data.get('repo_last_updated')
            self.repo_description = data.get('repo_description')
            self.repo_language = data.get('repo_language')
            self.repo_license = data.get('repo_license')
            self.repo_forks_count = data.get('repo_forks_count')
            self.repo_stars_count = data.get('repo_stars_count')
            self.repo_watchers_count = data.get('repo_watchers_count')
            self.repo_open_issues_count = data.get('repo_open_issues_count')
            self.repo_has_issues = data.get('repo_has_issues')
            self.repo_has_projects = data.get('repo_has_projects')
            self.repo_is_public = data.get('repo_is_public')
            self.repo_visibility = data.get('repo_visibility')
            self.repo_collaborators_count = data.get('repo_collaborators_count')
            self.repo_file_count = data.get('repo_file_count')
            self.repo_line_count = data.get('repo_line_count')
            self.repo_commit_count = data.get('repo_commit_count')
            self.repo_contributor_count = data.get('repo_contributor_count')
            self.repo_last_commit_timestamp = data.get('repo_last_commit_timestamp')
            self.repo_push_count_last_week = data.get('repo_push_count_last_week')
            self.repo_pull_request_count_last_week = data.get('repo_pull_request_count_last_week')
        elif json_file:
            self.load_from_json(json_file, key)

    def load_from_json(self, json_file, key=None):
        self.json_handler = Json(json_file)
        data = self.json_handler.load()
        if debug:
            print("Loaded data from JSON")
        if key:
            data = data.get(key)
        self.__init__(data)

    def save_to_json(self, file_path, key=None):
        data = {
            "origin": self.origin,
            "target": self.target,
            "branch": self.branch,
            "latest_commit": self.latest_commit,
            "repo_name": self.repo_name,
            "repo_size": self.repo_size,
            "repo_owner": self.repo_owner,
            "repo_last_updated": self.repo_last_updated,
            "repo_description": self.repo_description,
            "repo_language": self.repo_language,
            "repo_license": self.repo_license,
            "repo_forks_count": self.repo_forks_count,
            "repo_stars_count": self.repo_stars_count,
            "repo_watchers_count": self.repo_watchers_count,
            "repo_open_issues_count": self.repo_open_issues_count,
            "repo_has_issues": self.repo_has_issues,
            "repo_has_projects": self.repo_has_projects,
            "repo_is_public": self.repo_is_public,
            "repo_visibility": self.repo_visibility,
            "repo_collaborators_count": self.repo_collaborators_count,
            "repo_file_count": self.repo_file_count,
            "repo_line_count": self.repo_line_count,
            "repo_commit_count": self.repo_commit_count,
            "repo_contributor_count": self.repo_contributor_count,
            "repo_last_commit_timestamp": self.repo_last_commit_timestamp,
            "repo_push_count_last_week": self.repo_push_count_last_week,
            "repo_pull_request_count_last_week": self.repo_pull_request_count_last_week
        }
        self.json_handler = Json(file_path)
        self.json_handler.add_data(key, data) if key else self.json_handler.update_data(key, data)
        self.json_handler.save()
        if debug:
            print("Saved data to JSON")

