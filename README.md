# Todolist-api
django todolist api

### Prerequisites
```
Python (3.5)
Django 1.10             ==> pip install django
Django Rest Framework   ==> pip install djangorestframework
pytz                    ==> pip install pytz
```

### Installing
```
clone or download zip
- git clone https://github.com/netp4ss/todolist-api.git

then extract file and go to TaskAPI directory and run
- python manage.py runserver
```

### Database 
db.sqlite3 (sqlite)
```
table Task
task_name : CharField [max_length=100]
task_desc : TextField [max_lenght=500]
date_created : DateTimeField
completed : BooleanField
```

## Testing
```
* [Testing by using Postman](http://www.youtube.com)
```
