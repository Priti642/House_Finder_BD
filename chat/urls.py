from django.urls import path
from chat.views import chat_list_view, chat_create_view, chat_users

app_name = 'chat'

urlpatterns = [
    # All Message
    path('chat_users/<receiver>', chat_list_view, name='chat'),
    # Send Message
    path('new/<receiver>', chat_create_view, name='new'),
    # All user option
    path('chat_users/', chat_users, name='chat_users')
]
