from django.urls import path
from .views import artwork_list, artwork_detail

urlpatterns = [
    path('', artwork_list, name='artworks_list'),         # /artworks/
    path('<int:pk>/', artwork_detail, name='artwork_detail'),  # /artworks/3/
]
