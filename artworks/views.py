import stripe
from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib import messages

from .models import Artwork, Artist, Cart, CartItem


stripe.api_key = settings.STRIPE_SECRET_KEY


def artwork_list(request):
    category = request.GET.get('category')
    artist_id = request.GET.get('artist')
    price_min = request.GET.get('price_min')
    price_max = request.GET.get('price_max')
    sort = request.GET.get('sort')

    artworks = Artwork.objects.all()

    if category:
        artworks = artworks.filter(category=category)

    if artist_id:
        artworks = artworks.filter(artist_id=artist_id)

    if price_min:
        artworks = artworks.filter(price__gte=price_min)

    if price_max:
        artworks = artworks.filter(price__lte=price_max)

    if sort == 'popular':
        artworks = artworks.order_by('-price')  # example popular logic
    else:
        artworks = artworks.order_by('-id')  # newest first

    categories = Artwork.objects.values_list('category', flat=True).distinct()
    artists = Artist.objects.all()

    context = {
        'artworks': artworks,
        'categories': categories,
        'artists': artists,
        'selected_category': category,
    }
    return render(request, 'artworks/artworks_list.html', context)


def artwork_detail(request, pk):
    artwork = get_object_or_404(Artwork, pk=pk)
    return render(request, 'artworks/artwork_detail.html', {'artwork': artwork})


def custom_404_view(request, _exception):
    return render(request, 'artworks:404.html', status=404)


@login_required
@csrf_exempt
def create_checkout_session(request):
    if request.method == 'POST':
        try:
            cart = Cart.objects.get(user=request.user)
            line_items = []
            for item in cart.items.all():
                line_items.append({
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {
                            'name': item.artwork.title,
                        },
                        'unit_amount': int(item.artwork.price * 100),
                    },
                    'quantity': item.quantity,
                })

            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=line_items,
                mode='payment',
                success_url=request.build_absolute_uri('/artworks/payment/success/'),
                cancel_url=request.build_absolute_uri('/artworks/payment/cancel/'),
            )
            return JsonResponse({'id': checkout_session.id})
        except Exception as e:
            return JsonResponse({'error': str(e)})


@login_required
def cart_page(request):
    cart, _ = Cart.objects.get_or_create(user=request.user)
    items = cart.items.select_related('artwork')

    subtotal = cart.subtotal()
    taxes = cart.taxes()
    total = cart.total()

    context = {
        'cart_items': items,
        'subtotal': f"{subtotal:.2f}",
        'taxes': f"{taxes:.2f}",
        'total': f"{total:.2f}",
    }
    return render(request, 'artworks/cart.html', context)


@login_required
@require_POST
def add_to_cart(request, artwork_id):
    artwork = get_object_or_404(Artwork, id=artwork_id)
    cart, _ = Cart.objects.get_or_create(user=request.user)
    if cart.items.filter(artwork=artwork).exists():
        messages.info(request, 'This artwork is already in your cart.') # Inform user if item is already in cart
    else:
        # Create a new cart item if it doesn't already exist    
        cart.items.create(artwork=artwork)
        messages.success(request, f'Added "{artwork.title}" to your cart.')
        
    return redirect('artworks:cart_page')


@login_required
@require_POST
def update_quantity(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    quantity = int(request.POST.get('quantity', 1))
    item.quantity = max(1, quantity)
    item.save()
    return redirect('artworks:cart_page')


@login_required
@require_POST
def remove_item(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    item.delete()
    return redirect('artworks:cart_page')


@login_required
def checkout_page(request):
    cart = get_object_or_404(Cart, user=request.user)
    items = cart.items.select_related('artwork')

    subtotal = cart.subtotal()
    taxes = cart.taxes()
    total = cart.total()

    context = {
        'cart_items': items,
        'subtotal': f"{subtotal:.2f}",
        'taxes': f"{taxes:.2f}",
        'total': f"{total:.2f}",
        'stripe_publishable_key': settings.STRIPE_PUBLISHABLE_KEY,
    }
    return render(request, 'artworks/checkout.html', context)


@login_required
def payment_success(request):
    return render(request, 'artworks/success.html')


@login_required
def payment_cancel(request):
    return render(request, 'artworks/cancel.html')


def my_view(request):
    messages.success(request, "You did the thing successfully!")
