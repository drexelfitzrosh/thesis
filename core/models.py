from django.db import models

# Create your models here.


class Sensor(models.Model):
    soilMoisture = models.FloatField()
    temperature = models.FloatField()
    humidity = models.FloatField()
    water = models.FloatField()
    time = models.TimeField()
    date = models.DateField()
