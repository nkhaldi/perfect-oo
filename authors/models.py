from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self) -> str:
        return self.name
