from django.contrib import admin

from books.models import Author, Book, Genre, Series


@admin.register(Author)
class BookAuthorAdmin(admin.ModelAdmin):
    list_display = ("name",)
    fields = ("name",)
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(Genre)
class BookGenreAdmin(admin.ModelAdmin):
    list_display = ("name",)
    fields = ("name",)
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(Series)
class BookSeriesAdmin(admin.ModelAdmin):
    list_display = ("name",)
    fields = ("name",)
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "series", "genre", "status")
    fields = ("title", "author", "series", "genre", "status")
    search_fields = ("title", "author", "series", "genre", "status")
    ordering = ("title", "author", "series", "genre", "status")
