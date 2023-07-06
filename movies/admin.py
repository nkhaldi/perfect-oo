from django.contrib import admin

from movies.models import Author, Genre, Movie, Series


@admin.register(Author)
class MovieAuthorAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    fields = ("id", "name")
    search_fields = ("id", "name")
    ordering = ("id", "name")


@admin.register(Genre)
class MovieGenreAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    fields = ("id", "name")
    search_fields = ("id", "name")
    ordering = ("id", "name")


@admin.register(Series)
class MovieSeriesAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    fields = ("id", "name")
    search_fields = ("id", "name")
    ordering = ("id", "name")


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author", "genre", "series", "status")
    fields = ("id", "title", "author", "genre", "series", "status")
    search_fields = ("id", "title", "author", "genre", "series", "status")
    ordering = ("id", "title", "author", "genre", "series", "status")
