from django.shortcuts import render
from .models import Artwork


def artwork_list(request):
    artworks = Artwork.objects.all()
    return render(request, 'artworks/artworks_list.html', {'artworks': artworks})
