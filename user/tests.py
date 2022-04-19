from django.test import TestCase
from django.contrib.auth.models import User


class UserModelTest(TestCase):

    def setUp(self) -> None:
        User.objects.create(
            username="rrrrr",
            first_name="rick",
            last_name="asjidysdi",
            email="example@gmail.com",
            password="a24hellocvbc",
            is_superuser=True,
        )

    def test_username(self):
        u = User.objects.get(username="rrrrr")
        self.assertEqual(u.username, "rrrrr")

    def test_first_name(self):
        u = User.objects.get(username="rrrrr")
        self.assertEqual(u.first_name, "rick")

    def test_last_name(self):
        u = User.objects.get(username="rrrrr")
        self.assertEqual(u.last_name, "asjidysdi")

    def test_password(self):
        u = User.objects.get(username="rrrrr")
        self.assertEqual(u.password, "a24hellocvbc")

    def test_email(self):
        u = User.objects.get(username="rrrrr")
        self.assertEqual(u.email, "example@gmail.com")

    def test_is_superuser(self):
        u = User.objects.get(username="rrrrr")
        self.assertTrue(u.is_superuser, True)

    def test_is_staff(self):
        u = User.objects.get(username="rrrrr")
        self.assertFalse(u.is_staff, True)

    def test_is_active(self):
        u = User.objects.get(username="rrrrr")
        self.assertTrue(u.is_active, False)
