from django import forms
from chat.models import Chat
from django.contrib.auth.models import User


# Chat Form
class ChatForm(forms.ModelForm):
    message = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'id': 'id_message', 'class': 'form-control', 'placeholder': 'Type your message',
            }
        ),
        min_length=1,
        label='',
    )

    class Meta:
        model = Chat
        fields = ('message',)

    def save(self, commit=True):
        save_message = super(ChatForm, self).save(commit=False)
        save_message.user = self.user
        save_message.receiver = User.objects.get(username=self.receiver)
        save_message.message = self.cleaned_data['message']

        if commit:
            save_message.save()
        return save_message


# Chat search user
class SearchUserForm(forms.Form):
    search = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control my-3', 'placeholder': 'Search', 'type': 'text'
            }
        ),
        label=''
    )

    # def __init__(self, *args, **kwargs):
    #     self.placeholder = placeholder
    #     form = super(SearchUserForm, self).__init__(*args, **kwargs)