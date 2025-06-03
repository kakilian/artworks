from django.shortcuts import render, get_object_or_404
from .models import Artwork, Artist


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
