from django.urls import path
from .views import UpdateWeatherView, WeatherListView, UpdateTaskTimeView

urlpatterns = [
    path('update/', UpdateWeatherView.as_view()),
    path('list/', WeatherListView.as_view()),
    path('update-time/', UpdateTaskTimeView.as_view()),
]