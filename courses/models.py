from django.db import models

from authors.models import Author
from utils.constants import Status


class Book(models.Model):
    title = models.CharField(max_length=256)
    platform = models.CharField(max_length=256)
    status = models.CharField(max_length=128, default=Status.PENDING)
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
