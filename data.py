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