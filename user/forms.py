from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


# Register form
class RegistrationForm(UserCreationForm):
    username = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'id': 'floatingUsername', 'class': 'form-control', 'placeholder': 'Username'
        }), label=False)
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'id': 'floatingFirstname', 'class': 'form-control', 'placeholder': 'First Name'
        }), label=False)
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'id': 'floatingLastname', 'class': 'form-control', 'placeholder': 'Last Name'
        }), label=False)
    email = forms.CharField(widget=forms.TextInput(
        attrs={
            'id': 'floatingEmail', 'class': 'form-control', 'placeholder': 'Email'
        }), label=False)
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'id': 'floatingPassword', 'class': 'form-control', 'placeholder': 'Password'
        }), label=False)
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'id': 'floatingPassword2', 'class': 'form-control', 'placeholder': 'Retype Password'
        }), label=False)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


# Login form
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'id': 'floatingEmail','class': 'form-control', 'placeholder': 'Username'
        }),label=False)
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'id': 'floatPassword','class': 'form-control','placeholder': 'Password'
        }), label=False)
