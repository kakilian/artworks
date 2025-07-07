from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from newsletter import urls as newsletter_urls



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('about/', TemplateView.as_view(
        template_name='about.html',
        ), name='about'),
    path('accounts/', include('allauth.urls')),  # Include allauth URLs for authentication
    path(
        'artworks/',
        include(
            ('artworks.urls', 'artworks'),
            namespace='artworks',
        ),
    ),
    path('newsletter/', include('newsletter.urls', namespace='newsletter')),    
]


# register custom 404 handler
handler404 = 'artworks.views.custom_404_view'
