from allauth.account.views import SignupView, LoginView, LogoutView
from django.urls import path, include
from .views import (
     artwork_list, artwork_detail, cart_page, update_quantity,
     remove_item, checkout_page, add_to_cart, payment_success,
     payment_cancel, create_checkout_session, artist_view, 
     exhibition_view, workshop_view,
)
# Namespace for the APP - Artworks, this allows us to use that same URLS in other APP stopping conflicts
app_name = 'artworks'


urlpatterns = [
    path('', artwork_list, name='artworks_list'),         # /artworks/
    path('<int:pk>/', artwork_detail, name='artwork_detail'),  # /artworks/
    path('login/', LoginView.as_view(), name='account_login'),  # /artworks/login/
    path('signup/', SignupView.as_view(), name='account_signup'),
    path('artists/', artist_view, name='artist_view'),
    path('logout/', LogoutView.as_view(), name='account_logout'),  # /artworks/logout/
    path('cart/', cart_page, name='cart_page'),  # /artworks/cart/
    path('cart/update/<int:item_id>/', update_quantity, name='update_quantity'),  # /artworks/cart/update/
    path('cart/remove/<int:item_id>/', remove_item, name='remove_item'),  # /artworks/cart/remove/
    path('checkout/', checkout_page, name='checkout'),  # /artworks/checkout/
    path('payment/success/', payment_success, name='payment_success'),  # /artworks/payment/success/
    path('payment/cancel/', payment_cancel, name='payment_cancel'),  # /artworks/payment/cancel/
    path('create-checkout-session/', create_checkout_session, name='create_checkout_session'),  # /artworks/create-checkout-session/
    path('add_to_cart/<int:artwork_id>/', add_to_cart, name='add_to_cart'),  # /artworks/add_to_cart/
    path('exhibition/', exhibition_view, name='exhibition_view'),  # /artworks/exhibition/
    path('workshop/', workshop_view, name='workshop_view'),
]
