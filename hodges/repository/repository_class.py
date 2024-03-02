class Repository:
    def __init__(self, url=None, vcs=None):
        self.url = url
        self.vcs = vcs

    def from_json(self, json_root):
        self.url = json_root.get('url')
        self.vcs = json_root.get('vcs')

    def to_json(self):
        return {
            'url': self.url,
            'vcs': self.vcs
        }
