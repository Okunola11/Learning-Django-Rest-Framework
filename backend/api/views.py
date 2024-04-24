# from django.shortcuts import render
import json
from django.http import JsonResponse

# Create your views here.


def api_home(request, *args, **kwargs):
    print(request.GET)  # url query params
    print(request.POST)
    body = request.body  # this is a byte string of JSON data
    data = {}
    try:
        data = json.loads(body)  # string of JSON data -> python dictionary
    except:
        pass
    print(f'Body is {data.keys()}')
    # older versions of django use request.META to get the headers
    # data['headers'] = request.headers // this could not be converted into a json data
    # so we had to enforce it to a dict() as done below

    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type
    data['params'] = request.GET
    return JsonResponse(data)
