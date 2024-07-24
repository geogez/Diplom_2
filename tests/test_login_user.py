import requests
import allure
from urls.url_config import APIEndpoints  # Обновленный импорт
from testdata.data import TestData  # Обновленный импорт


class UserAuthenticationTests:

    @allure.title('Успешный вход пользователя в систему')
    @allure.description('Проверка успешного ответа и кода статуса при корректных данных для входа')
    def test_successful_login(self):
        response = requests.post(APIEndpoints.login_user, data=TestData.predefined_user)
        assert response.status_code == 200
        assert response.json().get('success') is True

    @allure.title('Ошибка входа пользователя при неверном email')
    @allure.description('Проверка кода статуса и сообщения об ошибке при некорректном email')
    def test_login_with_invalid_email(self):
        response = requests.post(APIEndpoints.login_user, data=TestData.invalid_email_data)
        assert response.status_code == 401
        assert response.json().get('message') == 'email or password are incorrect'

    @allure.title('Ошибка входа пользователя при неверном пароле')
    @allure.description('Проверка кода статуса и сообщения об ошибке при некорректном пароле')
    def test_login_with_invalid_password(self):
        response = requests.post(APIEndpoints.login_user, data=TestData.invalid_password_data)
        assert response.status_code == 401
        assert response.json().get('message') == 'email or password are incorrect'
