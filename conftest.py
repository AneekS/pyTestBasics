# conftest.py
import pytest
import requests

BASE_URL = "https://reqres.in/api"
HEADERS = {"x-api-key": "reqres-free-v1"}


@pytest.fixture
def base_url():

    return BASE_URL


@pytest.fixture
def headers():

    return HEADERS


@pytest.fixture
def new_user(base_url, headers):

    payload = {"name": "random_useer", "job": "qa/at"}
    response = requests.post(f"{base_url}/users", json=payload, headers=headers)
    user = response.json()
    yield user  # provide user to the test
    # teardown: delete user
    if "id" in user:
        requests.delete(f"{base_url}/users/{user['id']}", headers=headers)
