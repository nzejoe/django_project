from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Book, Review

class BookTest(TestCase):

    def setUp(self):
        # create user
        User = get_user_model()
        self.user = User.objects.create_user(
            username= 'joe',
            email= 'joe@company.com',
            password= 'password',
        )
        # create book object
        self.book = Book.objects.create(
            title= 'django for professionals',
            author= 'James',
            price= 34.00
        )
        # create book_list view
        book_list_url = reverse('book_list')
        self.book_list_response = self.client.get(book_list_url)

        # create book_detail view
        self.book_url = self.book.get_absolute_url()
        self.book_detail_response = self.client.get(self.book_url)

        # create non_url view
        self.non_url = '/books/237hee4/'
        self.non_url_response = self.client.get(self.non_url)

        # create review for book
        self.review = Review.objects.create(
            book= self.book,
            author= self.user,
            review= 'One of the best book I have read so far.',
        )

    def test_user_creation(self):
        self.assertEqual(self.user.username, 'joe')

    def test_book_create_object(self):
        self.assertEqual(self.book.title, 'django for professionals')
        self.assertEqual(self.book.price, 34.00)

    def test_book_list_view(self):
        self.assertEqual(self.book_list_response.status_code, 200)
        self.assertTemplateUsed(self.book_list_response, 'books/book_list.html')
        self.assertContains(self.book_list_response, 'django for professionals')

    def test_book_detail_view(self):
        self.assertEqual(self.book_detail_response.status_code, 200)
        self.assertTemplateUsed(self.book_detail_response, 'books/book_detail.html')
        self.assertContains(self.book_detail_response, 'James')
        self.assertContains(self.book_detail_response, 'joe')

    def test_non_url_view(self):
        self.assertEqual(self.non_url_response.status_code, 404)