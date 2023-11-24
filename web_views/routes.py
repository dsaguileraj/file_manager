from django.urls import include, path

urlpatterns = [
    path('auth/', include("web_views.auth.routes")),
    path('management/', include("web_views.management.routes")),
]
