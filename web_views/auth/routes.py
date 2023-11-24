from django.urls import path

from web_views.auth.authentication_views import login, logout, signup

urlpatterns = [
    path('auth/login/', login, name='login'),
    path('auth/signup/', signup, name='signup'),
    path('auth/logout/', logout, name='logout'),
]
