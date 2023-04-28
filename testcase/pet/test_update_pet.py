from faker import Faker
from api.api_request import APIRequest
from api.requester import Requester

def test_update_pet():
    petId = 10
    url = f"pet/{petId}"

    fake = Faker()
    params = {
        "name": fake.name(),
        "status": "available"
    }

    api = APIRequest()
    response = api.request('post', url, params=params)
    assert response.status_code == 200