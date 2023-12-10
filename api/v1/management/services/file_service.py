from api.v1.management.repositories.file_repository import FileRepository
from django.core.files.storage import FileSystemStorage
from resources.utils.file_helper import FileHelper
from apps.management.models import File


class FileService:

    def __init__(self) -> None:
        self.repo = FileRepository
        self.file_helper = FileHelper()

    def get_one(self, id: int = None, filters: dict = None):
        if id:
            return self.repo.get_one(id=id)
        return self.repo.get_all(filters).first()

    def get_all(self, filters: dict = None):
        return self.repo.get_all(filters)

    def get_empty(self):
        return self.repo.get_empty()

    def save_file(self, file, file_obj: File):
        if file_obj.url:
            url = self.file_helper.update_file(file=file,
                                               old_filepath=file_obj.url,
                                               new_filename=file.name)
        else:
            url = self.file_helper.save_file(file=file,
                                             filename=file.name)
        file_obj.url = url
        file_obj.save()

    def delete_file(self, file: File):
        if file.url:
            self.file_helper.delete_file(file.url.split("media/")[-1])
