import json
import os
from api.api_request import APIRequest
from api.requester import Requester
import pytest
from jinja2 import Environment, FileSystemLoader
from faker import Faker

from constants import ROOT_PATH
from utils import load_test_data

# @pytest.mark.parametrize("test_input, expected", load_test_data(r"testcase/pet/post_pet.yaml"))
def test_post_pet(test_input, expected):
    url = "pet"

    env = Environment(loader=FileSystemLoader(os.path.join(ROOT_PATH, r'testcase/pet')))
    template = env.get_template('post_pet.json')
    data = test_input['data']

    api = APIRequest()
    response = api.request('post', url, json=json.loads(template.render(data)))
    assert response.status_code == expected['status_code']
    assert response.json() == expected["response"]