"""Display your apps config here."""
from django.apps import AppConfig


class CatalogConfig(AppConfig):
    """Config class for app Catalog."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'catalog'
