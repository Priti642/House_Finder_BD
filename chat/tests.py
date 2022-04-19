from django.test import TestCase
from chat.models import Chat
from django.contrib.auth.models import User


class ChatModelTest(TestCase):

    def setUp(self) -> None:
        user_1 = User.objects.create(
            username="rrrrr",
            first_name="dfsdv",
            last_name="asjidysdi",
            email="example@gmail.com",
            password="a24hellocvbc",
        )

        user_2 = User.objects.create(
            username="cvcvvc",
            first_name="jhkhkjh",
            last_name="eresfds",
            email="example2@gmail.com",
            password="bpfcvb23fc",
        )

        Chat.objects.create(
            id=23,
            user=user_1,
            message="hoaw arte sbnfd",
            receiver=user_2,
        )

    def test_user(self):
        ch = Chat.objects.get(id=23)
        u = User.objects.get(username="rrrrr")
        self.assertEqual(ch.user, u)

    def test_message(self):
        ch = Chat.objects.get(id=23)
        self.assertEqual(ch.message, "hoaw arte sbnfd")

    def test_receiver(self):
        ch = Chat.objects.get(id=23)
        u = User.objects.get(username="cvcvvc")
        self.assertEqual(ch.receiver, u)

    def test_user_inf(self):
        ch = Chat.objects.get(id=23)
        self.assertEqual(ch.user.first_name, "dfsdv")