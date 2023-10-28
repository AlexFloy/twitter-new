
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include
from posts.views import posts_menu


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("users.urls")),
    path('posts/', include("posts.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)