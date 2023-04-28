import json
import os
from jinja2 import Template
from jinja2 import Environment, FileSystemLoader
from faker import Faker
from api.api_request import APIRequest
from constants import ROOT_PATH

from helper.fetch_url import fetch_url

def test_put_pet(token):
    url = f'pet'
    requester = APIRequest()

    env = Environment(loader=FileSystemLoader(os.path.join(ROOT_PATH, r'testcase/pet')))
    template = env.get_template('put_pet.json')
    fake = Faker()
    data = {
        "name": fake.name(),
        "category": fake.name()
    }
    response = requester.request('put', url, json=json.loads(template.render(data)))
    assert response.status_code == 200
