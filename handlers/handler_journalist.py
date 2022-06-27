"""
Github action handler
"""
from clients.http_client import HTTPClient


def handler(action):
    """
    :param action: action to be handled
    :return: action handler
    """
    client = HTTPClient('https://api.github.com', '443')
    if action == 'get_repositories':
        return client.get('get_repositories')
    if action == 'get_repository':
        return client.get('get_repository')
    if action == 'get_issues':
        return client.get('get_issues')
    return None
