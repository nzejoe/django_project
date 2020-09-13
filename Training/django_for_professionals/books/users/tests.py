from django.contrib.auth import get_user_model
from django.test import TestCase


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