from django.db import models

from authors.models import Author
from utils.constants import Status


class Course(models.Model):
    title = models.CharField(max_length=256)
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    platform = models.CharField(max_length=256)
    status = models.CharField(max_length=128, default=Status.PENDING)

    def __str__(self) -> str:
        return self.title
