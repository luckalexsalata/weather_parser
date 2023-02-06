FROM python:3.11
ENV PYTHONUNBUFFERED 1

RUN mkdir /weather_parser
WORKDIR /weather_parser

COPY requirements.txt .
COPY . /weather_parser/

RUN pip install -r requirements.txt

ADD . /weather_parser/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]