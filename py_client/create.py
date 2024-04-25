import requests

headers = {
    'Authorization': 'Bearer b7cc4a4cfd5967d18d420e240f4cde0eec0af4d0'
}

endpoint = 'http://127.0.0.1:8000/api/products/'

get_response = requests.post(
    endpoint, {'title': 'Testing Create Api_View', 'price': 29}, headers=headers)

print(get_response.json())
