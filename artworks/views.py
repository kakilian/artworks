from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.urls import reverse

from .models import Artwork, Artist, Cart, CartItem


def artwork_list(request):
    category = request.GET.get('category')
    if category:
        filtered_artworks = Artwork.objects.filter(category=category)
    else:
        filtered_artworks = Artwork.objects.all()

    categories = Artwork.objects.values_list('category', flat=True).distinct()
    context = {
        'artworks': filtered_artworks,
        'categories': categories,
        'selected_category': category,
    }
    return render(request, 'artworks/artworks_list.html', context)


def artwork_detail(request, pk):
    artwork = get_object_or_404(Artwork, pk=pk)
    return render(request, 'artworks/artwork_detail.html', {'artwork': artwork})


@login_required
def cart_page(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    items = cart.items.select_related('artwork')

    subtotal = cart.subtotal()
    taxes = cart.taxes()
    total = cart.total()

    context = {
        'cart_items': items,
        'subtotal': f"{subtotal():.2f}",
        'taxes': f"{taxes:.2f}",
        'total': f"{total:.2f}",
    }
    return render(request, 'artworks/cart.html', context)


@login_required
@require_POST
def update_quantity(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    quantity = int(request.POST.get('quantity', 1))
    item.quantity = max(1, quantity)
    item.save()
    return redirect(reverse('cart_page'))


@login_required
@require_POST
def remove_item(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    item.delete()
    return redirect(reverse('cart_page'))


@login_required
def checkout_page(request):
    # Placeholder for checkout logic
    return render(request, 'artworks/checkout.html')