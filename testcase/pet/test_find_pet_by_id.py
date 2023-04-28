from api.api_request import APIRequest


def test_find_pet_by_id():
    petId = 1
    url = f"pet/{petId}"

    api = APIRequest()
    response = api.request('get', url)
    assert response.status_code == 200
