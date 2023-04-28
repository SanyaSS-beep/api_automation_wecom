from api.api_request import APIRequest
from api.requester import Requester

def test_store_inventory():
    url = "store/inventory"

    api = APIRequest()
    response = api.request('get', url)
    assert response.status_code == 200