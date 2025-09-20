from configapp.models import *
from rest_framework import serializers

from configapp.serializers.teacherserializers import TeacherSerializers
from configapp.serializers.userserializers import UserSerializers


class TeacherPostSerializer(serializers.Serializer):
    user = UserSerializers()
    teacher=TeacherSerializers()