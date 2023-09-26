from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet, GenreViewSet, ConditionViewSet, BookViewSet

router = DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'genres', GenreViewSet)
router.register(r'conditions', ConditionViewSet)
router.register(r'books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # Add authentication and registration URL patterns
]
