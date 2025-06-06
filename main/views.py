from django.shortcuts import render


def artworks_list(request):
    return render(request, 'artworks/artworks_list.html')
