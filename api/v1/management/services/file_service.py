from api.v1.management.repositories.file_repository import FileRepository


class FileService:

    def __init__(self) -> None:
        self.repo = FileRepository

    def get_one(self, id: int = None, filters: dict = None):
        if id:
            return self.repo.get_one(id=id)
        return self.repo.get_all(filters).first()

    def get_all(self, filters: dict = None):
        return self.repo.get_all(filters)
