import allure
import requests
import json
import pytest
from Sprint_7.data import colors, URL



class TestCreateOrder:

    @allure.description(
        'Проверяем, что заказ можно создать с любым цветом или без него'
    )
    @pytest.mark.parametrize('color', colors)
    def test_set_color(self, color):
        order =  {
                  "firstName": "Naruto",
                  "lastName": "Uchiha",
                  "address": "Konoha, 142 apt.",
                  "metroStation": 4,
                  "phone": "+7 800 355 35 35",
                  "rentTime": 5,
                  "deliveryDate": "2020-06-06",
                  "comment": "Saske, come back to Konoha",
                  "color": [color]
        }
        json_string = json.dumps(order)
        response = requests.post(f'{URL}/orders', json_string)
        assert response.status_code == 201 and 'track' in response.text

