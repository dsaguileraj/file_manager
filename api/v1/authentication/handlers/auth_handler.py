from rest_framework import status
from rest_framework.response import Response

from api.v1.authentication.services.auth_service import AuthService
from file_manager.views import BaseViewSet

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
        token, user = self.srv.signup(**request.data)
        if not user:
            return Response({"token": token.key}, status=status.HTTP_201_CREATED)
        return Response({}, status=status.HTTP_400_BAD_REQUEST)

    def login(self, request):
        """
        Request:
        - username:str
        - password:str
        """
        token, user = self.srv.login(**request.data)
        if user:
            return Response({"token": token.key}, status=status.HTTP_200_OK)
        return Response({"error": "Credenciales inválidas"}, status=status.HTTP_400_BAD_REQUEST)
