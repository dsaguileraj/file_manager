from rest_framework import status
from rest_framework.response import Response

from api.v1.management.serializers.file_serializer import FileSerializer
from api.v1.management.services.file_service import FileService
from file_manager.views import BaseViewSet
from resources.utils.clean_data import CleanData


class FileHandler(BaseViewSet):
    srv = FileService()

    def retrieve(self, request, id):
        if not (file := self.srv.get_one(id)):
            return Response({"error": "File not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = FileSerializer(file, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def list(self, request):
        filters = CleanData.clean_filters(request.GET.dict())
        files = self.srv.get_all(filters)
        serializer = FileSerializer(files, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        try:
            data = request.data
        except Exception:
            data = request.POST.dict()
        if "user" not in data and request.user.is_authenticated:
            data["user"] = request.user.id
        file_serializer = FileSerializer(data=data, partial=False)
        if not file_serializer.is_valid():
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        file_obj = file_serializer.save()
        if file := request.FILES.get("file_upload"):
            self.srv.save_file(file, file_obj)
        return Response(file_serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, id):
        if not (file := self.srv.get_one(id)):
            return Response({"error": "File not found"}, status=status.HTTP_404_NOT_FOUND)
        try:
            data = request.data
        except Exception:
            data = request.POST.dict()
        serializer = FileSerializer(file, data=data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        file_obj = serializer.save()
        if file := request.FILES.get("file_upload"):
            self.srv.save_file(file, file_obj)
        return Response(serializer.data,
                        status=status.HTTP_200_OK)

    def delete(self, request, id):
        file = self.srv.get_one(id)
        if not file:
            return Response({"error": "File not found"}, status=status.HTTP_404_NOT_FOUND)
        self.srv.delete_file(file)
        file.delete()
        return Response({}, status=status.HTTP_200_OK)
