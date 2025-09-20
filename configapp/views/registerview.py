from django.contrib.auth.hashers import make_password
from django.core.cache import cache
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from configapp import serializers
from configapp.models import User
from configapp.serializers.Crud_login import  RegisterSerializer
from configapp.serializers.Crud_user import UserSerializers


class RegisterApi(APIView):
    @swagger_auto_schema(request_body=UserSerializers)
    def post(self,request):
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
            'status':True,
            'detail':'Account create'
        })
