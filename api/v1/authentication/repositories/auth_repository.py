from contextlib import suppress

from django.contrib.auth.models import User


class AuthRepository:

    @staticmethod
    def get_one(id: int):
        with suppress(User.DoesNotExist):
            return User.objects.get(id=id)

    @staticmethod
    def get_all(filters: dict = None):
        if not filters:
            filters = {}
        return User.objects.filter(**filters).order_by("id")
