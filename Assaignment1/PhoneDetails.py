import math
mobile_data = {
    'status': True,
    'data': [
          {'name': 'Xiaomi Note 5', 'price': '300 USD', 'made': 'China'},
          {'name': 'Samsung Note 6', 'price': '200 USD', 'made': 'USA'},
          {'name': 'Iphone 5', 'price': '180.5 USD', 'made': 'Japan'},
          {'name': 'Pixel 5', 'price': '89.60 USD', 'made': 'Rusia'},
          {'name': 'Techno 5', 'price': '110 USD', 'made': 'Uk'},
          {'name': 'Huawei 5', 'price': '350 USD', 'made': 'Malaysia'},
            ],
    'exchnage_rate': 107.2
            }
def getConvertedPrice(price):
        priceInNumber = int(math.ceil(float(price.split()[0])))
        return priceInNumber * mobile_data['exchnage_rate']


for eachItem in mobile_data['data']:
        print(f"{eachItem['name']} is made in {eachItem['made']}. The price is {eachItem['price'] } which is almost equal to {getConvertedPrice(eachItem['price'])} BDT")
