from django.contrib import admin

from movies.models import Author, Genre, Movie, Series


@admin.register(Author)
class MovieAuthorAdmin(admin.ModelAdmin):
    list_display = ("name",)
    fields = ("name",)
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(Genre)
class MovieGenreAdmin(admin.ModelAdmin):
    list_display = ("name",)
    fields = ("name",)
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(Series)
class MovieSeriesAdmin(admin.ModelAdmin):
    list_display = ("name",)
    fields = ("name",)
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "series", "genre", "status")
    fields = ("title", "author", "series", "genre", "status")
    search_fields = ("title", "author", "series", "genre", "status")
    ordering = ("title", "author", "series", "genre", "status")
