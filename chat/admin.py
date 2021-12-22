from django.contrib import admin
from chat.models import Chat

# Admin can access ChatModel
admin.site.register(Chat)
