from rest_framework import viewsets
from .models import Author, Genre, Condition, Book, Interest, Photo
from .serializers import AuthorSerializer, GenreSerializer, ConditionSerializer, BookSerializer, InterestSerializer, PhotoSerializer
from .filters import BookFilter
from rest_framework.decorators import action
from rest_framework.response import Response

# The InterestViewSet class handles the CRUD operations for Interest objects.


class InterestViewSet(viewsets.ModelViewSet):
    queryset = Interest.objects.all()
    serializer_class = InterestSerializer

    # Custom action to handle the selection of a recipient for a book
    @action(detail=True, methods=['POST'])
    def select_recipient(self, request, pk=None):

        # Fetch the relevant Interest object and the book owner
        interest = self.get_object()
        book_owner = interest.book.owner

        # Validate that the requesting user is the book owner before proceeding
        if request.user != book_owner:
            return Response({"error": "Only the book owner can select a recipient"}, status=403)

        # Update the Interest object and return a success message
        interest.select_as_recipient()
        return Response({"message": "Recipient selected successfully"})


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer


class ConditionViewSet(viewsets.ModelViewSet):
    queryset = Condition.objects.all()
    serializer_class = ConditionSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filterset_class = BookFilter

    # Implement filtering based on parameters (author, genre, etc.)
