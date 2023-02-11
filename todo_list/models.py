from typing import Any

from django.db import models
from django.urls import reverse


class Tag(models.Model):
    name = models.CharField(max_length=63)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self) -> Any:
        return reverse("todo:tag-list")


class Task(models.Model):
    content = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True, null=True)
    is_done = models.BooleanField()
    tags = models.ManyToManyField(to=Tag)

    class Meta:
        ordering = ["is_done", "-datetime"]

    def get_absolute_url(self) -> Any:
        return reverse("todo:task-list")
