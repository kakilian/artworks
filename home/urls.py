# in home/urls.py
from django.urls import path
from django.views.generic import TemplateView
from .views import Index

urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('about/', TemplateView.as_view(template_name='home/about.html'), name='about'),
]
