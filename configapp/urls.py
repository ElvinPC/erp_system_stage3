from rest_framework.routers import DefaultRouter
from configapp.views import *
from django.urls import path,include

from configapp.serializers.Crud_login import VerifyApi
from configapp.serializers.Crud_teacher import SendSmsAPIView, VerifyCodeApiView
from configapp.views import SendEmailApi
from configapp.views.registerview import RegisterApi

router = DefaultRouter()
# router.register(r'teachers',TeacherCreateApi)
# router.register(r'department',DepartmentAPI)
# router.register(r'course',CourseAPI)

urlpatterns = [
    path('',include(router.urls)),
    path('send_mail/',SendSmsAPIView.as_view(),name = 'send_email'),
    path('send_sms/',SendSmsAPIView.as_view()),
    path('verify/',VerifyCodeApiView.as_view()),
    path('register/',RegisterApi.as_view()),
]