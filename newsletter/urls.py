from django.urls import path
from . import views

app_name = 'newsletter'

urlpatterns = [
    path('', views.subscribe, name='subscribe'),
    path('thank-you/', views.thank_you, name='thank_you'),
]
