import requests

endpoint = 'http://127.0.0.1:8000/api/products/update/10/'

get_response = requests.put(
    endpoint, {'title': 'Updated Product', 'price': '9.9'})

print(get_response.json())
