import requests
from clients.github_client import GithubClient


def get_repositories():
    return requests.get("http://localhost:8080/repositories")


def get_repository(name):
    return GithubClient().get("/repositories/" + name)
