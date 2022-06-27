"""
Github client handlers
"""
import requests
from clients.github_client import GithubClient


def get_repositories():
    """
    :return: list of repositories
    """
    return requests.get("http://localhost:8080/repositories")


def get_repository(name):
    """
    :param name: name of the repository
    :return: repository data
    """
    return GithubClient().get("/repositories/" + name)
