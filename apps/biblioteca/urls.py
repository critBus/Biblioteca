from django.urls import path

from .views import *

urlpatterns = [
    path("register/", register, name="register"),
path("plantilla/", plantilla_en_blanco, name="plantilla_en_blanco"),
]
