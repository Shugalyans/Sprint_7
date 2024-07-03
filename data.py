URL = 'http://qa-scooter.praktikum-services.ru/api/v1'

colors = ['"BLACK"',
          '"GREY"',
          '"BLACK", "GREY"',
         None
         ]
orderEndpoints = ['orders?courierId=335921',
          'orders?courierId=335921&nearestStation=["1", "2"]',
          'orders?limit=10&page=0',
         'orders?limit=10&page=0&nearestStation=["110"]'
         ]

color = None
order = {
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