from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=256)


class Author(models.Model):
    name = models.CharField(max_length=256)


class Book(models.Model):
    title = models.CharField(max_length=256)
    series = models.CharField(max_length=256, blank=True, null=True)
    author = models.ForeignKey(Author, on_delete=models.PROTECT, blank=True, null=True)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT, blank=True, null=True)
