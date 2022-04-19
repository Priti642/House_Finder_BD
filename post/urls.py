from django.urls import path
from post.views import *

app_name = 'post'

urlpatterns = [
    path('apply/', apply_to_post_property, name='apply_to_post_property'),
    path('profile/edit/', edit_profile, name='edit_profile'),
]
