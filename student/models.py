from django.db import models

# Create your models here. 

class Student(models.Model):
    f_name=models.CharField(max_length = 50)
    l_name=models.CharField(max_length = 50)
    age=models.IntegerField()


class User(models.Model)  :
    name=models.CharField(max_length = 50)
    email=models.EmailField(primary_key=True)
    password=  models.CharField(max_length=50)  





  
    
