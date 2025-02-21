from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.
from django.shortcuts import render, redirect
from .forms import UserRegisterForm

from django.contrib.auth.models import User, Group
from django.core.exceptions import ObjectDoesNotExist
from .models import *


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            add_user_to_group(username=user.username, group_name=NOMBRE_ROL_SUSCRIPTOR)
            # Aquí puedes añadir una lógica adicional, como enviar un correo de confirmación
            return HttpResponseRedirect(
                "/admin/"
            )  # Redirige a la página de inicio de sesión después de registrarse
    else:
        form = UserRegisterForm()

    return render(request, "registration/register.html", {"form": form})


def add_user_to_group(username, group_name):
    try:
        # Obtén el usuario por el nombre de usuario
        user = User.objects.get(username=username)

        # Obtén el grupo por el nombre del grupo
        group = Group.objects.get(name=group_name)

        # Agrega el usuario al grupo
        user.groups.add(group)

        return f"El usuario {user.username} ha sido agregado al grupo {group.name}."

    except ObjectDoesNotExist:
        return "El usuario o el grupo no existe."
    except Exception as e:
        return f"Ocurrió un error: {str(e)}"


def plantilla_en_blanco(request):


    return render(request, "biblioteca/blank.html")