from django.db import models

# Create your models here.
class Location(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    lo_id = models.IntegerField(max_length=16)
    name = models.CharField(max_length= 30)


class Powerspot(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    ps_id = models.IntegerField(max_length = 16)
    name = models.CharField(max_length = 30)
