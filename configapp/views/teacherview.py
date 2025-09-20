from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from django.shortcuts import get_object_or_404
from configapp.models.teachermodel import Teacher
from configapp.serializers.Crud_login import SendEmailSerializer
from configapp.serializers.Crud_teacher import TeacherSerializers
from django.conf import settings
from django.core.mail import send_mail
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

class SendEmailApi(APIView):
    @swagger_auto_schema(request_body=SendEmailSerializer)
    def post(self, request):
        serializer = SendEmailSerializer(data=request.data)
        if serializer.is_valid():
            subject = 'Bekhruzdan salomlar'
            message = serializer.validated_data['text']
            email = serializer.validated_data['email']
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]

            send_mail(subject, message, email_from, recipient_list)

            return Response({email: "yuborildi"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
