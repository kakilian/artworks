import stripe
import logging
from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib import messages

from .models import Artwork, Artist, Cart, CartItem


stripe.api_key = settings.STRIPE_SECRET_KEY


def home(request):
    return render(request, 'home.html')


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


def artist_view(request):
    artists = Artist.objects.all()
    return render(request, 'artworks/artist_list.html', {'artists': artists})


def exhibition_view(request):
    return render(request, 'artworks/exhibitions.html')


def workshop_view(request):
    return render(request, 'artworks/workshop.html')


def custom_404_view(request, exception):
    logging.warning(f"404 Error: {exception}")
    return render(request, '404.html', status=404)


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
def order_history(request):
    mock_orders = []

    if request.user.is_superuser:
        mock_orders = [
            {
                'title': 'Titanic',
                'artist': 'Billy Jones',
                'price': 100.00,
                'status': 'Shipped',
                'shipping_id': 'PP56-1234',
                'date': 'July 7, 2025',
            },
            {
                'title': 'Starry Night',
                'artist': 'Vincent van Gogh',
                'price': 250.00,
                'status': 'Delivered',
                'shipping_id': 'PP56-5678',
                'date': 'July 8, 2025',
            },
            {
                'title': 'The Scream',
                'artist': 'Edvard Munch',
                'price': 300.00,
                'status': 'Pending',
                'shipping_id': 'PP56-9101',
                'date': 'July 9, 2025',
            }
        ]

        return render(request, 'artworks/order_history.html', {'orders': mock_orders})


@login_required
def profile_view(request):
    is_artist = request.user.is_staff or request.user.is_superuser

    context = {
        'user': request.user,
        'is_artist': 'is_artist',
        'mock_orders': [
            {
                'title': 'Kill a Mockingbird',
                'artist': 'Sarah Kinred',
                'price': 150.000,
                'status': 'Deleivered',
                'shipping_id': 'PP56-1234',
                'date': 'July 5, 2025',
            },
        ] if not is_artist else [],
        'mock_artworks': [
            {
                'title': 'Sunset Print',
                'price': 400,
                'status': 'Active Listing',
            },
        ] if is_artist else [],
    }
    return render(request, 'artworks/profile.html', context)


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
        messages.info(
            request,
            'This artwork is already in your cart.',
            )  # Inform user if item is already in cart
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
