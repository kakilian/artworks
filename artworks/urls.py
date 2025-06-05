from django.urls import path
from .views import artwork_list, artwork_detail, cart_page, update_quantity, remove_item, checkout_page


urlpatterns = [
    path('', artwork_list, name='artworks_list'),         # /artworks/
    path('<int:pk>/', artwork_detail, name='artwork_detail'),  # /artworks/
    path('cart/', cart_page, name='cart_page'),  # /artworks/cart/
    path('cart/update/<int:item_id>/', update_quantity, name='update_quantity'),  # /artworks/cart/update/
    path('cart/remove/<int:item_id>/', remove_item, name='remove_item'),  # /artworks/cart/remove/
    path('checkout/', checkout_page, name='checkout_page'),  # /artworks/checkout/
]
