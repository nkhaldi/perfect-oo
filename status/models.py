from django.db import models


class Status(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.name
