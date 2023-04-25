import os
import yaml
from constants import ROOT_PATH

def fetch_url():
    with open(os.path.join(ROOT_PATH, r'env.yaml')) as f:
        config = yaml.safe_load(f)
    app_env = os.environ.get('APP_ENV')
    if app_env not in config:
        raise ValueError(f'Invalid APP_ENV value: {app_env}')
    return config[app_env]['url']