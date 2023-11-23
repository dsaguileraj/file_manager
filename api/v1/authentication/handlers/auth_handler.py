from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from api.v1.authentication.serializers.user_serializer import UserSerializer
from api.v1.authentication.services.auth_service import AuthService
from file_manager.views import BaseViewSet
from django.contrib.auth import authenticate

# ... tus importaciones existentes ...


class AuthHandler(BaseViewSet):
    srv = AuthService()

    def signup(self, request):
        """
        Request:
        - username:str
        - email:str
        - password:str
        """
        token, errors = self.srv.signup(**request.data):
        if not errors:
            return Response({"token": token.key}, status=status.HTTP_201_CREATED)
        return Response(errors, status=status.HTTP_400_BAD_REQUEST)

    def login(self, request):
        """
        Request:
        - username:str
        - password:str
        """
        if token := self.srv.login(**request.data):
            return Response({"token": token.key}, status=status.HTTP_200_OK)
        return Response({"error": "Credenciales inválidas"}, status=status.HTTP_400_BAD_REQUEST)
