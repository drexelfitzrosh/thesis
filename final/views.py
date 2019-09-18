from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View
from core.models import Sensor
from rest_framework.views import APIView
from rest_framework.response import Response
import json


# def get_data(request, *args, **kwargs):
#     data = {
#         'id': 1,
#         "name": 'drexel'
#     }
#     return JsonResponse(data)


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


# class ChartData(APIView):
#     authentication_classes = []
#     permission_classes = []

#     def get(self, request, format=None):
#         data = Sensor.objects.all()
#         s = json.dumps(data.__dict__)
#         return Response(s)
