import os
from importlib import import_module

def load_config():
    env = os.environ.get('APP_ENV', 'local')
    module_name = f'config.{env}'
    module = import_module(module_name)
    return module