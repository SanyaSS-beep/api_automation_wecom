import os
import yaml
from faker import Faker
from constants import ROOT_PATH

def load_test_data(path):
    test_data = yaml.safe_load(open(os.path.join(ROOT_PATH, path)))
    for data in test_data:
        if "use_faker" in data:
            faker = Faker()
            for key, value in data["test_input"]['data'].items():
                if "{{ faker." in str(value):
                    # {{ faker.name }
                    value = str(value).replace("{{ faker.", "{{ ").replace(" }}", " }}")      
                    value = yaml.safe_load()
                    # data["test_input"]['data'] = {k: getattr(faker,v)() for k, v in value.items()}
                    method_name = value['value']
                    method_args = value.get('args', [])
                    method_kwargs = value.get('kwargs', [])
                    method = getattr(faker, method_name)
                    data['test_input']['data'][key] = method(*method_args, **method_kwargs)
    return test_data    
    