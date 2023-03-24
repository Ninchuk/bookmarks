from django.apps import AppConfig


class ImagesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'  # noqa: BLK100
    name = 'images'

    def ready(self):
        import images.signals  # noqa F401
