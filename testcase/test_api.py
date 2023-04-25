import json
import os
from jinja2 import Template
from jinja2 import Environment, FileSystemLoader
from faker import Faker
from api_info.requester import Requester
from constants import ROOT_PATH

from helper.fetch_url import fetch_url

def test_fetch_access_token(token):
    url = f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={token}'
    requester = Requester(url)

    env = Environment(loader=FileSystemLoader(os.path.join(ROOT_PATH, r'api_info')))
    template = env.get_template('create.json')
    fake = Faker()
    data = {
        "userid": fake.name(),
        "name": fake.name(),
        "alias": fake.name(),
        "mobile": fake.phone_number()
    }
    print(data)
    response = requester.post(json=json.loads(template.render(data))).json()
    assert response['errcode'] == 0
    assert response['errmsg'] == 'created'