from django.db import models

from status.models import Status


class Author(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.name


class Series(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=256)
    author = models.ForeignKey(to=Author, on_delete=models.SET_NULL, null=True)
    genre = models.ForeignKey(to=Genre, on_delete=models.SET_NULL, null=True)
    series = models.ForeignKey(
        to=Series,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    status = models.ForeignKey(
        to=Status,
        on_delete=models.SET_NULL,
        default=Status.objects.get_or_create(name="Pending")[0].id,
        null=True,
    )

    def __str__(self) -> str:
        return self.title
