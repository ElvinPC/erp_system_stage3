from django.db import models

from configapp.models import *
from configapp.models import User, BaseModel

class Course(BaseModel):
    title =models.CharField(max_length=50)
    descriptions =models.CharField(max_length=500,null=True,blank=True)
    def __str__(self):
        return self.title

class Departments(BaseModel):
    title = models.CharField(max_length=50)
    is_active =models.CharField(default=True)
    descriptions =models.CharField(max_length=500,null=True,blank=True)

    def __str__(self):
        return self.title



class Teacher(BaseModel):

    user =models.OneToOneField(User,on_delete=models.CASCADE,related_name='get_user')
    departments = models.ManyToManyField(Departments,related_name="get_departments")
    course =models.ManyToManyField(Course,related_name='get_course')
    descriptions =models.CharField(max_length=500,blank=True,null=True)


    def __str__(self):
        return self.user.phone_number

