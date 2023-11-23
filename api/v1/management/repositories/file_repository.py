from contextlib import suppress

from apps.management.models import File


class FileRepository:

    @staticmethod
    def get_one(id: int):
        with suppress(File.DoesNotExist):
            return File.objects.get(id=id)

    @staticmethod
    def get_all(filters: dict = None):
        if not filters:
            filters = {}
        return File.objects.filter(**filters).order_by("-created_at")
