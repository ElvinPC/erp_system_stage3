import random

from django.conf import settings
from django.core.cache import cache
from django.core.mail import send_mail
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from configapp.models import *
from rest_framework import serializers, status
from configapp.models.teachermodel import Teacher


from configapp.models import *
from rest_framework import serializers

from configapp.models.teachermodel import Teacher
from configapp.serializers.Crud_login import VerifyEmailSerializer, SendEmailSerializer, SendEmailSerializers

user = serializers.IntegerField(source='user.id', read_only=True)  # GET paytida faqat id qaytaradi


class TeacherSerializers(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"
        read_only_fields = ['user']

class SendSmsAPIView(APIView):
    @swagger_auto_schema(request_body=SendEmailSerializers)
    def post(self,request):
        serializer = SendEmailSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        subject = "Registiratsiya kod"
        message = str(random.randint(100000, 999999))
        email = serializer.validated_data['email']
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [f"{email}"]
        if message:
            cache.set(f"sms_{email}", message, 600)
            send_mail(subject, message, email_from, recipient_list)
        return Response(data={f"{email}":"Yuborildi"})



class VerifyCodeApiView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(request_body=VerifyEmailSerializer)
    def post(self, request):
        serializer = VerifyEmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        verification_code = serializer.validated_data['verification_code']

        cache_code = cache.get(f"sms_{email}")

        if cache_code and verification_code == str(cache_code):
            cache.set(f"verified_{email}", True, timeout=600)

            return Response({
                'status': True,
                'detail': 'OTP code to‘g‘ri! Endi registratsiyadan o‘tishingiz mumkin'
            }, status=status.HTTP_200_OK)

        return Response({
            'status': False,
            'detail': 'OTP incorrect yoki vaqt tugagan'
        }, status=status.HTTP_400_BAD_REQUEST)

# user = serializers.IntegerField(source='user.id', read_only=True)
# class TeacherPostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model =Teacher
#         fields =["id","department","course","descriptions"]
# class AddUserSerializer(serializers.ModelSerializer):
#     is_active =serializers.BooleanField(read_only=True)
#     is_teacher =serializers.BooleanField(read_only=True)
#     is_admin =serializers.BooleanField(read_only=True)
#     is_student =serializers.BooleanField(read_only=True)
#     is_staff =serializers.BooleanField(read_only=True)
#
#
# class TeacherSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Teacher
#         fields = ['name', 'surname', 'address']
#         read_only_fields = ["user"]
# class AddUserSerializers(serializers.ModelSerializer):
#     is_active =serializers.BooleanField(read_only=True)
#     is_teacher =serializers.BooleanField(read_only=True)
#     is_admin =serializers.BooleanField(read_only=True)
#     is_stuff =serializers.BooleanField(read_only=True)
#     is_student =serializers.BooleanField(read_only=True)
#     class Meta:
#         model =User
#         class Meta:
#             model = User
#             fields = ['phone_number', 'password', 'email', 'is_teacher', 'is_admin', 'is_student']
#             read_only_fields = ['is_active']


# class TeacherPostSerializers(serializers.Serializer):
#     user =AddUserSerializers()
#     teacher =TeacherPostSerializers()
# class TeacherSerializers(serializers.ModelSerializer):
#     user =AddUserSerializers()
#     departments =serializers.PrimaryKeyRelatedField(queryset=Departaments.objects.all(),many =True)
#     course =serializers.PrimaryKeyRelatedField(queryset=Course.objects.all(),many=True)
#
#     class Meta:
#         models =Teacher
#         fields =["id","user","departments","course","descriptions"]
#     def create(self, validated_data):
#         user_db =validated_data.pop("user")
#         departments_db=validated_data.pop("departments")
#         course_db =validated_data.pop("course")
#         user_db=["is_active"]=True
#         user_db=["is_teacher"=True
