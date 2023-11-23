from django.urls import include, path

urlpatterns = [
    path('auth/', include('api.v1.authentication.routes')),
    path('management/', include('api.v1.management.routes')),
]
