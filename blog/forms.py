from django import forms
from blog.models import BlogModel


# Blog Form
class BlogForm(forms.ModelForm):
    text = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={},
        ),
        min_length=10,
        label='Write Here',
    )
    picture1 = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(
            attrs={},
        ),
        allow_empty_file=False,
        label='Insert 1st Photo',
    )
    picture2 = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(
            attrs={},
        ),
        allow_empty_file=False,
        label='Insert 2nd Photo',
    )
    picture3 = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(
            attrs={},
        ),
        allow_empty_file=False,
        label='Insert 3rd Photo',
    )

    class Meta:
        model = BlogModel
        fields = ('text', 'picture1', 'picture2', 'picture3')

    def save(self, commit=True):
        save_blog = super(BlogForm, self).save(commit=False)
        save_blog.text = self.cleaned_data['text']

        save_blog.picture1 = self.first_picture
        save_blog.picture2 = self.second_picture
        save_blog.picture3 = self.third_picture

        save_blog.user = self.user

        if commit:
            save_blog.save()
            print(save_blog)
            print("Form saved")
        return save_blog
