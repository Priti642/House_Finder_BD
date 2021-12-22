from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from chat.forms import ChatForm
from chat.models import Chat


# Send Message
def chat_create_view(request, receiver):
    if request.method == 'POST':
        chat_form = ChatForm(request.POST)
        if chat_form.is_valid():
            chat_form.user = request.user
            chat_form.receiver = receiver
            chat_form.save()
            return redirect('chat:chat', receiver=receiver)
        else:
            messages.error(request, 'Error Occurred')
    chat_form = ChatForm()
    return render(request=request, template_name="chat/chat_form.html", context={'chat_form': chat_form})


# All Message
def chat_list_view(request, receiver):
    receiver = User.objects.get(username=receiver)
    queryset = (
            Chat.objects.filter(user=request.user, receiver=receiver).order_by('posted_at') |
            Chat.objects.filter(user=receiver, receiver=request.user).order_by('posted_at')
    ).distinct()

    data = {
        'chat': queryset,
        'receiver': receiver,
    }
    return render(request=request, template_name='chat/chat_list.html', context=data)


# Show Chat Users
def chat_users(request):
    users = User.objects.filter(is_superuser=False)
    data = {
        'users': users
    }
    return render(request=request, template_name='chat/chat_users.html', context=data)