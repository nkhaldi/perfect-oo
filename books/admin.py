from django.contrib import admin

from books.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "series", "author", "genre")
    fields = ("title", "series", "author", "genre")
    search_fields = ("title", "series", "author", "genre")
    ordering = ("title", "series", "author", "genre")
