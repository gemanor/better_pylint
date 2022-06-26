from http_client import HTTPClient


class GithubClient(HTTPClient):
    def __init__(self):
        super().__init__(host="https://www.github.com", port=443)

    def get_repositories(self):
        return self.get("/repositories")

    def get_repository(self, name):
        return self.get("/repositories/{}".format(name))
