from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from chat.forms import ChatForm, SearchUserForm
from chat.models import Chat


# Send Message
@login_required
def send_message(request, receiver):
    if request.method == 'POST':
        message = request.POST.get('message')
        user = request.user
        receiver = receiver
        Chat.objects.create(
            message = message,
            user = User.objects.get(username=user),
            receiver = User.objects.get(username=receiver),
        ).save()

        return redirect(request.META['HTTP_REFERER'])
    else:
        messages.error(request, 'Error Occurred')
    return redirect(request.META['HTTP_REFERER'])


# Chat window from where Messages will be sent and received
@login_required
def chat_window(request, receiver):
    receiver = User.objects.get(username=receiver)
    queryset = (
            Chat.objects.filter(user=request.user, receiver=receiver).order_by('posted_at') |
            Chat.objects.filter(user=receiver, receiver=request.user).order_by('posted_at')
    ).distinct()
    chat_form = ChatForm()

    data = {
        'chats': queryset,
        'receiver': receiver,
        'chat_form': chat_form
    }
    return render(request=request, template_name='chat/chat_window.html', context=data)


# Chat dashboard
@login_required
def chat_dashboard(request):
    search_form = SearchUserForm()
    search = request.GET.get('search')

    if search is None or bool(search) is False:
        users = User.objects.filter().exclude(username=request.user)
    else:
        users = (
            User.objects.filter(username__icontains=search) |
            User.objects.filter(first_name__icontains=search) |
            User.objects.filter(last_name__icontains=search) |
            User.objects.filter(email__icontains=search)
        ).distinct().exclude(username=request.user)

        search_form.fields['search'].widget.attrs['placeholder'] = search

    data = {
        'users': users,
        'search_form': search_form
    }
    return render(request=request, template_name='chat/chat_dashboard.html', context=data)
