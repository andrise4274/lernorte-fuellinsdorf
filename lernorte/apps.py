from django.apps import AppConfig


class LernorteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'lernorte'

    def ready(self):
        import lernorte.signals  # Import signals to connect them
