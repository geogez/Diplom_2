import allure
import pytest
import requests
from urls.url_config import APIEndpoints
from testdata.data import TestData


class UserUpdateTests:

    @allure.title('Попытка обновления данных пользователя без авторизации')
    @allure.description('Проверка кода статуса и содержимого JSON-ответа при попытке обновления данных без авторизации')
    @pytest.mark.parametrize('invalid_data',
                             [TestData.invalid_password_data, TestData.invalid_email_data])
    def test_update_user_without_auth(self, invalid_data):
        response = requests.patch(APIEndpoints.update_user, data=invalid_data)
        assert response.status_code == 401
        assert response.json().get('message') == 'You should be authorised'

    @allure.title('Обновление данных авторизованного пользователя')
    @allure.description('Проверка кода статуса и содержимого JSON-ответа при успешном обновлении данных пользователя')
    def test_update_user_with_auth(self, login_static_user):
        token = login_static_user.json().get('accessToken')
        response = requests.patch(APIEndpoints.update_user, headers={'Authorization': f'Bearer {token}'},
                                  data={'name': 'Георгий Гезалянц Updated'})
        assert response.status_code == 200
        assert response.json().get('user', {}).get('name') == 'Георгий Гезалянц Updated'

    @allure.title('Обновление почты авторизованного пользователя')
    @allure.description('Проверка кода статуса и содержимого JSON-ответа при обновлении почты пользователя')
    def test_update_user_email_with_auth(self, login_static_user):
        token = login_static_user.json().get('accessToken')
        response = requests.patch(APIEndpoints.update_user, headers={'Authorization': f'Bearer {token}'},
                                  data={'email': 'new_email@example.com'})
        assert response.status_code == 200
        assert response.json().get('user', {}).get('email') == 'new_email@example.com'

    @allure.title('Обновление пароля авторизованного пользователя')
    @allure.description('Проверка кода статуса и содержимого JSON-ответа при обновлении пароля пользователя')
    def test_update_user_password_with_auth(self, login_static_user):
        token = login_static_user.json().get('accessToken')
        response = requests.patch(APIEndpoints.update_user, headers={'Authorization': f'Bearer {token}'},
                                  data={'password': 'new_password'})
        assert response.status_code == 200
        assert response.json().get('message') == 'Password updated successfully'
