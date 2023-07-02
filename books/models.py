from django.db import models

from authors.models import Author
from utils.constants import Status


class Book(models.Model):
    title = models.CharField(max_length=256)
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    series = models.CharField(max_length=256, blank=True, null=True)
    genre = models.CharField(max_length=256, blank=True, null=True)
    status = models.CharField(max_length=128, default=Status.PENDING)

    def __str__(self) -> str:
        return self.title
