from configapp.models import *
from rest_framework import serializers
class TeacherSerializers(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['name', 'surname', 'address']
        read_only_fields = ["user_id"]