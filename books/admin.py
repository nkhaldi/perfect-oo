from django.contrib import admin

from books.models import Author, Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name",)
    fields = ("name",)
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):

    list_display = ("title", "series", "author", "genre",)
    fields = ("title", "series", "author", "genre",)
    search_fields = ("title", "series", "author", "genre",)
    ordering = ("title", "series", "author", "genre",)
