import allure
import requests
from Sprint_7.helpers import create_courier_for_test
from Sprint_7.data import URL


class TestCouriers:

    @allure.description(
        'Проверяем, что курьера можно создать'
    )
    def test_possible_to_create_courier(self):
        payload=create_courier_for_test()
        response = requests.post(f'{URL}/courier', payload)

        #курьер создан, логин пароль есть, проверим id курьера == курьер точно создан
        response = requests.post(f'{URL}/courier/login', payload)
        assert response.status_code == 200 and "id" in response.text

    @allure.description(
        'Проверяем, что нельзя создать 2 одинаковых курьера'
    )
    def test_not_possible_to_create_2_identical_couriers(self):
        payload = create_courier_for_test()
        response = requests.post(f'{URL}/courier', payload)
        #второй раз отправим POST на ручку с тем же payload
        response = requests.post(f'{URL}/courier', payload)

        assert response.status_code == 409 and response.text == '{"code":409,"message":"Этот логин уже используется. Попробуйте другой."}'

    @allure.description(
        'Проверяем, что для создания курьера надо заполнить все обязательные поля'
    )
    def test_fill_all_mandatory_fields_to_create_courier(self):
        payload = create_courier_for_test()
        values = list(payload.values())
        response = requests.post(f'{URL}/courier', payload)

        payload = {
            "login": values[0],
            "password": "",
            "firstName": values[2]
        }

        response = requests.post(f'{URL}/courier', payload)
        assert response.status_code == 400

    @allure.description(
    'Проверяем, что при успешном создании курьера возвращается код == 201'
    )
    def test_request_return_correct_answer(self):
        payload = create_courier_for_test()
        response = requests.post(f'{URL}/courier', payload)

        assert response.status_code == 201 and response.text == '{"ok":true}'

    @allure.description('Проверяем, что если одного из полей нет, запрос возвращает ошибку')
    def test_receive_error_if_mandatory_field_is_empty(self):
        payload = create_courier_for_test()
        values = list(payload.values())
        response = requests.post(f'{URL}/courier', payload)

        payload = {
            "login": "",
            "password": values[1],
            "firstName": values[2]
        }

        response = requests.post(f'{URL}/courier', payload)

        assert response.text == '{"code":400,"message":"Недостаточно данных для создания учетной записи"}'

