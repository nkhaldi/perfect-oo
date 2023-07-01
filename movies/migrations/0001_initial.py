# Generated by Django 4.2.2 on 2023-07-01 19:40

import django.db.models.deletion
from django.db import migrations, models

import utils.constants


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("authors", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Movie",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=256)),
                ("series", models.CharField(blank=True, max_length=256, null=True)),
                ("genre", models.CharField(blank=True, max_length=256, null=True)),
                (
                    "status",
                    models.CharField(
                        default=utils.constants.Status["PENDING"], max_length=128
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="authors.author"
                    ),
                ),
            ],
        ),
    ]
