from django.test import TestCase
from django.contrib.auth.models import User
from post.models import PostPropertyPermissionModel


class PostPropertyPermissionModelTest(TestCase):

    def setUp(self) -> None:
        user_ = User.objects.create(
            username="rrrrr",
            first_name="rick",
            last_name="asjidysdi",
            email="example@gmail.com",
            password="a24hellocvbc",
            is_superuser=True,
        )

        PostPropertyPermissionModel.objects.create(
            id=57,
            phone="01712312312",
            additional_phone="",
            bio_data=["<h2>Cras ultricies ligula sed magna dictum porta.</h2>"],
            facebook="https://facebook.com/test_name",
            twitter="https://twitter.com/test_name",
            skype="test_name",
            user=user_,
        )

    def test_phone(self):
        pp = PostPropertyPermissionModel.objects.get(id=57)
        self.assertEqual(pp.phone, "01712312312")

    def test_add_phone(self):
        pp = PostPropertyPermissionModel.objects.get(id=57)
        self.assertEqual(pp.additional_phone, "")

    def test_biodata(self):
        pp = PostPropertyPermissionModel.objects.get(id=57)
        self.assertEqual(pp.bio_data, "['<h2>Cras ultricies ligula sed magna dictum porta.</h2>']")

    def test_facebook(self):
        pp = PostPropertyPermissionModel.objects.get(id=57)
        self.assertEqual(pp.facebook, "https://facebook.com/test_name")

    def test_twitter(self):
        pp = PostPropertyPermissionModel.objects.get(id=57)
        self.assertEqual(pp.twitter, "https://twitter.com/test_name")

    def test_skype(self):
        pp = PostPropertyPermissionModel.objects.get(id=57)
        self.assertEqual(pp.skype, "test_name")

    def test_user(self):
        pp = PostPropertyPermissionModel.objects.get(id=57)
        self.assertEqual(pp.user.username, "rrrrr")