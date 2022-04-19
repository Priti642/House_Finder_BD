from django.urls import path
from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('', blog_dashboard, name='blog_dashboard'),
    path('save_blog/', save_blog, name='save_blog'),
    path('blog_view/<blog_id>', blog_view, name='blog_view'),
    path('blog_view/<blog_id>/edit', edit_blog, name='edit_blog'),
    path('blog_view/<blog_id>/delete', delete_blog, name='delete_blog'),
    path('save_commment/<blog_id>', save_comment, name='save_comment'),
    path('delete_comment/<comment_id>', delete_comment, name='delete_comment'),
]
