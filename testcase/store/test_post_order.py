import json
import os
from api.api_request import APIRequest
from api.requester import Requester
from jinja2 import Environment, FileSystemLoader
from constants import ROOT_PATH
from faker import Faker

def test_post_order():
    environment = Environment(loader=FileSystemLoader(os.path.join(ROOT_PATH, 'testcase/store')))
    template = environment.get_template('post_order.json')
    faker = Faker()
    data = {
        "id": faker.random_int(min=1, max=100),
        "pedId": faker.random_int(),
        "quantity": faker.random_digit()
    }

    url = "store/order"

    api = APIRequest()
    response = api.request('post', url, json=json.loads(template.render(data)))
    assert response.status_code == 200

    
