from django.db import models
from taggit.managers import TaggableManager


class Folder(models.Model):
    name = models.CharField(max_length=200, default=None, blank=True)

    def __str__(self):
        return self.name


class Bookmark(models.Model):
    name = models.CharField(max_length=200, default=None, blank=True)
    folder_name = models.ForeignKey(Folder, on_delete=models.SET_NULL, null=True)
    url = models.URLField(max_length=230, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    tags = TaggableManager()

    def __str__(self):
        return f"{self.name} - {self.url}"
