from django.test import TestCase
from django.contrib.auth.models import User
from .models import Author, Genre, Condition, Book, Interest, Photo

class UserCreationTestCase(TestCase):

    def test_create_user(self):
        # Create a user
        User.objects.create_user(username='testuser', password='testpassword')
        
        # Check if the user is created
        user = User.objects.get(username='testuser')
        self.assertEqual(user.username, 'testuser')

class BookCreationTestCase(TestCase):

    def setUp(self):
        # Create necessary objects for testing
        self.author = Author.objects.create(name='Test Author')
        self.genre = Genre.objects.create(name='Test Genre')
        self.condition = Condition.objects.create(name='Test Condition')
        self.user = User.objects.create_user(username='book_owner', password='testpassword')
        self.photo = Photo.objects.create(name='TestPhoto.jpg')  

    def test_create_book(self):
        # Create a book
        book = Book.objects.create(
            title='Test Book',
            author=self.author,
            condition=self.condition,
            owner=self.user,
            photo=self.photo  
        )
        book.genres.add(self.genre)
        
        # Check if the book is created
        created_book = Book.objects.get(title='Test Book')
        self.assertEqual(created_book.title, 'Test Book')
        self.assertEqual(created_book.author, self.author)
        self.assertTrue(self.genre in created_book.genres.all())
        self.assertEqual(created_book.condition, self.condition)
        self.assertEqual(created_book.owner, self.user)

class ShowInterestTestCase(TestCase):

    def setUp(self):
        # Create necessary objects for testing
        self.author = Author.objects.create(name='Test Author')
        self.genre = Genre.objects.create(name='Test Genre')
        self.condition = Condition.objects.create(name='Test Condition')
        self.book_owner = User.objects.create_user(username='book_owner', password='testpassword')
        self.interested_user = User.objects.create_user(username='interested_user', password='testpassword')
        self.photo = Photo.objects.create(name='InterestTestPhoto.jpg')  

        self.book = Book.objects.create(
            title='Interest Test Book',
            author=self.author,
            condition=self.condition,
            owner=self.book_owner,
            photo=self.photo  
        )
        self.book.genres.add(self.genre)

    def test_show_interest(self):
        # Create an Interest object to show interest in the book
        interest = Interest.objects.create(
            book=self.book,
            user=self.interested_user
        )
        
        # Check if the interest is recorded
        recorded_interest = Interest.objects.get(book=self.book, user=self.interested_user)
        self.assertEqual(recorded_interest.book, self.book)
        self.assertEqual(recorded_interest.user, self.interested_user)
        
        
        
class MakeDecisionTestCase(TestCase):

    def setUp(self):
        # Create necessary objects for testing
        self.author = Author.objects.create(name='Decision Test Author')
        self.genre = Genre.objects.create(name='Decision Test Genre')
        self.condition = Condition.objects.create(name='Decision Test Condition')
        self.book_owner = User.objects.create_user(username='decision_book_owner', password='testpassword')
        self.interested_user = User.objects.create_user(username='decision_interested_user', password='testpassword')
        self.photo = Photo.objects.create(name='DecisionTestPhoto.jpg')  

        self.book = Book.objects.create(
            title='Decision Test Book',
            author=self.author,
            condition=self.condition,
            owner=self.book_owner,
            photo=self.photo  
        )
        self.book.genres.add(self.genre)

        self.interest = Interest.objects.create(
            book=self.book,
            user=self.interested_user
        )

    def test_make_decision(self):
        # Make a decision on the book by selecting a recipient
        self.interest.select_as_recipient()
        
        # Check if the decision is recorded
        recorded_interest = Interest.objects.get(book=self.book, user=self.interested_user)
        self.assertTrue(recorded_interest.is_owner_selected)       