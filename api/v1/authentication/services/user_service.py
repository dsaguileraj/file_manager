from api.v1.authentication.repositories.user_repository import UserRepository

from django.contrib.auth.models import User


class UserService:

    def __init__(self) -> None:
        self.repo = UserRepository

    def get_one(self, id: int = None, filters: dict = None):
        if id:
            return self.repo.get_one(id=id)
        return self.repo.get_all(filters).first()

    def get_all(self, filters: dict = None):
        return self.repo.get_all(filters)

    def create_user(self, username: str, email: str, password: str):
        return User.objects.create_user(username=username,
                                        email=email,
                                        password=password)
