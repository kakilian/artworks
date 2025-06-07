from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home/index.html'), name='home'),
    path('accounts/', include('allauth.urls')),  # Include allauth URLs for authentication
    path(
        'artworks/',
        include(
            ('artworks.urls', 'artworks'),
            namespace='artworks',
        ),
    ),
]   

# register custom 404 handler
handler404 = 'artworks.views.custom_404_view'
