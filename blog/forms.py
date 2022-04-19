from django import forms
from blog.models import BlogModel, BlogCommentModel
from tinymce.widgets import TinyMCE


# Blog Form
class BlogForm(forms.ModelForm):
    blog_title = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'id': 'floatingTitle', 'class': 'form-control', 'placeholder': 'Blog Title'
            },
        ),
        min_length=10,
        label='Title',
    )

    text = forms.CharField(
        required=True,
        widget=TinyMCE(
            attrs={
                'id': 'id_text'
            },
        ),
        min_length=10,
        label='Write Here',
    )
    picture = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(
            attrs={
                'class': 'form-control', 'id': 'formFile', 'onchange': 'readImage(this)',
                'style': 'padding: 20px 20px 0'
            },
        ),
        allow_empty_file=False,
        label='Insert Picture',
    )

    class Meta:
        model = BlogModel
        fields = ('blog_title', 'text', 'picture')

    def save(self, commit=True, picture_edited=None):
        save_blog = super(BlogForm, self).save(commit=False)
        save_blog.blog_title = self.cleaned_data['blog_title']
        save_blog.text = self.cleaned_data['text']
        if picture_edited:
            save_blog.picture = self.picture
        save_blog.user = self.user

        if commit:
            save_blog.save()
        return save_blog


# Blog Comment Form
class BlogCommentForm(forms.ModelForm):

    comment = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={
                'id': 'textMessage', 'class': 'form-control', 'placeholder': 'Comment', 'rows': '8', 'cols': '45'
            },
        ),
        min_length=10,
        label='Comment',
    )

    class Meta:
        model = BlogCommentModel
        fields = ('comment',)

    def save(self, commit=True):
        save_comment = super(BlogCommentForm, self).save(commit=False)
        save_comment.blog = BlogModel.objects.get(blog_id=self.blog_id)
        save_comment.comment_user = self.user
        if commit:
            save_comment.save()
        return save_comment
