from django.urls import path

from api.v1.authentication.handlers.auth_handler import UserHandler


urlpatterns = [
    path("user/", UserHandler.as_view({"get": "list",
                                       "post": "create"}), name="user"),
    path("user/<int:id>", UserHandler.as_view({"get": "retrieve",
                                               "put": "update",
                                               "delete": "delete"}), name="user_id"),
]
