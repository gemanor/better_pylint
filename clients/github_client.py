"""
Github HTTP Client
"""
from clients.http_client import HTTPClient


class GithubClient(HTTPClient):
    """
    Github API Client
    """
    def __init__(self):
        super().__init__(host="https://www.github.com", port=443)

    def get_repositories(self):
        """
        Proxies /repositories github request
        :return: list of repositories
        """
        return self.get("/repositories")

    def get_repository(self, name):
        """
        Proxies /repositories/:name github request
        :param name: name of the repository
        :return: repository data
        """
        return self.get(f"/repositories/{name}")
