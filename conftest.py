import pytest
import requests
from testdata.data import TestData
from urls.url_config import APIEndpoints


@pytest.fixture
def create_user():
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}  # Убедитесь, что заголовки правильные
    response = requests.post(APIEndpoints.register_user, data=TestData.create_test_data(), headers=headers)

    assert response.status_code == 200, f"Failed to create user: {response.text}"

    yield response

    access_token = response.json().get('accessToken')
    if access_token:
        token = f"Bearer {access_token}"
        delete_response = requests.delete(APIEndpoints.update_user_info, headers={'Authorization': token})
        assert delete_response.status_code == 200, f"Failed to delete user: {delete_response.text}"


@pytest.fixture
def login_static_user():
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}  # Убедитесь, что заголовки правильные
    response = requests.post(APIEndpoints.login_user, data=TestData.predefined_user, headers=headers)

    assert response.status_code == 200, f"Failed to login user: {response.text}"

    yield response
