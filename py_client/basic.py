import requests

# sending a request to this return an HTML, it's no endpoint
endpoint = "https://httpbin.org/"

# sending a request to this return a JSON. It's an endpoint.
endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/"

get_response = requests.get(endpoint)

get_response = requests.get(endpoint, data={'query': 'hello world'})
# Content-type: application/x-www-form-urlencoded

get_response = requests.get(endpoint, params={'abc': 123}, json={
                            'query': 'hello world'})
# header has Content-type: application/json

print(get_response.text)  # Print raw text response

# HTTP Request -> HTML
# REST API HTTP Request -> JSON
# JavaScript Object Notation ~ Python Dict (Object in case of JS)
print(get_response.json())  # Print json response
print(get_response.status_code)
