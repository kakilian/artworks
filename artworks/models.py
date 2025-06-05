from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal


class Artist(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Artwork(models.Model):
    CATEGORY_CHOICES = [
        ('painting', 'Painting'),
        ('sculpture', 'Sculpture'),
    ]

    title = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default='painting'
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(
        upload_to='artwork_images/',
        blank=True, null=True)
    dimensions = models.CharField(
        max_length=100,
        blank=True,
        help_text="e.g. 60 x 80 cm")
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cart')

    def __str__(self):
        return f"Cart for {self.user.username}"

    def subtotal(self):
        return sum(item.total_price() for item in self.items.all())

    def taxes(self):
        return self.subtotal() * Decimal('0.19')


    def total(self):
        return self.subtotal() + self.taxes()


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    artwork = models.ForeignKey(Artwork, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.artwork.price  # quantity always 1, so no multiplication

    def __str__(self):
        return self.artwork.title
