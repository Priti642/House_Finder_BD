from django.db import models
from django.contrib.auth import get_user_model
from tinymce.models import HTMLField

User = get_user_model()

# Register to post a property
class PostPropertyPermissionModel(models.Model):
    id = models.AutoField(primary_key=True)
    phone = models.CharField(max_length=20, null=False, blank=False)
    additional_phone = models.CharField(max_length=20)
    bio_data = HTMLField()
    facebook = models.CharField(max_length=100)
    twitter = models.CharField(max_length=100)
    skype = models.CharField(max_length=100)
    user = models.OneToOneField(User, db_column='email', on_delete=models.CASCADE, unique=True)
    time = models.DateTimeField(auto_now_add=True, null=False)

    # Default string representation
    def __str__(self):
        return str(self.user)+"-"+str(self.id)
