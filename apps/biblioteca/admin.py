from django.contrib import admin

# Register your models here.
from apps.biblioteca.models import *
from .reportes.para_reportes import *

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = (
        "titulo",
        "autor",
        "ubicacion",
        "genero",
        "numero_copias",
    )
    search_fields = (
        "titulo",
        "autor",
        "genero",
    )
    list_filter = (
        "autor",
        "genero",
    )
    ordering = (
        "titulo",
        "autor",
        "ubicacion",
        "genero",
        "numero_copias",
    )
    list_display_links = (
        "titulo",
        "autor",
        "ubicacion",
        "genero",
        "numero_copias",
    )
    date_hierarchy = "fecha_publicacion"


@admin.register(Revista)
class RevistaAdmin(admin.ModelAdmin):
    list_display = (
        "nombre",
        "numero",
        "ubicacion",
        "editorial",
        "numero_copias",
    )
    search_fields = (
        "nombre",
        "numero",
        "editorial",
    )
    list_filter = (
        "nombre",
        "numero",
    )
    ordering = (
        "nombre",
        "numero",
        "ubicacion",
        "editorial",
        "numero_copias",
    )
    list_display_links = (
        "nombre",
        "numero",
        "ubicacion",
        "editorial",
        "numero_copias",
    )


@admin.register(MaterialAudiovisual)
class MaterialAudiovisualAdmin(admin.ModelAdmin):
    list_display = (
        "titulo",
        "creador",
        "ubicacion",
        "productora",
        "numero_copias",
    )
    search_fields = (
        "titulo",
        "creador",
        "productora",
    )
    list_filter = (
        "titulo",
        "creador",
        "productora",
    )
    ordering = (
        "titulo",
        "creador",
        "ubicacion",
        "productora",
        "numero_copias",
    )
    list_display_links = (
        "titulo",
        "creador",
        "ubicacion",
        "productora",
        "numero_copias",
    )


@admin.register(Mobiliario)
class Mobiliario(admin.ModelAdmin):
    list_display = (
        "nombre_tipoMueble",
        "ubicacion",
        "costo_adqisicion",
        "cantidad",
    )
    search_fields = (
        "nombre_tipoMueble",
        "costo_adqisicion",
    )
    list_filter = (
        "nombre_tipoMueble",
        "costo_adqisicion",
    )
    ordering = (
        "nombre_tipoMueble",
        "ubicacion",
        "costo_adqisicion",
        "cantidad",
    )
    list_display_links = (
        "nombre_tipoMueble",
        "ubicacion",
        "costo_adqisicion",
        "cantidad",
    )


@admin.register(MuestrasMes)
class MuestrasMes(admin.ModelAdmin):
    list_display = (
        "nombre_muestra",
        "autor",
        "direccion",
    )
    search_fields = (
        "nombre_muestra",
        "autor",
    )
    list_filter = (
        "nombre_muestra",
        "autor",
    )
    ordering = (
        "nombre_muestra",
        "autor",
        "direccion",
    )
    list_display_links = (
        "nombre_muestra",
        "autor",
        "direccion",
    )
    date_hierarchy = "fecha_inicio"


@admin.register(Suscriptor)
class Suscriptor(admin.ModelAdmin):
    list_display = ("nombre", "ci", "direccion", "Telefono")
    search_fields = (
        "Telefono",
        "ci",
    )
    list_filter = (
        "ci",
        "Telefono",
    )
    ordering = ("nombre", "ci", "direccion", "Telefono")
    list_display_links = ("nombre", "ci", "direccion", "Telefono")


@admin.register(LibrosDelMes)
class LibrosDelMes(admin.ModelAdmin):
    list_display = (
        "libro",
        "fecha",
    )
    search_fields = ("fecha",)
    list_filter = ("fecha",)
    ordering = (
        "libro",
        "fecha",
    )
    list_display_links = (
        "libro",
        "fecha",
    )
    date_hierarchy = "fecha"


@admin.register(Concurso)
class Concurso(admin.ModelAdmin):
    list_display = (
        "nombre",
        "modalidad",
        "fecha_inicio",
        "fecha_cierre",
    )
    search_fields = (
        "nombre",
        "modalidad",
    )
    list_filter = (
        "fecha_inicio",
        "fecha_cierre",
    )
    ordering = (
        "nombre",
        "modalidad",
        "fecha_inicio",
        "fecha_cierre",
    )
    list_display_links = (
        "nombre",
        "modalidad",
        "fecha_inicio",
        "fecha_cierre",
    )
    date_hierarchy = "fecha_inicio"


@admin.register(Prestamo)
class Prestamo(admin.ModelAdmin):
    list_display = (
        "fecha_prestamo",
        "fecha_entrga",
        "libro",
        "suscriptor",
    )
    search_fields = (
        "fecha_prestamo",
        "fecha_entrga",
    )
    list_filter = ("suscriptor",)
    ordering = (
        "fecha_prestamo",
        "fecha_entrga",
        "libro",
        "suscriptor",
    )
    list_display_links = (
        "fecha_prestamo",
        "fecha_entrga",
        "libro",
        "suscriptor",
    )
    date_hierarchy = "fecha_prestamo"
    actions = [generar_reporte_prestamo_pdf]


@admin.register(Lecturade_libro)
class Lecturade_libro(admin.ModelAdmin):
    list_display = (
        "fecha",
        "libro",
        "suscriptor",
    )
    search_fields = ("fecha",)
    list_filter = ("suscriptor",)
    ordering = (
        "fecha",
        "libro",
        "suscriptor",
    )
    list_display_links = (
        "fecha",
        "libro",
        "suscriptor",
    )
    date_hierarchy = "fecha"

    actions = [
        generar_reporte_expediente_lectura_pdf
    ]


@admin.register(Trabajador)
class Trabajador(admin.ModelAdmin):
    list_display = ("nombre", "expediente", "direccion", "Telefono")
    search_fields = (
        "Telefono",
        "expediente",
    )
    list_filter = (
        "expediente",
        "Telefono",
    )
    ordering = ("nombre", "expediente", "direccion", "Telefono")
    list_display_links = ("nombre", "expediente", "direccion", "Telefono")


@admin.register(Inventario)
class Inventario(admin.ModelAdmin):
    list_display = ("fecha",)
    search_fields = ("fecha",)
    list_filter = ("fecha",)
    ordering = ("fecha",)
    list_display_links = ("fecha",)
    date_hierarchy = "fecha"


@admin.register(Asistencia)
class Asistencia(admin.ModelAdmin):
    list_display = (
        "fecha",
        "trabajador",
        'horas'
    )
    search_fields = ("fecha",)
    list_filter = (
        "fecha",
        "trabajador",
    )
    ordering = (
        "fecha",
        "trabajador",
    )
    list_display_links = (
        "fecha",
        "trabajador",
        'horas',
    )
    date_hierarchy = "fecha"
    actions = [
        generar_reporte_informe_asistencia_pdf
    ]
