from api.api_request import APIRequest
from api.requester import Requester

def test_get_order_by_id():
    orderId = 1
    url = f"store/order/{orderId}"
    
    api = APIRequest()
    response = api.request('get', url)
    assert response.status_code == 200