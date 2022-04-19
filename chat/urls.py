from django.urls import path
from chat.views import chat_window, send_message, chat_dashboard

app_name = 'chat'

urlpatterns = [
    # Chat dashboard
    path('chat_dashboard/', chat_dashboard, name='chat_dashboard'),
    # All Message
    path('chat_users/<receiver>', chat_window, name='chat_window'),
    # Send Message
    path('send_message/<receiver>', send_message, name='send_message'),

]
