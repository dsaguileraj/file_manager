from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password

from api.v1.authentication.repositories.user_repository import UserRepository
from api.v1.authentication.serializers.user_serializer import UserSerializer


class AuthService:

    def __init__(self) -> None:
        self.repo = UserRepository

    def login(self, username: str, password: str):
        if user := authenticate(username=username,
                                password=password):
            return self.generate_token(user)

    def signup(self, username: str, email: str, password: str):
        data = {"username": username,
                "email": email,
                "password": password}
        serializer = UserSerializer(data=data)
        if not serializer.is_valid():
            return None, serializer.errors
        user = serializer.save()
        user.password = make_password(user.password)
        user.save()
        return self.generate_token(user), []

    def generate_token(self, user: User):
        token, _ = Token.objects.get_or_create(user=user)
        return token
