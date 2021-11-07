from django.db import models

#C:\Users\porntep.pj\Documents\GitHub\flutterBootCamp\DJANGO WEBAPI>.\venv\scripts\activate
#(venv) C:\Users\porntep.pj\Documents\GitHub\flutterBootCamp\DJANGO WEBAPI>cd flutterapi
#(venv) C:\Users\porntep.pj\Documents\GitHub\flutterBootCamp\DJANGO WEBAPI\flutterapi>python manage.py runserver


#create database
#python manage.py makemigrations
#python manage.py migrate

# Create your models here.
class Todolist(models.Model):
    title = models.CharField(max_length=100)
    detail = models.TextField(null=True, blank=True) # ไม่บังคับใส่ข้อมูล

    def __str__(self):
        return self.title  # ให้แสดงค่า subject
