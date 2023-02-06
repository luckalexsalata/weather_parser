from rest_framework.views import APIView
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import *
from .serializers import *

from api.tasks import parser_task
from django_celery_beat.models import CrontabSchedule, PeriodicTask


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


class UpdateTaskTimeView(generics.CreateAPIView):
    serializer_class = CrontabScheduleSerializer

    def post(self, request, *args, **kwargs):
        try:
            pk = PeriodicTask.objects.get(name='sample_task').pk
            req = request.data.dict()
            serializer = CrontabScheduleSerializer(data=req)
            if serializer.is_valid():
                current_data = CrontabSchedule.objects.filter(id=pk)
                current_data.update(**req)
                return Response({
                    "update": 'complete',
                })

            return Response({
                "error": 'not valid data',
            })
        except Exception as e:
            res = {"msg": str(e), "success": False, "data": None}
            return Response(data=res, status=status.HTTP_400_BAD_REQUEST)


