from django.shortcuts import render


def artwork_list(request):
    return render(request, 'artworks/artworks_list.html')
