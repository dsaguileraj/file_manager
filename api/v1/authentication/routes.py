from django.urls import path

from api.v1.authentication.handlers.auth_handler import AuthHandler
from api.v1.authentication.handlers.user_handler import UserHandler

urlpatterns = [
    path("user/", UserHandler.as_view({"get": "list",
                                       "post": "create"}), name="user"),
    path("user/<int:id>", UserHandler.as_view({"get": "retrieve",
                                               "put": "update",
                                               "delete": "delete"}), name="user_id"),
]

urlpatterns += [
    path(
        "login/", AuthHandler.as_view({"post": "login"}), name="api_login"),
    path(
        "signup/", AuthHandler.as_view({"post": "signup"}), name="api_signup"),
]
