from allauth.account.views import SignupView, LoginView, LogoutView
from django.urls import path, include
from .views import (
     artwork_list, artwork_detail, cart_page, update_quantity,
     remove_item, checkout_page, add_to_cart, payment_success,
     payment_cancel, create_checkout_session, artist_view, 
     exhibition_view, workshop_view, home, order_history,
     profile_view, thank_you,
)
# Namespace for the APP - Artworks, this allows us to use that same URLS in other APP stopping conflicts
app_name = 'artworks'


urlpatterns = [
    path('', artwork_list, name='artworks_list'),
    path('home/', home, name='home'),
    path('about/', home, name='about'),
    path('<int:pk>/', artwork_detail, name='artwork_detail'),
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', SignupView.as_view(), name='account_signup'),
    path('profile/', profile_view, name='profile'),
    path('artists/', artist_view, name='artist_view'),
    path('logout/', LogoutView.as_view(), name='account_logout'),
    path('orders/', order_history, name='order_history'),
    path('cart/', cart_page, name='cart_page'),
    path(
        'cart/update/<int:item_id>/',
        update_quantity,
        name='update_quantity',
    ),
    path(
        'cart/remove/<int:item_id>/',
        remove_item,
        name='remove_item',
    ),
    path('checkout/', checkout_page, name='checkout'),
    path(
        'payment/success/',
        payment_success,
        name='payment_success',
    ),
    path(
        'payment/cancel/',
        payment_cancel,
        name='payment_cancel',
    ),
    path(
        'create-checkout-session/',
        create_checkout_session,
        name='create_checkout_session',
    ),
    path(
        'add_to_cart/<int:artwork_id>/',
        add_to_cart,
        name='add_to_cart',
    ),
    path(
        'exhibition/',
        exhibition_view,
        name='exhibition_view',
    ),
    path('workshop/', workshop_view, name='workshop_view'),
    path('thank-you/', thank_you, name='thank_you'),
    path('newsletter/', include('newsletter.urls')),
]
