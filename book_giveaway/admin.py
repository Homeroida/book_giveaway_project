from django.contrib import admin
from .models import Author, Genre, Condition, Book

admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Condition)
admin.site.register(Book)
