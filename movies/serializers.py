from rest_framework import serializers

from movies.models import Author, Genre, Movie, Series
from status.models import Status


class MovieSerializer(serializers.ModelSerializer):
    author = serializers.CharField(max_length=128)
    genre = serializers.CharField(max_length=128)
    series = serializers.CharField(max_length=128)
    status = serializers.CharField(max_length=128)

    class Meta:
        model = Movie
        fields = ("title", "author", "genre", "series", "status")

    def create(self, post_data):
        title = post_data.pop("title")
        author_name = post_data.pop("author")
        genre_name = post_data.pop("genre")
        series_name = post_data.pop("series", None)
        status_name = post_data.get("status", "Pending")

        author, _ = Author.objects.get_or_create(name=author_name)
        genre, _ = Genre.objects.get_or_create(name=genre_name)
        series = Series.objects.get(name=series_name) if series_name else None
        status = Status.objects.get(name=status_name) if status_name else None

        return Movie.objects.create(
            title=title,
            author=author,
            genre=genre,
            series=series,
            status=status,
        )
