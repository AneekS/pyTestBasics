import requests
import pytest
from pygments.lexers import data

BASE_URL = "https://reqres.in/api"
# protection access key type
HEADERS = {
    "x-api-key": "reqres-free-v1"
}


# pytest fixtures
# DRY principle
@pytest.fixture
def base_url():
    return BASE_URL
# pytest fixtures
@pytest.fixture
def header_desc():
    return {  "x-api-key": "reqres-free-v1"}


# testing function

def test_req_api():
    response = requests.get(BASE_URL)
    assert response.status_code == 200
    data = response.json()
    print(data)

def test_post_creation():
    # description type
    payload = {
        "name": "aneek",
        "job": "automation"
    }
    response = requests.post(f"{BASE_URL}/users", json=payload,headers=HEADERS)
    assert response.status_code == 201
    data = response.json()
    print(data)

def test_delete_user():
    url = "https://reqres.in/api/users/2"
    headers = {"x-api-key": "reqres-free-v1"}
    response = requests.delete(url, headers=headers)
    assert response.status_code == 204

def test_update_user(base_url, header_desc):
    user_id = "Cris"
    payload = {"name": "aneek", "job": "lead"}
    response = requests.put(f"{BASE_URL}/users/{user_id}", json=payload, headers=header_desc)
    assert response.status_code == 200
    assert response.json()["job"] == "lead"