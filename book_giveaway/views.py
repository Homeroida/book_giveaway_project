from rest_framework import viewsets
from .models import Author, Genre, Condition, Book, Interest
from .serializers import AuthorSerializer, GenreSerializer, ConditionSerializer, BookSerializer, InterestSerializer
from .filters import BookFilter
from rest_framework.decorators import action
from rest_framework.response import Response


class InterestViewSet(viewsets.ModelViewSet):
    queryset = Interest.objects.all()
    serializer_class = InterestSerializer

    @action(detail=True, methods=['POST'])
    def select_recipient(self, request, pk=None):
        interest = self.get_object()
        book_owner = interest.book.owner

        if request.user != book_owner:
            return Response({"error": "Only the book owner can select a recipient"}, status=403)

        interest.select_as_recipient()
        return Response({"message": "Recipient selected successfully"})


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
