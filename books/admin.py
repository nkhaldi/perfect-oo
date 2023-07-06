from django.contrib import admin

from books.models import Author, Book, Genre, Series


@admin.register(Author)
class BookAuthorAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    fields = ("id", "name")
    search_fields = ("id", "name")
    ordering = ("id", "name")


@admin.register(Genre)
class BookGenreAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    fields = ("id", "name")
    search_fields = ("id", "name")
    ordering = ("id", "name")


@admin.register(Series)
class BookSeriesAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    fields = ("id", "name")
    search_fields = ("id", "name")
    ordering = ("id", "name")


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author", "genre", "series", "status")
    fields = ("id", "title", "author", "genre", "series", "status")
    search_fields = ("id", "title", "author", "genre", "series", "status")
    ordering = ("id", "title", "author", "genre", "series", "status")
