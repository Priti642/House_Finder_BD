from django.db import models
from django.contrib.auth import get_user_model
from tinymce.models import HTMLField

User = get_user_model()

# Blog Model
class BlogModel(models.Model):
    blog_id = models.AutoField(primary_key=True)
    blog_title = models.TextField(null=False)
    text = HTMLField()
    picture = models.ImageField(null=False, upload_to='blog_images/%Y/%m/%d/')
    time = models.DateTimeField(auto_now_add=True, null=False)
    user = models.ForeignKey(User, db_column='email', on_delete=models.CASCADE)

    # Default string representation
    def __str__(self):
        return str(self.blog_title)

# Blog Comments
class BlogCommentModel(models.Model):
    comment_id = models.AutoField(primary_key=True)
    comment = models.TextField(null=False)
    blog = models.ForeignKey(BlogModel, db_column='blog_id', on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True, null=False)
    comment_user = models.ForeignKey(User, db_column='email', on_delete=models.CASCADE)

    # Default string representation
    def __str__(self):
        return str(self.comment)
