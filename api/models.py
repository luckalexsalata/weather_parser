from django.db import models
from django.contrib.auth.models import User


class Weather(models.Model):
    date = models.CharField(max_length=50)
    temperature = models.CharField(max_length=20)
    description = models.TextField(blank=True, null=True)


