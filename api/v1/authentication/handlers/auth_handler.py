from rest_framework import status
from rest_framework.response import Response

from api.v1.authentication.serializers.auth_serializer import UserSerializer
from api.v1.authentication.services.auth_service import AuthService
from file_manager.views import BaseViewSet
from utils.clean_data import CleanData


class UserHandler(BaseViewSet):
    srv = AuthService()

    def retrieve(self, request, id):
        if not (user := self.srv.get_one(id)):
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def list(self, request):
        filters = CleanData.clean_filters(request.GET.dict())
        users = self.srv.get_all(filters)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        data = request.data
        user_serializer = UserSerializer(data=data, partial=False)
        if not user_serializer.is_valid():
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        user_serializer.save()
        return Response(user_serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, id):
        if not (user := self.srv.get_one(id)):
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        data = request.data
        serializer = UserSerializer(user, data=data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data,
                        status=status.HTTP_200_OK)

    def delete(self, request, id):
        if not (user := self.srv.get_one(id)):
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        user.delete()
        return Response({}, status=status.HTTP_200_OK)
