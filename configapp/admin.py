from django.contrib import admin

from configapp.models.usermodel import *
from configapp.models.studentmodel import *
from configapp.models.teachermodel import *

admin.site.register([Teacher,User,Student])