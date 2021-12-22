from django.urls import path
from blog.views import save_blog, blog_dashboard, blog_view


urlpatterns = [
    path('', blog_dashboard, name='blog'),
    path('save_blog/', save_blog, name='save_blog'),
    path('blog_view/<blog_id>', blog_view, name='blog_view')
]
