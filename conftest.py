import os
import pytest

from api_info.requester import Requester

@pytest.fixture(autouse=True, scope='function')
def token(request, cache):
    token_value = cache.get("token", None)
    if token_value is None:
        corpid = os.environ.get('corpid')
        syncContact = os.environ.get('syncContact')
        
        url = f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={syncContact}'
        print(url)
        requestster = Requester(url)
        response = requestster.get().json()

        assert response['errcode'] == 0
        assert response['errmsg'] == 'ok'
        token_value = response['access_token']
        cache.set("token", token_value)
    return token_value