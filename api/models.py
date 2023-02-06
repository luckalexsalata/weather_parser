from django.db import models
from django.contrib.auth.models import User


class Weather(models.Model):
    date = models.CharField(max_length=50) # CharField because in task not data format
    temperature = models.CharField(max_length=20) # parser get two temperature the problem of getting one value is to pass the captcha
    description = models.TextField(blank=True, null=True)


