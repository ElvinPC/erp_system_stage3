from django.db import models

from configapp.models import *
from configapp.models import User


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    surname =models.CharField(max_length=100)
    address =models.CharField(max_length=50)
    user_id =models.ForeignKey(User,on_delete=models.CASCADE)
