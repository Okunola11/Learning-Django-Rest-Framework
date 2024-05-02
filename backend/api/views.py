import json
from django.forms.models import model_to_dict
# from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializer

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

# Create your views here.


@api_view(['GET'])
def api_home(request, *args, **kwargs):
    instance = Product.objects.all().order_by(
        "?").first()  # returns a random instance of 'Product'
    data = {}
    if instance:
        # data['id'] = instance.id
        # data['title'] = instance.title
        # data['content'] = instance.content
        # data['price'] = instance.price

        # built in method to avoid the manual process above, with options to select fields from the data
        # data = model_to_dict(instance, fields=['id', 'title', 'sale_price'])

        # Serializers does model_to_dict() function for us
        data = ProductSerializer(instance).data

        # Serialization
        # model instance (instance)
        # Turn to a Python dict()
        # Return JSON to my client

    return Response(data)


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
