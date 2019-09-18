from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View

# Create your views here.


def get_data(request, *args, **kwargs):
    data = {
        'id': 1,
        "user": 'drexel'
    }
    return JsonResponse(data)
