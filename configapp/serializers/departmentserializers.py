from rest_framework import serializers
from configapp.models import Departments


class DepartmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = "__all__"