from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render
import os


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home/index.html'), name='home'),
    path('artworks/', include('artworks.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Always serve static files from 'main/static' during development
urlpatterns += static(settings.STATIC_URL, document_root=os.path.join(settings.BASE_DIR, 'main', 'static'))

handler404 = 'artworks.views.custom_404_view'
