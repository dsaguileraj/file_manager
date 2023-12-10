from rest_framework.serializers import ModelSerializer

from apps.management.models import File


class FileSerializer(ModelSerializer):
    class Meta:
        model = File
        fields = (
            "id",
            "user",
            "name",
            "description",
            "url",
            "created_at",
            "updated_at",
        )
