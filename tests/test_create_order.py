import allure
import requests
import json
import pytest
from data import colors, URL, order



class TestCreateOrder:

    @allure.description(
        'Проверяем, что заказ можно создать с любым цветом или без него'
    )
    @pytest.mark.parametrize('color', colors)
    def test_set_color(self, order, color):
        json_string = json.dumps(order)
        response = requests.post(f'{URL}/orders', json_string)
        assert response.status_code == 201 and 'track' in response.text

