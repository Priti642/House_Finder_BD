from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


# returns a URL
def get_absolute_url():
    return reverse('chat:chat')


# ChatModel
class Chat(models.Model):
    id = models.AutoField(primary_key=True),
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    message = models.TextField()
    posted_at = models.DateTimeField(auto_now=True)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')

    # Default string representation
    def __str__(self):
        return str(self.message)
