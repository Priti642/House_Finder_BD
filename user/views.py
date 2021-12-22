from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.forms import PasswordResetForm
from django.core.mail import send_mail, BadHeaderError

from user.forms import RegistrationForm, LoginForm


# Login functionality
def login_view(request):
    if request.method == 'POST':
        login_form = LoginForm(request, data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"You are now logged in as {username}.")
                return redirect("home")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    login_form = LoginForm()
    return render(request=request, template_name="user/login.html", context={"login_form": login_form})


# Register Functionality
def register_view(request):
    if request.method == 'POST':
        register_form = RegistrationForm(data=request.POST)
        if register_form.is_valid():
            user = register_form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            messages.success(request, "Registration successful.")
            return redirect('home')
        messages.error(request, "Unsuccessful registration. Invalid information.")
    register_form = RegistrationForm()
    return render(request=request, template_name='user/register.html', context={'register_form': register_form})


# Logout Functionality
@login_required
def logout_view(request):
    logout(request)
    return redirect('home')


# Password Reset Functionality
def password_reset_view(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)

        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))

            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "password/password_reset_email.txt"
                    email_info = {
                        "email": user.email,
                        'domain': '127.0.0.1:8000',
                        'site_name': 'House Finder BD',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, email_info)
                    try:
                        send_mail(subject, email, 'admin@example.com', [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect("/password_reset/done/")

    password_reset_form = PasswordResetForm()
    return render(request, "password/password_reset.html", {"password_reset_form": password_reset_form})
