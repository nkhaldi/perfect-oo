from django.db import models

from authors.models import Author
from utils.constants import Status


class Book(models.Model):
    title = models.CharField(max_length=256)
    status = models.CharField(max_length=128, default=Status.PENDING)
    series = models.CharField(max_length=256, blank=True, null=True)
    genre = models.CharField(max_length=256, blank=True, null=True)
    author = models.ForeignKey(Author, on_delete=models.PROTECT, blank=True, null=True)
