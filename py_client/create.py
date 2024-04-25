import requests

endpoint = 'http://127.0.0.1:8000/api/products/'

get_response = requests.post(
    endpoint, {'title': 'Testing Create Api_View', 'price': 29})

print(get_response.json())
