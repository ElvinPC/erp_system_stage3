from django.db import models
class Student(models.Model):
    name= models.CharField(max_length=128)
    surname =models.CharField(max_length=128)
    address =models.CharField(max_length=128)
