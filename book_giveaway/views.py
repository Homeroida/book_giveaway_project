from rest_framework import viewsets
from .models import Author, Genre, Condition, Book
from .serializers import AuthorSerializer, GenreSerializer, ConditionSerializer, BookSerializer
from .filters import BookFilter


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ConditionViewSet(viewsets.ModelViewSet):
    queryset = Condition.objects.all()
    serializer_class = ConditionSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filterset_class = BookFilter

    # Implement filtering based on parameters (author, genre, etc.)
