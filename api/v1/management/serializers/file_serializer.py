from rest_framework.serializers import ModelSerializer

from apps.management.models import File


class FileSerializer(ModelSerializer):
    class Meta:
        model = File
        fields = (
            "name",
            "descirption",
            "url",
            "created_at",
            "updated_at",
        )
