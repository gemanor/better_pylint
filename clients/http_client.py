import requests


class HTTPClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def get(self, path):
        requests.get(self.host + ":" + self.port + path)
