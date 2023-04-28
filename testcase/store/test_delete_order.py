from api.api_request import APIRequest
from api.requester import Requester

def test_delete_order():
    orderId = 1
    url = f"store/order/{orderId}"

    api = APIRequest()
    response = api.request('delete', url)
    assert response.status_code == 200
