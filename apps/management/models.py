from django.db import models


class File(models.Model):
    name = models.CharField(max_length=50, blank=False)
    description = models.TextField(blank=True)
    url = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
