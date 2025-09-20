from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from configapp.models.usermodel import User
from configapp.serializers import TeacherPostSerializer
from configapp.serializers.teacherserializers import TeacherSerializers
from configapp.serializers.userserializers import UserSerializers

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
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

from configapp.models.teachermodel import Teacher
from configapp.serializers.userserializers import UserSerializers
from configapp.serializers.teacherserializers import TeacherSerializers


class TeacherAndUser(APIView):

    @swagger_auto_schema(request_body=TeacherPostSerializer)
    def post(self, request):
        user_data = request.data.get('user', None)
        user_serializer = UserSerializers(data=user_data)
        if user_serializer.is_valid():
            user = user_serializer.save(is_teacher=True)
        else:
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        teacher_data = request.data.get('teacher', None)
        teacher_serializer = TeacherSerializers(data=teacher_data)
        if teacher_serializer.is_valid():
            teacher_serializer.save(user=user)
        else:
            user.delete()
            return Response(teacher_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response({
            "user": user_serializer.data,
            "teacher": teacher_serializer.data
        }, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(responses={200: TeacherPostSerializer(many=True)})
    def get(self, request):
        teachers = Teacher.objects.select_related('user').all()
        data = []
        for teacher in teachers:
            teacher_data = TeacherSerializers(teacher).data
            user_data = UserSerializers(teacher.user).data
            data.append({
                "teacher": teacher_data,
                "user": user_data
            })
        return Response(data, status=status.HTTP_200_OK)
