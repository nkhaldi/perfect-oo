from django.db import models

from status.models import Status


class Author(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.name


class Platform(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=256)
    author = models.ForeignKey(to=Author, on_delete=models.PROTECT)
    platform = models.ForeignKey(to=Platform, on_delete=models.PROTECT)
    link = models.CharField(max_length=256)
    status = models.ForeignKey(to=Status, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.title
