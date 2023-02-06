from rest_framework import serializers
from api.models import Weather
from django_celery_beat.models import CrontabSchedule


class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = '__all__'


class CrontabScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrontabSchedule
        fields = '__all__'