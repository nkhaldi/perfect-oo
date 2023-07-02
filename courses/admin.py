from django.contrib import admin

from courses.models import Author, Course, Platform


@admin.register(Author)
class CourseAuthorAdmin(admin.ModelAdmin):
    list_display = ("name",)
    fields = ("name",)
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(Platform)
class CoursePlatformAdmin(admin.ModelAdmin):
    list_display = ("name",)
    fields = ("name",)
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "platform", "link", "status")
    fields = ("title", "author", "platform", "link", "status")
    search_fields = ("title", "author", "platform", "link", "status")
    ordering = ("title", "author", "platform", "link", "status")
