from django.contrib import admin

from books.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "series", "genre", "status")
    fields = ("title", "author", "series", "genre", "status")
    search_fields = ("title", "author", "series", "genre", "status")
    ordering = ("title", "author", "series", "genre", "status")
