from django import forms
from post.models import PostPropertyPermissionModel
from django.contrib.auth.models import User
from tinymce.widgets import TinyMCE


# Post Property Permission form
class PostPropertyPermissionForm(forms.ModelForm):
    phone = forms.CharField(
        required=True,
        widget=forms.NumberInput(
            attrs={
                'id': 'floatingPhone', 'class': 'form-control', 'placeholder': 'Phone number'
            },
        ),
        label='Phone number',
    )
    additional_phone = forms.CharField(
        required=True,
        widget=forms.NumberInput(
            attrs={
                'id': 'floatingAdditionalPhone', 'class': 'form-control', 'placeholder': 'Additional Phone number'
            },
        ),
        label='Additional Phone number',
    )
    bio_data = forms.CharField(
        required=True,
        widget=TinyMCE(
            attrs={
                'id': 'id_text',
            },
        ),
        min_length=10,
        label='Enter information about yourself',
    )
    facebook = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'id': 'floatingFacebook', 'class': 'form-control', 'placeholder': 'Facebook'
            }
        ),
        label='Facebook',
    )
    twitter = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'id': 'floatingTwitter', 'class': 'form-control', 'placeholder': 'Twitter'
            }
        ),
        label='Twitter',
    )
    skype = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'id': 'floatingSkype', 'class': 'form-control', 'placeholder': 'Skype'
            }
        ),
        label='Skype',
    )

    class Meta:
        model = PostPropertyPermissionModel
        fields = '__all__'
        exclude = ('user',)

    def save(self, commit=True, is_edited=False):
        save_form = super(PostPropertyPermissionForm, self).save(commit=False)
        save_form.phone = self.cleaned_data['phone']
        save_form.additional_phone = self.cleaned_data['additional_phone']
        save_form.facebook = self.cleaned_data['facebook']
        save_form.twitter = self.cleaned_data['twitter']
        save_form.skype = self.cleaned_data['skype']
        save_form.bio_data = self.cleaned_data['bio_data']

        save_form.user = self.user

        user = User.objects.get(username=self.user)
        user.is_superuser = True
        user.save()

        if commit:
            save_form.save()
            print("The form has been saved")
        return save_form
