from django.urls import path

from web_views.management.file_views import list_files, edit_file, delete_file

urlpatterns = [
    path('file/', list_files, name='list_files'),
    path('file/edit/', edit_file, name='create_file'),
    path('file/edit/<int:id>', edit_file, name='edit_file'),
    path('file/delete/<int:id>', delete_file, name='delete_file'),
]
