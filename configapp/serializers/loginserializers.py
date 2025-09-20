from django.core.cache import cache
from configapp.models import User
from rest_framework import serializers


class SendEmailSerializer(serializers.Serializer):
    email = serializers.EmailField()
    text = serializers.CharField()


class VerifyEmailSerializer(serializers.Serializer):
    email = serializers.EmailField()
    verification_code = serializers.CharField(max_length=12)

    def validate(self, attrs):
        email = attrs.get("email")
        verification_code = attrs.get("verification_code")

        cache_code = cache.get(f"sms_{email}")

        if not cache_code:
            raise serializers.ValidationError({
                "email": "Email kodi topilmadi yoki muddati o‘tib ketdi"
            })

        if str(cache_code) != verification_code:
            raise serializers.ValidationError({
                "verification_code": "Tasdiqlash kodi noto‘g‘ri."
            })

        cache.set(f"verified_{email}", True, timeout=600)

        return attrs


class SendEmailSerializers(serializers.Serializer):
    email = serializers.EmailField()



class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('phone_number', 'email', 'password')

    def create(self, validated_data):
        user = User(
            phone_number=validated_data['phone_number'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def validate(self, attrs):
        email = attrs.get('email')
        verified = cache.get(f"verified_{email}")
        if not verified:
            raise serializers.ValidationError({
                "email": "Bu email hali tasdiqlanmagan."
            })
        return attrs
