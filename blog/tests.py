import pathlib
from django.test import TestCase
from blog.models import BlogModel, BlogCommentModel
from django.contrib.auth.models import User
import tempfile


class BlogModelTest(TestCase):

    def setUp(self) -> None:
        user_ = User.objects.create(
            username="rrrrr",
            first_name="rick",
            last_name="asjidysdi",
            email="example@gmail.com",
            password="a24hellocvbc",
            is_superuser=True,
        )
        BlogModel.objects.create(
            blog_id=5,
            blog_title="tittttttle",
            text=["<h4>Proin eget tortor risus. Donec sollicitudin molestie malesuada. Cras ultricies ligula sed magna dictum porta."],
            picture=tempfile.NamedTemporaryFile(suffix=".jpg").name,
            user=user_,
        )

    def test_blog_title(self):
        b = BlogModel.objects.get(blog_id=5)
        self.assertEqual(b.blog_title, "tittttttle")

    def test_blog_text(self):
        b = BlogModel.objects.get(blog_id=5)
        self.assertEqual(b.text, "['<h4>Proin eget tortor risus. Donec sollicitudin molestie malesuada. Cras ultricies ligula sed magna dictum porta.']")

    def test_picture(self):
        b = BlogModel.objects.get(blog_id=5)
        self.assertEqual(pathlib.Path(b.picture.name).suffix, ".jpg")

    def test_string_present(self):
        b = BlogModel.objects.get(blog_id=5)
        self.assertEqual(str(b), b.blog_title)

    def test_user(self):
        b = BlogModel.objects.get(blog_id=5)
        u = User.objects.get(username="rrrrr")
        self.assertEqual(b.user, u)


class BlogCommentModelTest(TestCase):

    def setUp(self) -> None:
        user_ = User.objects.create(
            username="rrrrr",
            first_name="rick",
            last_name="asjidysdi",
            email="example@gmail.com",
            password="a24hellocvbc",
            is_superuser=True,
        )

        blog_ = BlogModel.objects.create(
            blog_id=5,
            blog_title="tittttttle",
            text=["<h4>Proin eget tortor risus."],
            picture=tempfile.NamedTemporaryFile(suffix=".jpg").name,
            user=user_,
        )

        BlogCommentModel.objects.create(
            comment_id=10,
            comment="this is okay",
            blog= blog_,
            comment_user=user_,
        )

    def test_comment(self):
        c = BlogCommentModel.objects.get(comment_id=10)
        self.assertEqual(c.comment, "this is okay")

    def test_blog_id(self):
        c = BlogCommentModel.objects.get(comment_id=10)
        self.assertEqual(c.blog.blog_id, 5)

    def test_blog_title(self):
        c = BlogCommentModel.objects.get(comment_id=10)
        self.assertEqual(c.blog.blog_title, "tittttttle")

    def test_blog_text(self):
        c = BlogCommentModel.objects.get(comment_id=10)
        self.assertEqual(c.blog.text, "['<h4>Proin eget tortor risus.']")

    def test_blog_picture(self):
        c = BlogCommentModel.objects.get(comment_id=10)
        self.assertEqual(pathlib.Path(c.blog.picture.name).suffix, ".jpg")

    def test_blog_user(self):
        c = BlogCommentModel.objects.get(comment_id=10)
        self.assertEqual(c.blog.user, c.comment_user)