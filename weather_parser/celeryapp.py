import os
from celery import Celery
print('hello')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "weather_parser.settings")
app = Celery("weather_parser")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()