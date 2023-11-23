from django.contrib.auth.models import User
from rest_framework.serializers import ValidationError, ModelSerializer


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password")
        extra_kwargs = {
            "password": {
                "write_only": True
            }
        }

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise ValidationError(
                "Un usuario con este email ya existe.")
        return value

    def validate_password(self, value):
        if len(value) < 8:
            raise ValidationError(
                "La contraseña debe tener al menos 8 caracteres.")
        return value
