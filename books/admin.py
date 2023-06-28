from django.contrib import admin

from books.models import Author, Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = "__all__"
    fields = "__all__"
    search_fields = "__all__"
    ordering = ("name",)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = "__all__"
    fields = "__all__"
    search_fields = "__all__"
    ordering = ("title", "author", "series", "genre")
