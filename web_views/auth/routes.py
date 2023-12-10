from django.urls import path

from web_views.auth.authentication_views import login_view, logout_view, signup_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('logout/', logout_view, name='logout'),
]
