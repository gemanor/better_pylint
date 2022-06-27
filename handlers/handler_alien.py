"""
  Github client class
"""
from clients.github_client import GithubClient


class Handler:
    """
      Github handler class
    """
    host = 'string'
    """
      Github Action Handlers
    """
    def get_repos(self):
        """
          :return: list of repositories
        """
        repos = GithubClient().get_repositories()
        return repos

    def get_repo(self, name):
        """
          :param name: name of the repository
          :return: repository data
        """
        repo = GithubClient().get_repository(name)
        return repo
