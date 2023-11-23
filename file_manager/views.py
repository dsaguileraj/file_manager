from django.conf import settings
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated

TOKEN_AUTHENTICATION = settings.TOKEN_AUTHENTICATION


class BaseViewSet(viewsets.ViewSet):
    """
    Vista basica sin permisos
    """


class IsAuthViewSet(BaseViewSet):
    """
    Vista con permisos solo para usuarios autenticados
    """
    if TOKEN_AUTHENTICATION:
        permission_classes = [IsAuthenticated,]


class IsAdminViewSet(BaseViewSet):
    """
    Vista con permisos solo para superusuarios
    """
    if TOKEN_AUTHENTICATION:
        permission_classes = [IsAuthenticated, IsAdminUser,]
