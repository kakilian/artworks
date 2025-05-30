from django.shortcuts import render

# artworks/views.py
# Sample data for artworks
ARTWORKS = [
    # Paintings
    {
        'id': 1,
        'title': 'Blue Headscarf',
        'artist': 'Nina Petrova',
        'category': 'Painting',
        'price': 600,
        'image': 'painting-face-one.png.jpg', 
    },
    {
        'id': 2,
        'title': 'Fragmented Beauty',
        'artist': 'Leah Chen',
        'category': 'Painting',
        'price': 950,
        'image': 'painting-face-two.png.jpg',
    },
    {
        'id': 3,
        'title': 'Vivid Abstract',
        'artist': 'Omar Hassan',
        'category': 'Painting',
        'price': 500,
        'image': 'painting-one.png.jpg',
    },
        {
        'id': 4,
        'title': 'Carnival Dreams',
        'artist': 'Emily Black',
        'category': 'Painting',
        'price': 1800,
        'image': 'painting-two.png.jpg', 
    },
    {
        'id': 5,
        'title': 'Night Scene',
        'artist': 'Sophie LaRue',
        'category': 'Painting',
        'price': 1900,
        'image': 'painting-three.png.jpg'
    },
    # Sculptures
    {
        'id': 6,
        'title': 'Mannequin Circle',
        'artist': 'Alexei Sokolov',
        'category': 'Sculpture',
        'price': 1750,
        'image': 'sculptures-one.png.jpg'
    },
    {
        'id': 7,
        'title': 'Abstract Mass',
        'artist': 'Marta Novak',
        'category': 'Sculpture',
        'price': 2100,
        'image': 'sculptures-two.png.jpg'
    },
    {
        'id': 8,
        'title': 'Bronze Giant',
        'artist': 'Jonas Bauer',
        'category': 'Sculpture',
        'price': 4000,
        'image': 'sculputes-three.png.jpg'
    },
    {
        'id': 9,
        'title': 'Crowd on Stairs',
        'artist': 'Helena Torres',
        'category': 'Sculpture',
        'price': 3200,
        'image': 'sculptures-four.png.jpg'
    },
    {
        'id': 10,
        'title': 'Man with Phones',
        'artist': 'Paul Yeats',
        'category': 'Sculpture',
        'price': 1500,
        'image': 'sculptures-five.png.jpg'
    },
]

CATEGORIES = ["Painting", "Sculpture"]


def artwork_list(request):
    category = request.GET.get('category')
    if category:
        filtered_artworks = [a for a in ARTWORKS if a['category'] == category]
    else:
        filtered_artworks = ARTWORKS
  
    context = {
        'artworks': filtered_artworks,
        'categories': CATEGORIES,
        'selected_category': category,  # Highlighting current filter
    }
    return render(request, 'artworks/artworks_list.html', context)


def artwork_detail(request, pk):
    # Find the artwork by pk (id) for detail view
    artwork = next((a for a in ARTWORKS if a['id'] == pk), None)
    return render(request, 'artworks/artwork_detail.html', {'artwork': artwork})