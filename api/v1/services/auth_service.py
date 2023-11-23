from api.v1.repositories.auth_repository import AuthRepository


class AuthService:

    def __init__(self) -> None:
        self.repo = AuthRepository

    def get_one(self, id: int = None, filters: dict = None):
        if id:
            return self.repo.get_one(id=id)
        return self.repo.get_all(filters).first()

    def get_all(self, filters: dict = None):
        return self.repo.get_all(filters)
