from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse


User = get_user_model()


class CustomUserTest(TestCase):

    def test_create_user(self):
        user = User.objects.create_user(
            username = 'nzejoe',
            email = 'nzejoe@gmail.com',
            gender = 'male'
        )

        self.assertEqual(user.username, 'nzejoe')
        self.assertEqual(user.gender, 'male')
        self.assertFalse(user.is_staff)

    def test_create_superuser(self):
        admin_user = User.objects.create_superuser(
            username = 'adminnzejoe',
            email = 'admin@gmail.com',
            date_of_birth = '1987-08-15'
        )
        self.assertEqual(admin_user.username, 'adminnzejoe')
        self.assertEqual(admin_user.date_of_birth, '1987-08-15')



class HomePageTest(TestCase):
    """This test the HomePageView"""

    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_homepage_view(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'base.html')
        self.assertContains(self.response, 'Hello')
        self.assertNotContains(self.response, "Hi, i'm not here.")