import random

from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.conf import settings

from configapp.serializers.loginserializers import *
from configapp.serializers.userserializers import UserSerializers


class SendSmsAPIView(APIView):
    @swagger_auto_schema(request_body=SendEmailSerializers)
    def post(self, request):
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
        return Response(data={f"{email}": "Yuborildi"})


class RegisterApi(APIView):
    @swagger_auto_schema(request_body=UserSerializers)
    def post(self, request):
        serializer = UserSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data.get("email")
        verified = cache.get(f"verified_{email}")
        if not verified:
            return Response({
                'status': False,
                'detail': 'Bu email hali tasdiqlanmagan. Avval OTP orqali tasdiqlang.'
            }, status=status.HTTP_400_BAD_REQUEST)
        password = serializer.validated_data["password"]
        serializer.validated_data["password"] = make_password(password)
        serializer.save()
        return Response({
            'status': True,
            'detail': 'Account create'
        })


class VerifyCodeApiView(APIView):
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