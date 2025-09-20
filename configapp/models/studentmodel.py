from django.db import models

from configapp.models import User, BaseModel


class Student(BaseModel):
    name= models.CharField(max_length=128)
    surname =models.CharField(max_length=128)
    address =models.CharField(max_length=128)
    user =models.OneToOneField(User,on_delete=models.CASCADE,related_name="student_id")
    # group =models.ManyToManyField('GroupStudent',related_name='get_group')
    is_line =models.BooleanField(default=False)
    description =models.CharField(max_length=500,blank=True,null=True)

    def __str__(self):
        return self.user.phone_number

class Parents(BaseModel):
    student =models.OneToOneField(Student,on_delete=models.CASCADE,related_name="student")
    full_name =models.CharField(max_length=50,null=True,blank=True)
    phone_number =models.CharField(max_length=15,null=True,blank=True)
    address =models.CharField(max_length=200,null=True,blank=True)
    descriptions =models.CharField(max_length=500,null=True,blank=True)
    created =models.DateTimeField(auto_now_add=True)
    updated =models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name


