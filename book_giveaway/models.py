from django.contrib.auth.models import User
from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Condition(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genres = models.ManyToManyField(Genre)
    condition = models.ForeignKey(Condition, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=200)
    is_available = models.BooleanField(default=True)
    cover_image = models.ImageField(upload_to='media/book_covers/')

    def __str__(self):
        return self.title


class Interest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    is_owner_selected = models.BooleanField(default=False)

    def select_as_recipient(self):
        self.is_owner_selected = True
        self.save()

    def __str__(self):
        return f"{self.user.username} is interested in {self.book.title}"
