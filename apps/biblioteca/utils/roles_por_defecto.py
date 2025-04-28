from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission


from config.utils.utils_permission import crear_rol
from django_reportbroD.models import ReportDefinition, ReportRequest
from ..models import *

User = get_user_model()


def crear_roles_django_default():
    crear_rol(
        lista_modelos=[],
        lista_modelos_solo_update=[],
        lista_modelos_solo_create=[],
        lista_modelos_solo_view=[
            Libro,
            Revista,
            MaterialAudiovisual,
            Concurso,
            MuestrasMes,
            LibrosDelMes,
            PrestamoLibro,
            Lecturade_libro,
        ],
        nombre_rol=NOMBRE_ROL_SUSCRIPTOR,
    )
    crear_rol(
        lista_modelos=[
            Libro,
            Revista,
            MaterialAudiovisual,
            Concurso,
            MuestrasMes,
            LibrosDelMes,
            PrestamoLibro,
            Lecturade_libro,
            Inventario,
            Mobiliario,
            Suscriptor,
            Trabajador,
            Asistencia,
        ],
        lista_modelos_solo_update=[],
        lista_modelos_solo_create=[],
        lista_modelos_solo_view=[],
        nombre_rol=NOMBRE_ROL_BIBLIOTECARIO,
    )
    crear_rol(
        lista_modelos=[

            ReportRequest,
            ReportDefinition,
            User,
            Group,
            Permission,
        ],
        lista_modelos_solo_update=[],
        lista_modelos_solo_create=[],
        lista_modelos_solo_view=[
            Libro,
            Revista,
            MaterialAudiovisual,
            Concurso,
            MuestrasMes,
            LibrosDelMes,
            PrestamoLibro,
            Lecturade_libro,
            Inventario,
            Mobiliario,
            Suscriptor,
            Trabajador,
            Asistencia,
        ],
        nombre_rol=NOMBRE_ROL_ADMINISTRADOR,
    )
