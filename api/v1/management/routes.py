from django.urls import path

from api.v1.management.handlers.file_handler import FileHandler


urlpatterns = [
    path("file/", FileHandler.as_view({"get": "list",
                                       "post": "create"}), name="file"),
    path("file/<int:id>", FileHandler.as_view({"get": "retrieve",
                                               "put": "update",
                                               "delete": "delete"}), name="file_id"),
]
