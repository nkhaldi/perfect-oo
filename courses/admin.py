from django.contrib import admin

from courses.models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "platform", "status")
    fields = ("title", "author", "platform", "status")
    search_fields = ("title", "author", "platform", "status")
    ordering = ("title", "author", "platform", "status")
