# utils.py


from django.core.files.storage import FileSystemStorage


class FileHelper:

    def __init__(self):
        self.fs = FileSystemStorage()

    def save_file(self, file, filename):
        filename = self.fs.save(filename, file)
        return self.get_path(filename)

    def delete_file(self, file_name):
        if self.fs.exists(file_name):
            self.fs.delete(file_name)

    def update_file(self, file, old_filepath, new_filename):
        self.delete_file(old_filepath.split("media/")[-1])
        return self.save_file(file, new_filename)

    def get_path(self, filename):
        return self.fs.url(filename)
