from api.api_request import APIRequest


def test_find_pet_by_status():
    url = f'pet/findByStatus'
    params = {
        "status": "available"
    }

    api = APIRequest()
    response = api.request('get', url, params=params)

    assert response.status_code == 200