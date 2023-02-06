from django.urls import path
from .views import UpdateWeatherView, WeatherListView

urlpatterns = [
    path('update/', UpdateWeatherView.as_view()),
    path('list/', WeatherListView.as_view()),
]