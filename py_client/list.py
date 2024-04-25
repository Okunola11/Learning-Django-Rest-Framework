import requests
from getpass import getpass

endpoint = 'http://127.0.0.1:8000/api/auth/'
username = input('\nWhat is your username?')
password = getpass()

auth_response = requests.post(
    endpoint, json={'username': username, 'password': password})

print(auth_response.json())


if auth_response.status_code == 200:
    endpoint = 'http://127.0.0.1:8000/api/products'

    token = auth_response.json()['token']
    headers = {
        # the default keyword here is 'Token' for Python not 'Bearer' we did an override on it @api/authentication.py
        'Authorization': f'Bearer {token}'
    }
    get_response = requests.get(
        endpoint, headers=headers
    )

    print(get_response.json())

    # {'Authorization': f'Token {auth_response.json()['token']}'}
