from django.contrib import admin

from courses.models import Author, Course, Platform


@admin.register(Author)
class CourseAuthorAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    fields = ("id", "name")
    search_fields = ("id", "name")
    ordering = ("id", "name")


@admin.register(Platform)
class CoursePlatformAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    fields = ("id", "name")
    search_fields = ("id", "name")
    ordering = ("id", "name")


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author", "platform", "link", "status")
    fields = ("id", "title", "author", "platform", "link", "status")
    search_fields = ("id", "title", "author", "platform", "link", "status")
    ordering = ("id", "title", "author", "platform", "link", "status")
