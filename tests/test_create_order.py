import requests
import allure
from urls.url_config import APIEndpoints
from testdata.data import IngredientSamples


class OrderTests:

    @allure.title('Создание заказа с авторизацией пользователя')
    @allure.description('Проверка ответа сервера на запрос создания заказа в формате JSON')
    def test_authenticated_user_order_creation(self, create_user):
        # Используем фикстуру create_user для получения токена авторизации
        response = requests.post(APIEndpoints.create_order, json=IngredientSamples.valid_burger,
                                 headers={'Authorization': f"Bearer {create_user.json().get('accessToken')}"})
        assert response.json().get('name') == 'Бессмертный флюоресцентный бургер'

    @allure.title('Создание заказа с некорректным хэшем ингредиентов')
    @allure.description('Проверка кода ответа и JSON-содержимого для запроса с неверными ингредиентами')
    def test_order_with_invalid_ingredient_hash(self, create_user):
        response = requests.post(APIEndpoints.create_order, json=IngredientSamples.faulty_burger,
                                 headers={'Authorization': f"Bearer {create_user.json().get('accessToken')}"})
        assert response.status_code == 500

    @allure.title('Создание заказа без ингредиентов')
    @allure.description('Проверка кода ответа и сообщения об ошибке при отсутствии ингредиентов в запросе')
    def test_order_without_ingredients(self, create_user):
        response = requests.post(APIEndpoints.create_order, json=IngredientSamples.empty_burger,
                                 headers={'Authorization': f"Bearer {create_user.json().get('accessToken')}"})
        assert response.status_code == 400
        assert response.json().get('message') == 'Ingredient ids must be provided'
