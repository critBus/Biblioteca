from django.apps import AppConfig
from django.db.models.signals import post_migrate


def config_app(sender, **kwargs):
    from .utils.roles_por_defecto import (
        crear_roles_django_default,
    )
    
    crear_roles_django_default()

    
class BibliotecaConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.biblioteca"
    def ready(self):
        post_migrate.connect(config_app, sender=self)