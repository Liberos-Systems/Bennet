import pygit2

class GitRepo:
    def __init__(self, repo_url):
        self.repo_url = repo_url
        self.repo = pygit2.Repository(self.repo_url)

    def get_repo_info(self):
        repo_info = {
            'repo_name': self.repo.path.split('/')[-1],
            'repo_path': self.repo.path,
            'repo_size': self.repo.size,
            'repo_owner': self.repo.owner.name,
            'repo_last_commit': self.repo.head.target.hex,
            'repo_branches': [branch for branch in self.repo.branches],
            'repo_tags': [tag for tag in self.repo.tags],
            'repo_remotes': [remote for remote in self.repo.remotes]
        }
        return repo_info
    
    def print_all_repo_attributes(self):
        for attr in dir(self.repo):
            if not attr.startswith('_'):
                print(f'{attr}: {getattr(self.repo, attr)}')

