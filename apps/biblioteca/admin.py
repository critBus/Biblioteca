from django.contrib import admin
from django.urls import path,reverse
from django.contrib import messages
from django.shortcuts import redirect
import traceback
# Register your models here.
from django.utils.safestring import mark_safe
from solo.admin import SingletonModelAdmin

from apps.biblioteca.models import *
from .reportes.para_reportes import *


@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    readonly_fields = ["factor_estancia", "peso"]
    list_display = (
        "titulo",
        "autor",
        "ubicacion",
        "tipo_libro",
        "genero",
        "numero_copias",
        "ilustraciones",
        "edad_minima",
        "edad_maxima",
    )
    search_fields = (
        "titulo",
        "numero_serie",
        "autor",
    )
    list_filter = (
        "autor",
        "genero",
        "materia",
        "tipo_libro",
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
        "tipo_libro",
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
class MobiliarioAdmin(admin.ModelAdmin):
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
class MuestrasMesAdmin(admin.ModelAdmin):
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
class SuscriptorAdmin(admin.ModelAdmin):
    list_display = ("nombre", "ci", "direccion", "Telefono","user")
    search_fields = (
        "Telefono",
        "ci",
    )
    list_filter = (
        "ci",
        "Telefono",
    )
    ordering = ("nombre", "ci", "direccion", "Telefono","user")
    list_display_links = ("nombre", "ci", "direccion", "Telefono","user")

    # def has_view_permission(self, request, obj=None):
    #     tiene_permiso= super().has_view_permission(request,obj)
    #     if tiene_permiso:
    #         return True
    #     return obj and obj.user.id==request.user.id


@admin.register(LibrosDelMes)
class LibrosDelMesAdmin(admin.ModelAdmin):
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
class ConcursoAdmin(admin.ModelAdmin):
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

@admin.register(PrestamoLibro)
class PrestamoLibroAdmin(admin.ModelAdmin):
    def agregar_comentario_button(self,obj):
        if obj.libro:
            url = reverse("agregar_comentario",args=[obj.libro.id])
            return mark_safe(f'<a class="button" href="{url}">Comentar</a>')
        return ""
    agregar_comentario_button.short_description = "Comentar"
    list_display = (
        "libro",
        "suscriptor",
        "devolucion",
        view_ci,
        "agregar_comentario_button"
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

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.groups.filter(name=NOMBRE_ROL_SUSCRIPTOR).exists():
            suscriptor = Suscriptor.objects.get(user=request.user)
            return qs.filter(suscriptor=suscriptor)
        return qs

    def has_add_permission(self, request):
        if request.user.groups.filter(name=NOMBRE_ROL_SUSCRIPTOR).exists():
            return False
        return super().has_add_permission(request)

    def has_change_permission(self, request, obj=None):
        if request.user.groups.filter(name=NOMBRE_ROL_SUSCRIPTOR).exists():
            return False
        return super().has_change_permission(request, obj)

    def has_delete_permission(self, request, obj=None):
        if request.user.groups.filter(name=NOMBRE_ROL_SUSCRIPTOR).exists():
            return False
        return super().has_delete_permission(request, obj)

    def save_model(self, request, obj, form, change):
        # Validación de peso máximo antes de guardar
        if obj.suscriptor and hasattr(obj.suscriptor, 'get_peso_acumulado'):
            peso_actual = obj.suscriptor.get_peso_acumulado()
            # Sumar el peso del nuevo préstamo
            if hasattr(obj, 'get_peso'):
                peso_actual += obj.get_peso()
            try:
                conf=ConfiguracionBiblio.objects.first()
                if conf:
                    print(conf)
                    peso_maximo = conf.peso_maximo
                else:
                    peso_maximo=0
            except Exception:
                print(traceback.format_exc())
                peso_maximo = 0
            if peso_actual > peso_maximo:
                self.message_user(request, f"El suscriptor excede el peso máximo permitido ({peso_maximo}). No se puede guardar el préstamo.", level=messages.ERROR)
                return
        super().save_model(request, obj, form, change)
@admin.register(PrestamoRevista)
class PrestamoRevistaAdmin(admin.ModelAdmin):
    # def agregar_comentario_button(self,obj):
    #     if obj.libro:
    #         url = reverse("agregar_comentario",args=[obj.libro.id])
    #         return mark_safe(f'<a class="button" href="{url}">Comentar</a>')
    #     return ""
    # agregar_comentario_button.short_description = "Comentar"
    list_display = (
        "revista",
        "suscriptor",
        "devolucion",
        view_ci,
        # "agregar_comentario_button"
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
        "revista",
        "suscriptor",
        "devolucion",
    )
    list_display_links = (
        "revista",
        "suscriptor",
    )
    date_hierarchy = "fecha_prestamo"

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.groups.filter(name=NOMBRE_ROL_SUSCRIPTOR).exists():
            suscriptor = Suscriptor.objects.get(user=request.user)
            return qs.filter(suscriptor=suscriptor)
        return qs

    def has_add_permission(self, request):
        if request.user.groups.filter(name=NOMBRE_ROL_SUSCRIPTOR).exists():
            return False
        return super().has_add_permission(request)

    def has_change_permission(self, request, obj=None):
        if request.user.groups.filter(name=NOMBRE_ROL_SUSCRIPTOR).exists():
            return False
        return super().has_change_permission(request, obj)

    def has_delete_permission(self, request, obj=None):
        if request.user.groups.filter(name=NOMBRE_ROL_SUSCRIPTOR).exists():
            return False
        return super().has_delete_permission(request, obj)

    def save_model(self, request, obj, form, change):
        # Validación de peso máximo antes de guardar
        if obj.suscriptor and hasattr(obj.suscriptor, 'get_peso_acumulado'):
            peso_actual = obj.suscriptor.get_peso_acumulado()
            # Sumar el peso del nuevo préstamo
            if hasattr(obj, 'get_peso'):
                peso_actual += obj.get_peso()
            try:
                conf=ConfiguracionBiblio.objects.first()
                if conf:
                    print(conf)
                    peso_maximo = conf.peso_maximo
                else:
                    peso_maximo=0
            except Exception:
                print(traceback.format_exc())
                peso_maximo = 0
            if peso_actual > peso_maximo:
                self.message_user(request, f"El suscriptor excede el peso máximo permitido ({peso_maximo}). No se puede guardar el préstamo.", level=messages.ERROR)
                return
        super().save_model(request, obj, form, change)


@admin.register(Lecturade_libro)
class Lecturade_libroAdmin(admin.ModelAdmin):
    def agregar_comentario_button(self,obj):
        if obj.libro:
            url = reverse("agregar_comentario",args=[obj.libro.id])
            return mark_safe(f'<a class="button" href="{url}">Comentar</a>')
        return ""
    agregar_comentario_button.short_description = "Comentar"
    list_display = (
        "fecha",
        "libro",
        "suscriptor",
        "agregar_comentario_button"
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

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.groups.filter(name=NOMBRE_ROL_SUSCRIPTOR).exists():
            suscriptor = Suscriptor.objects.get(user=request.user)
            return qs.filter(suscriptor=suscriptor)
        return qs

    def has_add_permission(self, request):
        if request.user.groups.filter(name=NOMBRE_ROL_SUSCRIPTOR).exists():
            return False
        return super().has_add_permission(request)

    def has_change_permission(self, request, obj=None):
        if request.user.groups.filter(name=NOMBRE_ROL_SUSCRIPTOR).exists():
            return False
        return super().has_change_permission(request, obj)

    def has_delete_permission(self, request, obj=None):
        if request.user.groups.filter(name=NOMBRE_ROL_SUSCRIPTOR).exists():
            return False
        return super().has_delete_permission(request, obj)


@admin.register(ComentarioLibro)
class ComentarioLibroAdmin(admin.ModelAdmin):
    list_display = (
        "libro",
        "suscriptor",
        "comentario",
        "puntuacion",
        "fecha"
    )
    search_fields = (
        "libro__titulo",
        "suscriptor__nombre",
        "comentario"
    )
    list_filter = (
        "puntuacion",
        "fecha",
        "libro",
        "suscriptor"
    )
    ordering = ("-fecha",)
    readonly_fields = ("fecha",)
    date_hierarchy = "fecha"

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.groups.filter(name=NOMBRE_ROL_SUSCRIPTOR).exists():
            suscriptor = Suscriptor.objects.get(user=request.user)
            return qs.filter(suscriptor=suscriptor)
        return qs

    def has_add_permission(self, request):
        return super().has_add_permission(request)

    def has_change_permission(self, request, obj=None):
        if request.user.groups.filter(name=NOMBRE_ROL_SUSCRIPTOR).exists():
            if obj is None:
                return True
            return obj.suscriptor.user == request.user
        return super().has_change_permission(request, obj)

    def has_delete_permission(self, request, obj=None):
        if request.user.groups.filter(name=NOMBRE_ROL_SUSCRIPTOR).exists():
            if obj is None:
                return True
            return obj.suscriptor.user == request.user
        return super().has_delete_permission(request, obj)


@admin.register(Trabajador)
class TrabajadorAdmin(admin.ModelAdmin):
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

revistas_view.short_description = "Revistas"

def mobiliario_view(obj):
    nombres = [v.nombre_tipoMueble for v in obj.mobiliarios.all()]
    return mark_safe("<br>\n".join(nombres))

mobiliario_view.short_description = "Mobiliario"

def audiovisual_view(obj):
    nombres = [v.titulo for v in obj.materiales_audiovisuales.all()]
    return mark_safe("<br>\n".join(nombres))

audiovisual_view.short_description = "Material Audiovisual"


@admin.register(Inventario)
class InventarioAdmin(admin.ModelAdmin):
    readonly_fields = ["fecha"]
    list_display = ("fecha",)
    date_hierarchy = "fecha"
    filter_horizontal = ("libros", "revistas", "mobiliarios", "materiales_audiovisuales")

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['ultimo_inventario'] = Inventario.objects.order_by('-fecha').first()
        print(extra_context['ultimo_inventario'])
        return super().changelist_view(request, extra_context)

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                'actualizar_inventario/',
                self.admin_site.admin_view(self.actualizar_inventario_view),
                name='actualizar-inventario',
            ),
        ]
        return custom_urls + urls

    def actualizar_inventario_view(self, request):
        try:
            # Obtener todos los objetos
            libros = Libro.objects.all()
            revistas = Revista.objects.all()
            mobiliarios = Mobiliario.objects.all()
            materiales = MaterialAudiovisual.objects.all()

            # Crear nuevo inventario
            inventario = Inventario.objects.create()
            
            # Agregar todos los objetos al inventario
            inventario.libros.set(libros)
            inventario.revistas.set(revistas)
            inventario.mobiliarios.set(mobiliarios)
            inventario.materiales_audiovisuales.set(materiales)
            
            messages.success(request, 'Inventario actualizado exitosamente.')
        except Exception as e:
            messages.error(request, f'Error al actualizar el inventario: {str(e)}')
        
        return redirect('..')

    def change_view(self, request, object_id, form_url="", extra_context=None):
        extra_context = extra_context or {}
        obj = self.get_object(request, object_id)
        if obj:
            extra_context['libros'] = obj.libros.all()
            extra_context['revistas'] = obj.revistas.all()
            extra_context['mobiliarios'] = obj.mobiliarios.all()
            extra_context['materiales_audiovisuales'] = obj.materiales_audiovisuales.all()
            extra_context['ultimo_inventario'] = Inventario.objects.order_by('-fecha').first()
            print(extra_context['ultimo_inventario'])
        return super().change_view(request, object_id, form_url, extra_context=extra_context)

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        # Obtener todos los inventarios
        inventarios = self.get_queryset(request)
        if inventarios.exists():
            # Usar el último inventario
            ultimo_inventario = inventarios.latest('fecha')
            extra_context['libros'] = ultimo_inventario.libros.all()
            extra_context['revistas'] = ultimo_inventario.revistas.all()
            extra_context['mobiliarios'] = ultimo_inventario.mobiliarios.all()
            extra_context['materiales_audiovisuales'] = ultimo_inventario.materiales_audiovisuales.all()
            extra_context['ultimo_inventario'] = Inventario.objects.order_by('-fecha').first()
            print(extra_context['ultimo_inventario'])
        return super().changelist_view(request, extra_context=extra_context)

    class Media:
        css = {
            'all': ('css/inventario_admin.css',)
        }

@admin.register(Asistencia)
class AsistenciaAdmin(admin.ModelAdmin):
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
class UsuariosEventualesAdmin(admin.ModelAdmin):
    list_display = ("user", "fecha",)
    search_fields = ("fecha",)
    list_filter = ("fecha",)
    ordering = ("fecha",)
    list_display_links = ("user", "fecha",)
    date_hierarchy = "fecha"

@admin.register(ConfiguracionBiblio)
class ConfiguracionBiblioAdmin(SingletonModelAdmin):
    pass

@admin.register(Archivo)
class ArchivoAdmin(admin.ModelAdmin):
    list_display = ("user", "fecha_inicio", "fecha_fin")
    search_fields = ("user__username", "fecha_inicio", "fecha_fin")
    list_filter = ("fecha_inicio", "fecha_fin")
    ordering = ("-fecha_fin", "user")
    list_display_links = ("user", "fecha_inicio", "fecha_fin")
    date_hierarchy = "fecha_fin"

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


@admin.register(ArchivoEntrada)
class ArchivoEntradaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "horaentrada", "horasalida")
    search_fields = ("nombre", "apellido", "ci")
    list_filter = ("ci", )
    ordering = ("-horaentrada", )
    list_display_links = ("nombre", "apellido", "horaentrada", "horasalida")
    date_hierarchy = "horaentrada"

@admin.register(LibroDigital)
class LibroDigitalAdmin(admin.ModelAdmin):
    list_display = (
        "titulo",
        "autor",
        "fecha_subida",
        "genero",
        "edad_minima",
        "edad_maxima",
    )
    search_fields = (
        "titulo",
        "autor",
        "descripcion",
    )
    list_filter = (
        "genero",
        "fecha_subida",
    )
    ordering = (
        "-fecha_subida",
        "titulo",
        "autor",
    )
    date_hierarchy = "fecha_subida"