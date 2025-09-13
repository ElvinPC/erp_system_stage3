# from django.contrib.auth.base_user import BaseUserManager
# from django.db import models
# class User(models.Model):
#     phone_number = models.CharField(max_length=13,unique=True)
#     password =models.CharField(max_length=128)
#     email = models.EmailField(unique=True,null=True,blank=True)
#     is_active = models.BooleanField(default=True)
#     is_admin = models.BooleanField(default=False)
#     is_student = models.BooleanField(default=False)
#     is_teacher = models.BooleanField(default=False)
#     USERNAME_FIELD = 'phone_number'
#     REQUIRED_FIELDS = []
#     objects = BaseUserManager()
from django.contrib.auth.models import *
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError('Phone number is required')
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(phone_number, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    phone_number = models.CharField(max_length=13, unique=True)
    email = models.EmailField(unique=True, null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.phone_number
