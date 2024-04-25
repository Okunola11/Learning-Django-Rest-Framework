import requests

product_id = input('What Product ID would you like to delete?\n')

try:
    product_id = int(product_id)
except:
    product_id = None
    print(f'{product_id} not a valid id')

if product_id:
    endpoint = f'http://127.0.0.1:8000/api/products/delete/{product_id}/'

    get_response = requests.delete(endpoint)
    print(f'Product with id: {product_id} has been succesfully deleted')
