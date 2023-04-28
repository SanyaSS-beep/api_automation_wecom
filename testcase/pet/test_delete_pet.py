from api.api_request import APIRequest


def test_delete_pet():
    petId = 10
    url = f"pet/{petId}"
    headers = {
        "api_key": "api_key"
    }

    requester = APIRequest()
    response = requester.request('delete', url, headers=headers)
    assert response.status_code == 200
    