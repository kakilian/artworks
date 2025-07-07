from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include
from django.views.generic import TemplateView
from artworks.sitemaps import StaticViewSitemap

sitemaps = {
    'static': StaticViewSitemap,
}

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
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]

handler404 = 'artworks.views.custom_404_view'
