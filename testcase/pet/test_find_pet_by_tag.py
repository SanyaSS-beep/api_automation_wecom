from api.api_request import APIRequest
from api.requester import Requester

def test_find_pet_by_tag():
    url = "pet/findByTags"
    params = {
        "tags":['1']
    }

    api = APIRequest()
    response = api.request('get', url, params=params)
    assert response.status_code == 200