from django.urls import path

from .views import *

urlpatterns = [
    path("register/", register, name="register"),
path("plantilla/", plantilla_en_blanco, name="plantilla_en_blanco"),
path("usuarios_eventuales/", tabla_usuario_eventual, name="usuarios_eventuales"),
path("addusuarios_eventuales/", agregar_usuario_eventual, name="addusuarios_eventuales"),
path("editarusuarios_eventuales/<int:id>/", editar_usuario_eventual, name="editarusuarios_eventuales"),
path("delete_usuario_eventual/<int:id>/", delete_usuario_eventual, name="delete_usuario_eventual"),
path("tabla_asistencia/", tabla_asistencia, name="tabla_asistencia"),
path("tabla_libros_mes/", tabla_libros_mes, name="tabla_libros_mes"),
path("tabla_lectura_libros/", tabla_lectura_libros, name="tabla_lectura_libros"),
path("delete_asistencia/<int:id>/", delete_asistencia, name="delete_asistencia"),
path("delete_libro_mes/<int:id>/", delete_libro_mes, name="delete_libro_mes"),
path("delete_lectura_libros/<int:id>/", delete_lectura_libros, name="delete_lectura_libros"),
    path('crear-asistencia/', crear_asistencia, name='crear_asistencia'),
    path('asistencia/editar/<int:asistencia_id>/', editar_asistencia, name='editar_asistencia'),
    path('agregar_libro_del_mes/', agregar_libro_del_mes, name='agregar_libro_del_mes'),
    path('editar_libro_del_mes/<int:libro_id>/', editar_libro_del_mes, name='editar_libro_del_mes'),
]
