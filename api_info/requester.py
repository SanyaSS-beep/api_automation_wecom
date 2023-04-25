import requests

class Requester:
    def __init__(self, url) -> None:
        self.url = url

    def get(self, params=None, headers=None):
        response = requests.get(self.url, params=params, headers=headers)
        return response

    def post(self, data=None, json=None, headers=None):
        response = requests.post(self.url, data=data, json=json, headers=headers)
        return response