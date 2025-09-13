from configapp.models import *
from rest_framework import serializers
class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['phone_number', 'password', 'email','is_teacher','is_admin','is_student']
        read_only_fields = ['is_active']