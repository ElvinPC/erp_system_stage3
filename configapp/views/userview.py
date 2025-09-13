from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from configapp.models.usermodel import User
from configapp.serializers.Crud_user import UserSerializers

class UserApi(APIView):

    @swagger_auto_schema(request_body=UserSerializers)
    def post(self, request):
        serializer = UserSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"message": "User qoshildi!"}, status=status.HTTP_201_CREATED)

    def get(self, request, pk=None):
        if pk:
            user = get_object_or_404(User, pk=pk)
            serializer = UserSerializers(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        users = User.objects.all()
        serializer = UserSerializers(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=UserSerializers)
    def put(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializers(user, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        user.delete()
        return Response({"detail": "O'chirildi"}, status=status.HTTP_204_NO_CONTENT)