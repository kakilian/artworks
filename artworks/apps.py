from django.apps import AppConfig
import os
from django.conf import settings


class ArtworksConfig(AppConfig):
    deafult_auto_field = 'django.db.models.BigAutoField'
    name = 'artworks'

    def ready(self):
        os.makedirs(os.path.join(settings.MEDIA_ROOT, 'artwork_images'), exist_ok=True)