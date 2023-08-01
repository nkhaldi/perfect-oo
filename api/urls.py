# api/urls.py
from django.urls import path

from .views import BookCreateView, CourseCreateView, MovieCreateView

urlpatterns = [
    path("books/", BookCreateView.as_view(), name="book-create"),
    path("movies/", MovieCreateView.as_view(), name="movie-create"),
    path("courses/", CourseCreateView.as_view(), name="course-create"),
]
