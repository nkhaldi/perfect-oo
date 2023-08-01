from rest_framework import serializers

from courses.models import Author, Course, Platform
from status.models import Status


class CourseSerializer(serializers.ModelSerializer):
    author = serializers.CharField(max_length=128)
    platform = serializers.CharField(max_length=128)
    status = serializers.CharField(max_length=128)

    class Meta:
        model = Course
        fields = ("title", "author", "platform", "link", "status")

    def create(self, post_data):
        title = post_data.pop("title")
        link = post_data.pop("link", None)
        author_name = post_data.pop("author")
        platform_name = post_data.pop("platform")
        status_name = post_data.get("status", "Pending")

        author, _ = Author.objects.get_or_create(name=author_name)
        platform, _ = Platform.objects.get_or_create(name=platform_name)
        status = Status.objects.get(name=status_name) if status_name else None

        return Course.objects.create(
            title=title,
            author=author,
            platform=platform,
            link=link,
            status=status,
        )
