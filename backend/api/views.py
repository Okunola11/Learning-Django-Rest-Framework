# from django.shortcuts import render
import json
from django.http import JsonResponse

from products.models import Product

# Create your views here.


def api_home(request, *args, **kwargs):
    model_data = Product.objects.all().order_by(
        "?").first()  # returns a random instance of 'Product'
    data = {}
    if model_data:
        data['id'] = model_data.id
        data['title'] = model_data.title
        data['content'] = model_data.content
        data['price'] = model_data.price
                
        # Serialization
        # model instance (model_data)
        # Turn to a Python dict()
        # Return JSON to my client

    return JsonResponse(data)


# These are from the first lesson instance to learn basics

# def api_home(request, *args, **kwargs):
# print(request.GET)  # url query params
# print(request.POST)
# body = request.body  # this is a byte string of JSON data
# data = {}
# try:
#   data = json.loads(body)  # string of JSON data -> python dictionary
# except:
#   pass
# print(f'Body is {data.keys()}')
# older versions of django use request.META to get the headers
# data['headers'] = request.headers // this could not be converted into a json data
# so we had to enforce it to a dict() as done below

# data['headers'] = dict(request.headers)
# data['content_type'] = request.content_type
# data['params'] = request.GET
# return JsonResponse(data)
