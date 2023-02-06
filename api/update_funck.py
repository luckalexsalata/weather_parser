from .models import Weather


def update_db_data(date, temperature, description):
    exist_object = Weather.objects.filter(date=date)
    if exist_object:
        exist_object.update(temperature=temperature, description=description)
    else:
        weather = Weather(date=date, temperature=temperature, description=description)
        weather.save()