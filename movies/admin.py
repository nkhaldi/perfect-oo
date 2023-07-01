from django.contrib import admin

from movies.models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "series", "genre", "status")
    fields = ("title", "author", "series", "genre", "status")
    search_fields = ("title", "author", "series", "genre", "status")
    ordering = ("title", "author", "series", "genre", "status")
