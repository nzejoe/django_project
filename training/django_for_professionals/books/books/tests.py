from django.contrib.auth.models import Permission
from django.test import TestCase
from .models import Book, Review
from django.contrib.auth import get_user_model
from django.urls import reverse


class BookTest(TestCase):

    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(
            username='jayDEV',
            email='jayDEV@company.com',
            password='password'
        )
        # create user permission
        self.permission = Permission.objects.get(codename='special_status')

        # create book object
        self.book = Book.objects.create(
            title='neverland',
            author=self.user,
            price=43
        )

        # write book review
        self.review = Review.objects.create(
            book=self.book,
            review='nice book',
            author=self.user
        )
    def test_book_list_view_with_logged_in_user(self):
        self.client.login(email='jayDEV@company.com', password='password') # user login
        url = reverse('book_list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'neverland')
        self.assertTemplateUsed(response, 'books/book_list.html')

    def test_book_list_view_for_logged_out_user(self):
        self.client.logout() # logout user
        url = reverse('book_list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '%s?next=/books/' % (reverse('account_login')))
        response = self.client.get('%s?next=/books/' % (reverse('account_login')))
        self.assertContains(response, 'Log In')

    def test_user_permitted_book_detail_view(self):
        self.client.login(email='jayDEV@company.com', password='password')
        self.user.user_permissions.add(self.permission) # assign special_status permission to user
        url = self.book.get_absolute_url()
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'jayDEV')
        self.assertTemplateUsed(response, 'books/book_detail.html')
        self.assertContains(response, 'nice book') # check for reivie on book detail page vies