from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, resolve
from . forms import CustomUserCreationForm
from  . views import SignupPageView


User = get_user_model()


class CustomUserTest(TestCase):

    def test_create_user(self):
        user = User.objects.create_user(
            username = 'nzejoe',
            email = 'nzejoeworld@gmail.com',
            password = 'password',
        )

        self.assertEqual(user.username, 'nzejoe')
        self.assertEqual(user.email, 'nzejoeworld@gmail.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):

        admin_user = User.objects.create_superuser(
            username = 'adminnzejoe',
            email = 'adminnzejoeworld@gmail.com',
            password = 'adminpassword',
        )

        self.assertEqual(admin_user.username, 'adminnzejoe')
        self.assertEqual(admin_user.email, 'adminnzejoeworld@gmail.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)


class SignupPageTest(TestCase):

    def setUp(self):
        url = reverse('signup')
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'signup.html')
        self.assertContains(self.response, 'Sign Up')
        self.assertNotContains(self.response, 'Hi there! I should not be on the page.')

    def test_signup_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, CustomUserCreationForm)
        self.assertContains(self.response, 'csrfmiddlewaretoken')


    def test_signup_view(self):
        view = resolve('/accounts/signup/')
        self.assertEqual(
            view.func.__name__,
            SignupPageView.as_view().__name__
        )