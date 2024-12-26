from datetime import datetime

from django.apps import AppConfig
from django.db.models.signals import post_migrate

from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.contrib import messages
from django.shortcuts import redirect
from django.utils import timezone


@receiver(user_logged_in)
def check_user_condition(sender, request, user, **kwargs):
    from apps.biblioteca.models import UsuariosEventuales

    # Aquí puedes comprobar la condición que necesites
    usuario_eventual: UsuariosEventuales = UsuariosEventuales.objects.filter(
        user=user
    ).first()
    if usuario_eventual:  # Ejemplo de condición
        if not usuario_eventual.caduco:
            fecha_caducar = usuario_eventual.fecha
            hoy = timezone.now().date()

            if fecha_caducar <= hoy:
                usuario_eventual.caduco = True
                usuario_eventual.save()
            else:
                return None
        # messages.error(request, "Tu cuenta no está activa.")
        # Puedes cerrar la sesión del usuario
        from django.contrib.auth import logout
        from .models import Archivo
        if not Archivo.objects.filter(user==usuario_eventual.user).exists():
            archivo=Archivo()
            archivo.user=usuario_eventual.user
            archivo.save()
        logout(request)
        return redirect("/login/")  # Redirige a la página de login o donde necesites

    # Otras condiciones pueden ir aquí


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
