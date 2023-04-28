from api.api_request import APIRequest
from api.requester import Requester

def test_post_image():
    petId = 10
    url = f"pet/{petId}/uploadImage"
    params = {
        "additionalMetadata": "additionalMetadata"
    }

    headers = {
        "Content-Type": "application/octet-stream",
        "accept": "application/json"
    }

    api = APIRequest()
    response = api.request('post', url, params=params, headers=headers)
    assert response.status_code == 200