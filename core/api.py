from core.models import Sensor
from rest_framework import viewsets, permissions
from .serializer import SensorSerializer
from django.db.models import Q


class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()

    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = SensorSerializer
