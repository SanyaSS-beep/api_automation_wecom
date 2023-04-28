import requests
from config.config_loader import load_config

class APIRequest:
    def __init__(self) -> None:
        self.config = load_config()
    
    def build_url(self, path):
        return f'{self.config.API_URL}/{self.config.API_VERSION}/{path}'

    def request(self, method, path, params=None, data=None, json=None, headers=None):
        url = self.build_url(path)
        try:
            with requests.request(method, url, params=params, data=data, json=json, headers=headers) as response:
                response.raise_for_status()
                return response
        except requests.exceptions.RequestException as e:
            print(f'Error during request: {e}')
            return response