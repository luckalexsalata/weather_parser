## Installation
You can run a demo of the app with Docker and Docker Compose:

```bash
docker-compose up --build
```
##### Create Admin
Post username and password for next url:
 ```bash 
docker exec -it weather_parser python manage.py createsuperuser
``` 
django admin :
 ```bash 
http://localhost:8080/admin/
```
get weather information:

 ```bash 
http://localhost:8080/api/list/
```
change update time(you need post data)
 ```bash 
http://localhost:8080/api/update-time/
```
to manually start the task, you need to go to the path:
 ```bash 
http://localhost:8080/api/update/
```
For track the status of parsing tasks I used "flower", you can see along the way:
 ```bash 
http://localhost:5555/
```

 May the Force be with you!
