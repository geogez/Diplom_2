import requests
import allure
from urls.url_config import APIEndpoints
from testdata.data import TestData

class UserCreationTests:

    @allure.title('Создание уникального пользователя')
    @allure.description('Проверка успешного создания пользователя и корректного ответа в формате JSON')
    def test_create_unique_user(self, user_data):
        assert user_data.status_code == 200
        assert user_data.json().get('success') is True

    @allure.title('Попытка создания пользователя, который уже существует в системе')
    @allure.description('Проверка кода статуса и ответа в формате JSON при попытке создать уже существующего пользователя')
    def test_create_existing_user(self):
        response = requests.post(APIEndpoints.create_user, data=TestData.predefined_user)
        assert response.status_code == 403
        assert response.json().get('success') is False

    @allure.title('Попытка создания пользователя с пропущенным полем')
    @allure.description('Проверка кода статуса и ответа в формате JSON при создании пользователя с пропущенным полем')
    def test_create_user_with_missing_field(self):
        response = requests.post(APIEndpoints.create_user, data=TestData.invalid_password_data)
        assert response.status_code == 403
        assert response.json().get('success') is False
