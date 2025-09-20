from configapp.models import *
from rest_framework import serializers
class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name', 'surname', 'address']
