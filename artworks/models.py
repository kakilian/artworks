from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Artwork(models.Model):
    title = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
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
