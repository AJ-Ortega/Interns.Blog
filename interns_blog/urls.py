from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include

from posts.views import (PostListView, PostDetailView, PostCreateView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PostListView.as_view(), name= 'list'),
    path('create/', PostCreateView.as_view(), name= 'create'),
    path('<int:pk>/', PostDetailView.as_view(), name= 'detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
