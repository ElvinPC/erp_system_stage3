from django.db import models

from configapp.models import User


class Student(models.Model):
    name= models.CharField(max_length=128)
    surname =models.CharField(max_length=128)
    address =models.CharField(max_length=128)
    user =models.OneToOneField(User,on_delete=models.CASCADE,related_name="student_id")

