from configapp.models import *
from rest_framework import serializers

from configapp.models.teachermodel import Teacher


class TeacherSerializers(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['name', 'surname', 'address']
        read_only_fields = ["user_id"]
# class AddUserSerializers(serializers.ModelSerializer):
#     is_active =serializers.BooleanField(read_only=True)
#     is_teacher =serializers.BooleanField(read_only=True)
#     is_admin =serializers.BooleanField(read_only=True)
#     is_stuff =serializers.BooleanField(read_only=True)
#     is_student =serializers.BooleanField(read_only=True)
#     class Meta:
#         model =User
#         class Meta:
#             model = User
#             fields = ['phone_number', 'password', 'email', 'is_teacher', 'is_admin', 'is_student']
#             read_only_fields = ['is_active']



# class TeacherPostSerializers(serializers.Serializer):
#     user =AddUserSerializers()
#     teacher =TeacherPostSerializers()
# class TeacherSerializers(serializers.ModelSerializer):
#     user =AddUserSerializers()
#     departments =serializers.PrimaryKeyRelatedField(queryset=Departaments.objects.all(),many =True)
#     course =serializers.PrimaryKeyRelatedField(queryset=Course.objects.all(),many=True)
#
#     class Meta:
#         models =Teacher
#         fields =["id","user","departments","course","descriptions"]
#     def create(self, validated_data):
#         user_db =validated_data.pop("user")
#         departments_db=validated_data.pop("departments")
#         course_db =validated_data.pop("course")
#         user_db=["is_active"]=True
#         user_db=["is_teacher"=True