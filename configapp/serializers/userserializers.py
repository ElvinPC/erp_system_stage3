from configapp.models import *
from rest_framework import serializers
class UserSerializers(serializers.ModelSerializer):
    is_active = serializers.BooleanField(read_only=True)
    is_teacher = serializers.BooleanField(read_only=True)
    is_admin = serializers.BooleanField(read_only=True)
    is_student = serializers.BooleanField(read_only=True)
    class Meta:
        model = User
        fields = ['phone_number', 'password', 'email','is_teacher','is_admin','is_student','is_active']
        read_only_fields = ['is_active']