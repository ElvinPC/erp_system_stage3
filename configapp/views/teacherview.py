from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from django.shortcuts import get_object_or_404
from configapp.models.teachermodel import Teacher
from configapp.serializers.loginserializers import SendEmailSerializer
from configapp.serializers.teacherserializers import TeacherSerializers
class TeacherApi(APIView):

    @swagger_auto_schema(request_body=TeacherSerializers)
    def post(self, request):
        serializer = TeacherSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"message": "Teacher qoshildi!"}, status=status.HTTP_201_CREATED)

    def get(self, request, pk=None):
        if pk:
            teacher = get_object_or_404(Teacher, pk=pk)
            serializer = TeacherSerializers(teacher)
            return Response(serializer.data, status=status.HTTP_200_OK)
        teachers = Teacher.objects.all()
        serializer = TeacherSerializers(teachers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=TeacherSerializers)
    def put(self, request, pk):
        teacher = get_object_or_404(Teacher, pk=pk)
        serializer = TeacherSerializers(teacher, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        teacher = get_object_or_404(Teacher, pk=pk)
        teacher.delete()
        return Response({"detail": "O'chirildi"}, status=status.HTTP_204_NO_CONTENT)


