import pytest
import requests
from Sprint_7.data import URL, orderEndpoints
import allure

class TestListOfOrders():

   @allure.description(
      'Получаем список заказов в теле ответа, отправляя различные данные'
   )
   @pytest.mark.parametrize('orderEndpoint', orderEndpoints)
   def test_get_list_of_orders(self, orderEndpoint):

      response = requests.get(f'{URL}/{orderEndpoint}')
      assert response.status_code == 200 and "orders" in response.text

