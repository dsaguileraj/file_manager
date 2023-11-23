from django.contrib.auth.models import User
from rest_framework.serializers import ValidationError, ModelSerializer
import re


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
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
        email_regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
        if not re.match(email_regex, value):
            raise ValidationError("Formato de email inválido.")
        user_id = self.instance.id if self.instance else None
        if User.objects.exclude(id=user_id).filter(email=value).exists():
            raise ValidationError(
                "Un usuario con este email ya existe.")
        return value

    def validate_password(self, value):
        if len(value) < 8:
            raise ValidationError(
                "La contraseña debe tener al menos 8 caracteres.")
        return value
