from django.contrib.auth.models import User
from django.db import models


class File(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='files')
    name = models.CharField(max_length=50, blank=False)
    description = models.TextField(blank=True)
    url = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
