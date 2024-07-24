import random
from datetime import datetime
class TestData:

    predefined_user = {'email': 'geogez_88@gmail.com', 'password': 'gTVawZ88', 'name': 'Георгий Гезалянц'}

    invalid_password_data = {'email': 'geogez_88@gmail.com', 'password': '', 'name': ''}

    invalid_email_data = {'email': '', 'password': 'gTVawZ88', 'name': ''}

    @staticmethod
    def generate_data():
        current_time = datetime.now().strftime('%Y%m%d%H%M')
        username = "AutoTest" + current_time
        user_email = username + '@yandex.ru'
        user_password = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=8)) + 'password'
        return {'email': user_email, 'password': user_password, 'name': username}

class IngredientSamples:

    valid_burger = {"ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]}

    faulty_burger = {"ingredients": ["61c0c5проблема1bdaaa6d", "61c0c5a71проблемаdaaa72"]}

    empty_burger = {"ingredients": []}