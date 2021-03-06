from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import HomePage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePage, name='home'),
    path('accounts/', include('user.urls')),
    path('blog/', include('blog.urls')),
    path('chat/', include('chat.urls')),
    path('property/', include('property.urls')),
    path('', include('post.urls')),

    path('tinymce/', include('tinymce.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
