from django.contrib import admin
from .models import Artwork, Artist, Cart, CartItem

admin.site.register(Artwork)
admin.site.register(Artist)
admin.site.register(Cart)
admin.site.register(CartItem)