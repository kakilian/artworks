from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path(
        'about/',
        TemplateView.as_view(template_name='about.html'),
        name='about',
    ),
    path('accounts/', include('allauth.urls')),  # allauth URLs
    path(
        'artworks/',
        include(('artworks.urls', 'artworks'), namespace='artworks'),
    ),
    path('newsletter/', include('newsletter.urls', namespace='newsletter')),
]

handler404 = 'artworks.views.custom_404_view'
