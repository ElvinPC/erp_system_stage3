from configapp.models import *
from rest_framework import serializers

from configapp.serializers.Crud_teacher import TeacherSerializers
from configapp.serializers.Crud_user import UserSerializers


class TeacherPostSerializer(serializers.Serializer):
    user = UserSerializers()
    teacher=TeacherSerializers()