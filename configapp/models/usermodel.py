from django.db import models
class User(models.Model):
    phone_number = models.CharField(max_length=13,unique=True)
    password =models.CharField(max_length=128)
    email = models.EmailField(unique=True,null=True,blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)