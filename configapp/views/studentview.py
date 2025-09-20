from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from configapp.models.studentmodel import Student
from configapp.serializers.studentserializers import StudentSerializers
from django.shortcuts import get_object_or_404

class StudentApi(APIView):

    @swagger_auto_schema(request_body=StudentSerializers)
    def post(self, request):
        serializer = StudentSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"message": "Student qoshildi!"}, status=status.HTTP_201_CREATED)

    def get(self, request, pk=None):
        if pk:
            student = get_object_or_404(Student, pk=pk)
            serializer = StudentSerializers(student)
            return Response(serializer.data, status=status.HTTP_200_OK)
        students = Student.objects.all()
        serializer = StudentSerializers(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=StudentSerializers)
    def put(self, request, pk):
        student = get_object_or_404(Student, pk=pk)
        serializer = StudentSerializers(student, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        student = get_object_or_404(Student, pk=pk)
        student.delete()
        return Response({"detail": "Ochirildi"}, status=status.HTTP_204_NO_CONTENT)
