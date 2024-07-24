import requests
import allure
from urls.url_config import APIEndpoints
from testdata.data import TestData


class UserOrderTests:

    @allure.title('Получение заказов без авторизации')
    @allure.description('Проверка кода ответа и содержания JSON для неавторизованного запроса')
    def test_fetch_orders_without_authentication(self, login_static_user):
        response = requests.get(APIEndpoints.retrieve_orders)
        assert response.status_code == 401
        assert response.json().get('message') == 'You should be authorised'

    @allure.title('Получение заказов с авторизацией')
    @allure.description('Проверка кода ответа и содержания JSON для авторизованного запроса')
    def test_fetch_orders_with_authentication(self, login_static_user):
        access_token = login_static_user.json().get('accessToken')
        if access_token:
            token_header = {'Authorization': f'Bearer {access_token}'}
            response = requests.get(APIEndpoints.retrieve_orders, headers=token_header)
            assert response.status_code == 200
            assert response.json().get('success') is True
