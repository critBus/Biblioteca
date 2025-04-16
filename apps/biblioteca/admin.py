from django.contrib import admin
from django.urls import path
from django.contrib import messages
from django.shortcuts import redirect

# Register your models here.
from django.utils.safestring import mark_safe
from solo.admin import SingletonModelAdmin

from apps.biblioteca.models import *
from .reportes.para_reportes import *


@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    readonly_fields = ["factor_estancia"]
    list_display = (
        "titulo",
        "autor",
        "ubicacion",
        "genero",
        "numero_copias",
    )
    search_fields = (
        "titulo",
        "numero_serie"

    )
    list_filter = (
        "autor",
        "genero",
        "materia",

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
    actions = [generar_reporte_lista_libros_por_autor_pdf,generar_reporte_lista_libros_por_materia_pdf]

@admin.register(LibroInfantil)
class LibroInfantilAdmin(admin.ModelAdmin):
    readonly_fields = ["factor_estancia","peso"]
    list_display = (
        "titulo",
        "autor",
        "ubicacion",
        "ilustracioes",
        "edad_minima",
        "edad_maxima",
    )
    search_fields = (
        "titulo",
        "autor",
    )
    list_filter = ("autor",)
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
        "ilustracioes",
        "edad_minima",
        "edad_maxima",
    )
    date_hierarchy = "fecha_publicacion"
    actions = [generar_reporte_lista_libros_por_autor_pdf,generar_reporte_lista_libros_por_materia_pdf]


@admin.register(Revista)
class RevistaAdmin(admin.ModelAdmin):
    readonly_fields = ["factor_estancia", "peso"]
    list_display = (
        "nombre",
        "numero",
        "ubicacion",
        "editorial",
        "numero_copias",
    )
    search_fields = (
        "nombre",
        "numero_serie",
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

    # def has_view_permission(self, request, obj=None):
    #     tiene_permiso= super().has_view_permission(request,obj)
    #     if tiene_permiso:
    #         return True
    #     return obj and obj.user.id==request.user.id


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
    
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                'calcular-libro-mes/',
                self.admin_site.admin_view(self.calcular_libro_mes_view),
                name='calcular-libro-mes',
            ),
        ]
        return custom_urls + urls

    def calcular_libro_mes_view(self, request):
        if request.method == 'POST':
            libro_mes = calcular_libro_mes()
            if libro_mes:
                self.message_user(
                    request,
                    f'Se ha actualizado el libro del mes: {libro_mes.libro.titulo}',
                    messages.SUCCESS
                )
            else:
                self.message_user(
                    request,
                    'No se pudo determinar el libro del mes',
                    messages.ERROR
                )
        return redirect('..')

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_calcular_button'] = True
        return super().changelist_view(request, extra_context)

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False


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

def view_ci(obj):
    return obj.suscriptor.ci if obj.suscriptor else ""
view_ci.short_description="CI"
@admin.register(Prestamo)
class Prestamo(admin.ModelAdmin):
    list_display = (
        "libro",
        "revista",
        "suscriptor",
        "devolucion",
        view_ci
    )
    search_fields = (
        "fecha_prestamo",
        "fecha_entrga",
        "suscriptor__ci"
    )
    list_filter = ("suscriptor",)
    ordering = (
        "fecha_prestamo",
        "fecha_entrga",
        "libro",
        "suscriptor",
        "devolucion",
    )
    list_display_links = (
        "libro",
        "suscriptor",
    )
    date_hierarchy = "fecha_prestamo"
    actions = [generar_reporte_prestamo_pdf,generar_reporte_lista_libros_por_prestramo_pdf]


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

    actions = [generar_reporte_expediente_lectura_pdf]


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


def libros_view(obj):
    nombres = [v.titulo for v in obj.libros.all()]
    return mark_safe("<br>\n".join(nombres))


libros_view.short_description = "Libros"


def revistas_view(obj):
    nombres = [v.nombre for v in obj.revistas.all()]
    return mark_safe("<br>\n".join(nombres))


revistas_view.short_description = "Revista"


def mobiliario_view(obj):
    nombres = [v.nombre_tipoMueble for v in obj.mobiliarios.all()]
    return mark_safe("<br>\n".join(nombres))


mobiliario_view.short_description = "Mobiliario"


def audiovisual_view(obj):
    nombres = [v.titulo for v in obj.materiales_audiovisuales.all()]
    return mark_safe("<br>\n".join(nombres))


audiovisual_view.short_description = "MaterialAudiovisual"


@admin.register(Inventario)
class Inventario(admin.ModelAdmin):
    readonly_fields = ["fecha"]
    list_display = (
        "fecha",
        libros_view,
        revistas_view,
        mobiliario_view,
        audiovisual_view,
    )
    search_fields = ("fecha",)
    list_filter = (
        "fecha",
        "libros__titulo",
        "revistas__nombre",
        "mobiliarios__nombre_tipoMueble",
        "materiales_audiovisuales__titulo",
    )
    ordering = ("fecha",)
    list_display_links = ("fecha",)
    date_hierarchy = "fecha"
    filter_horizontal = [
        "libros",
        "revistas",
        "mobiliarios",
        "materiales_audiovisuales",
    ]


@admin.register(Asistencia)
class Asistencia(admin.ModelAdmin):
    list_display = ("fecha", "trabajador", "horas")
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
        "horas",
    )
    date_hierarchy = "fecha"
    actions = [generar_reporte_informe_asistencia_pdf]


@admin.register(UsuariosEventuales)
class UsuariosEventuales(admin.ModelAdmin):
    list_display = ("user", "fecha",)
    search_fields = ("fecha",)
    list_filter = ("fecha",)
    ordering = ("fecha",)
    list_display_links = ("user", "fecha",)
    date_hierarchy = "fecha"


@admin.register(ConfiguracionBiblio)
class ConfiguracionBiblio(SingletonModelAdmin):
    pass

@admin.register(Archivo)
class Archivo(admin.ModelAdmin):
    list_display = ("user",)
    ordering = ("user",)
    list_display_links = ("user",)

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('actualizar-archivo/', 
                 self.admin_site.admin_view(self.actualizar_archivo_view),
                 name='actualizar-archivo'),
        ]
        return custom_urls + urls

    def actualizar_archivo_view(self, request):
        verificar_usuarios_vencidos()
        self.message_user(request, "Se ha actualizado el archivo histórico correctamente", messages.SUCCESS)
        return redirect("..")

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_actualizar_button'] = True
        return super().changelist_view(request, extra_context)
    def has_add_permission(self, request):
        return  False

    def has_change_permission(self, request, obj=None):
        return False
