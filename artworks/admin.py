from django.contrib import admin
from django.utils.html import format_html
from .models import Artwork, Artist, Cart, CartItem

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name', 'bio')

@admin.register(Artwork)
class ArtworkAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'category', 'price', 'dimensions')
    list_filter = ('category', 'artist')
    search_fields = ('title', 'description', 'artist__name')
    readonly_fields = ('image_preview',)

    fieldsets = (
        (None, {
            'fields': ('title', 'artist', 'category', 'price', 'image', 'image_preview', 'dimensions', 'description')
        }),
    )

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 150px;" />', obj.image.url)
        return "No image"
    image_preview.short_description = 'Current Image'

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user',)

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'artwork')
