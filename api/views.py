from rest_framework.views import APIView
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import *
from .serializers import *

from api.tasks import parser_task


class UpdateWeatherView(generics.CreateAPIView):
    serializer_class = WeatherSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        parser_task()
        return Response({
            "Save": 'ok',
        })


class WeatherListView(generics.ListAPIView):
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer
