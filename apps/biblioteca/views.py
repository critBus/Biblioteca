from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django import forms
# Create your views here.
from django.shortcuts import render, redirect
from .forms import UserRegisterForm
import datetime
from django.contrib.auth.models import  Group
from django.core.exceptions import ObjectDoesNotExist
from .models import *
from django.http import HttpResponse
from django.views.generic import DetailView, TemplateView
from django.contrib import admin
User=get_user_model()

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

def tabla_usuario_eventual(request):
    usuarios=UsuariosEventuales.objects.all()
    datos={
        "usuarios":[{
            "nombre": usuario.user.username,
            "fecha":usuario.fecha.strftime('%Y-%m-%d'),
            "caduco": "Si" if usuario.caduco else "No",
            "id":usuario.id
        } for usuario in usuarios]
    }
    return render(request, "biblioteca/tablaUsuariosEventuales.html",datos)

def get_fecha_de_request(request,key):
    try:
        fecha = request.POST.get(key, '')
        if fecha != "":
            fecha=datetime.date.fromisoformat(fecha)
            return fecha
    except:
        print("error")
    return ""

def agregar_usuario_eventual(request):
    mensaje_de_error=""
    if request.method == 'POST':
        nombre = request.POST.get('nombre', '')
        fecha = get_fecha_de_request(request,'fecha')
        caduco = request.POST.get('caduco', False) == 'on'
        if (
            nombre.strip()==""
            or fecha==""

        ):
            mensaje_de_error="Los campos nombre fecha y caduco no pueden estar vacios"
        else:
            usuario=User.objects.filter(username=nombre).first()
            if not usuario:
                mensaje_de_error = "Este usuario no existe"
            else:
                UsuariosEventuales.objects.create(
                    user=usuario,
                    fecha=fecha,
                    caduco=caduco
                )
                return tabla_usuario_eventual(request)

    return render(request, "biblioteca/agrgarUsuarioEventual.html",{
        "mensaje_de_error":mensaje_de_error
    })


def editar_usuario_eventual(request, id):
    mensaje_de_error = ""
    e = UsuariosEventuales.objects.filter(id=id).first()
    if request.method == 'POST':
        nombre = request.POST.get('nombre', '')
        fecha = get_fecha_de_request(request,'fecha')
        caduco = request.POST.get('caduco', False) == 'on'
        if (
            nombre.strip()==""
            or fecha==""

        ):
            mensaje_de_error="Los campos nombre fecha y caduco no pueden estar vacios"
        else:
            usuario=User.objects.filter(username=nombre).first()
            if not usuario:
                mensaje_de_error = "Este usuario no existe"
            else:
                e.user=usuario
                e.fecha=fecha
                e.caduco=caduco
                e.save()
                return tabla_usuario_eventual(request)
    fecha=e.fecha.strftime('%Y-%m-%d')
    print(fecha)
    return render(request, "biblioteca/editarUsuarioEventual.html", {
        "elemento": {
            "nombre":e.user.username,
            "fecha":fecha,
            "caduco":e.caduco
        },
        "mensaje_de_error": mensaje_de_error
    })

def delete_usuario_eventual(request, id):
    UsuariosEventuales.objects.filter(id=id).delete()
    return tabla_usuario_eventual(request)

def tabla_lectura_libros(request):
    if request.user.groups.filter(name=NOMBRE_ROL_SUSCRIPTOR).exists():
        # Si es suscriptor, obtener el objeto Suscriptor relacionado
        suscriptor = Suscriptor.objects.get(user=request.user)
        # Filtrar solo las lecturas del suscriptor actual
        lecturas = Lecturade_libro.objects.filter(suscriptor=suscriptor)
    else:
        # Si no es suscriptor, mostrar todas las lecturas (para bibliotecarios y administradores)
        lecturas = Lecturade_libro.objects.all()
    
    datos = {
        "lecturas": [{
            "suscriptor": lectura.suscriptor.nombre,
            "libro": lectura.libro.titulo,
            "fecha": lectura.fecha.strftime('%Y-%m-%d'),
            "id": lectura.id
        } for lectura in lecturas]
    }
    return render(request, "biblioteca/tabla_lectura_libros.html", datos)

def delete_lectura_libros(request, id):
    Lecturade_libro.objects.filter(id=id).delete()
    return tabla_lectura_libros(request)

def tabla_libros_mes(request):
    libros_mes=LibrosDelMes.objects.all()
    datos={
        "libros":[{
            "libro" : libro_mes.libro.titulo,
            "fecha":libro_mes.fecha.strftime('%Y-%m-%d'),
            "id":libro_mes.id
        } for libro_mes in libros_mes]
    }
    return render(request, "biblioteca/tabla_libros_mes.html",datos)

def delete_libro_mes(request, id):
    LibrosDelMes.objects.filter(id=id).delete()
    return tabla_libros_mes(request)

def tabla_asistencia(request):
    asistencias=Asistencia.objects.all()
    datos={
        "asistencias":[{
            "trabajador" : asistencia.trabajador.nombre,
            "fecha":asistencia.fecha.strftime('%Y-%m-%d'),
            "id":asistencia.id
        } for asistencia in asistencias]
    }
    return render(request, "biblioteca/tabla_asistencia.html",datos)

def delete_asistencia(request, id):
    Asistencia.objects.filter(id=id).delete()
    return tabla_asistencia(request)


class AsistenciaForm(forms.ModelForm):
    class Meta:
        model = Asistencia
        fields = ['fecha', 'trabajador', 'horas']


def crear_asistencia(request):
    if request.method == 'POST':
        form = AsistenciaForm(request.POST)
        if form.is_valid():
            form.save()
            return tabla_asistencia(request)  # Redirige a una página de éxito o a donde prefieras
    else:
        form = AsistenciaForm()

    return render(request, 'biblioteca/crear_asistencia.html', {'form': form})

class AsistenciaEditForm(forms.ModelForm):
    class Meta:
        model = Asistencia
        fields = ['fecha', 'trabajador', 'horas']
        widgets = {
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'trabajador': forms.Select(attrs={'class': 'form-control'}),
            'horas': forms.NumberInput(attrs={'class': 'form-control'}),
        }


def editar_asistencia(request, asistencia_id):
    asistencia = get_object_or_404(Asistencia, id=asistencia_id)

    if request.method == 'POST':
        form = AsistenciaEditForm(request.POST, instance=asistencia)
        if form.is_valid():
            form.save()
            return tabla_asistencia(request)  # Cambia esto a tu URL de redirección deseada
    else:
        form = AsistenciaEditForm(instance=asistencia)

    return render(request, 'biblioteca/editar_asistencia.html', {'form': form, 'asistencia': asistencia,
                                                                 'fecha':asistencia.fecha.strftime('%Y-%m-%d')})

class LibrosDelMesForm(forms.ModelForm):
    class Meta:
        model = LibrosDelMes
        fields = ['libro', 'fecha']

def agregar_libro_del_mes(request):
    if request.method == 'POST':
        form = LibrosDelMesForm(request.POST)
        if form.is_valid():
            form.save()
            return tabla_libros_mes(request)  # Redirige a la lista de libros del mes o a donde desees
    else:
        form = LibrosDelMesForm()

    return render(request, 'biblioteca/agregar_libro_del_mes.html', {'form': form})

class LibrosDelMesEditForm(forms.ModelForm):
    class Meta:
        model = LibrosDelMes
        fields = ['libro', 'fecha']  # Asegúrate de incluir todos los campos que deseas editar

def editar_libro_del_mes(request, libro_id):
    libro_del_mes = get_object_or_404(LibrosDelMes, id=libro_id)

    if request.method == 'POST':
        form = LibrosDelMesEditForm(request.POST, instance=libro_del_mes)
        if form.is_valid():
            form.save()
            return tabla_libros_mes(request)  # Cambia esto por el nombre de la vista a la que deseas redirigir
    else:
        form = LibrosDelMesEditForm(instance=libro_del_mes)

    return render(request, 'biblioteca/editar_libro_del_mes.html', {'form': form,
                                                                    'libro_del_mes': libro_del_mes,
                                                                    'fecha':libro_del_mes.fecha.strftime('%Y-%m-%d')})

class ComentarioLibroForm(forms.ModelForm):
    class Meta:
        model = ComentarioLibro
        fields = ['comentario', 'puntuacion']
        widgets = {
            'comentario': forms.Textarea(attrs={'class': 'form-control'}),
            'puntuacion': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 5}),
        }

def tabla_comentarios(request):
    comentarios = ComentarioLibro.objects.all().order_by('-fecha')
    datos = {
        **admin.site.each_context(request),
        "comentarios": [{
            "libro": comentario.libro.titulo,
            "suscriptor": comentario.suscriptor.nombre,
            "comentario": comentario.comentario,
            "puntuacion": "★" * comentario.puntuacion,
            "fecha": comentario.fecha.strftime('%Y-%m-%d %H:%M'),
            "id": comentario.id,
            "libro_id": comentario.libro.id
        } for comentario in comentarios]
    }
    return render(request, "biblioteca/tabla_comentarios.html", datos)

def agregar_comentario(request, libro_id):
    print(f"libro_id {libro_id}")
    libro = Libro.objects.filter(id=libro_id).first()
    print(f"request.user {request.user.username}")
    suscriptor = Suscriptor.objects.filter(user=request.user).first()
    # libro = get_object_or_404(Libro, id=libro_id)
    # suscriptor = get_object_or_404(Suscriptor, user=request.user)
    
    # Verificar si ya existe un comentario
    comentario_existente = ComentarioLibro.objects.filter(libro=libro, suscriptor=suscriptor).first()
    
    if request.method == 'POST':
        if comentario_existente:
            form = ComentarioLibroForm(request.POST, instance=comentario_existente)
        else:
            form = ComentarioLibroForm(request.POST)
            
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.libro = libro
            comentario.suscriptor = suscriptor
            comentario.save()
            # /admin/biblioteca/prestamo/
            return HttpResponseRedirect("/admin/biblioteca/comentariolibro/")
            
    else:
        if comentario_existente:
            form = ComentarioLibroForm(instance=comentario_existente)
        else:
            form = ComentarioLibroForm()
    
    return render(request, "biblioteca/agregar_comentario.html", {
        **admin.site.each_context(request),
        'form': form,
        'libro': libro,
        'suscriptor': suscriptor
    })

def tabla_prestamos(request):
    if request.user.groups.filter(name=NOMBRE_ROL_SUSCRIPTOR).exists():
        # Si es suscriptor, obtener el objeto Suscriptor relacionado
        suscriptor = Suscriptor.objects.get(user=request.user)
        # Filtrar solo los préstamos del suscriptor actual
        prestamos_libros = PrestamoLibro.objects.filter(suscriptor=suscriptor)
        prestamos_revistas = PrestamoRevista.objects.filter(suscriptor=suscriptor)
    else:
        # Si no es suscriptor, mostrar todos los préstamos (para bibliotecarios y administradores)
        prestamos_libros = PrestamoLibro.objects.all()
        prestamos_revistas = PrestamoRevista.objects.all()
    
    datos = {
        "prestamos": []
    }
    
    for prestamo in prestamos_libros:
        datos["prestamos"].append({
            "tipo": "Libro",
            "suscriptor": prestamo.suscriptor.nombre,
            "item": prestamo.libro.titulo if prestamo.libro else "",
            "fecha_prestamo": prestamo.fecha_prestamo.strftime('%Y-%m-%d'),
            "fecha_entrega": prestamo.fecha_entrga.strftime('%Y-%m-%d'),
            "devolucion": "Si" if prestamo.devolucion else "No",
            "id": prestamo.id
        })
    
    for prestamo in prestamos_revistas:
        datos["prestamos"].append({
            "tipo": "Revista",
            "suscriptor": prestamo.suscriptor.nombre,
            "item": prestamo.revista.nombre if prestamo.revista else "",
            "fecha_prestamo": prestamo.fecha_prestamo.strftime('%Y-%m-%d'),
            "fecha_entrega": prestamo.fecha_entrga.strftime('%Y-%m-%d'),
            "devolucion": "Si" if prestamo.devolucion else "No",
            "id": prestamo.id
        })
    
    return render(request, "biblioteca/tabla_prestamos.html", datos)

def delete_prestamo(request, id):
    PrestamoLibro.objects.filter(id=id).delete()
    return redirect('tabla_prestamos')

from django.db.models import Count, Avg
from django.contrib.auth.decorators import login_required

def get_top_books(queryset, limit=5):
    """Obtiene los mejores libros basados en puntuación y popularidad"""
    return queryset.annotate(
        avg_rating=Avg('comentariolibro__puntuacion'),
        num_prestamos=Count('prestamolibro'),
        num_lecturas=Count('lecturade_libro')
    ).order_by('-avg_rating', '-num_prestamos', '-num_lecturas')[:limit]

@login_required
def asistente_paso1(request):
    """Primera pregunta: País de origen"""
    # Obtener países únicos que tienen libros
    paises = Libro.objects.values_list('pais', flat=True).distinct().exclude(pais='')
    
    if request.method == 'POST':
        pais = request.POST.get('pais')
        if pais:
            # Guardar selección en sesión
            request.session['filtro_pais'] = pais
            return redirect('asistente_paso2')
    

    return render(request, 'biblioteca/asistente/paso1.html', {
        **admin.site.each_context(request),
        'paises': paises
    })

@login_required
def asistente_paso2(request):
    """Segunda pregunta: Género literario"""
    pais = request.session.get('filtro_pais')
    if not pais:
        return redirect('asistente_paso1')
    
    # Obtener géneros disponibles para el país seleccionado
    generos = Libro.objects.filter(pais=pais).values_list('genero', flat=True).distinct().exclude(genero='')
    
    if request.method == 'POST':
        genero = request.POST.get('genero')
        if genero:
            request.session['filtro_genero'] = genero
            return redirect('asistente_paso3')
    
    return render(request, 'biblioteca/asistente/paso2.html', {
        **admin.site.each_context(request),
        'generos': generos,
        'pais_seleccionado': pais
    })

@login_required
def asistente_paso3(request):
    """Tercera pregunta: Editorial"""
    pais = request.session.get('filtro_pais')
    genero = request.session.get('filtro_genero')
    if not (pais and genero):
        return redirect('asistente_paso1')
    
    # Obtener editoriales disponibles según filtros previos
    editoriales = Libro.objects.filter(
        pais=pais,
        genero=genero
    ).values_list('editorial', flat=True).distinct().exclude(editorial='')
    
    if request.method == 'POST':
        editorial = request.POST.get('editorial')
        if editorial:
            request.session['filtro_editorial'] = editorial
            return redirect('asistente_paso4')
    
    return render(request, 'biblioteca/asistente/paso3.html', {
        **admin.site.each_context(request),
        'editoriales': editoriales,
        'pais_seleccionado': pais,
        'genero_seleccionado': genero
    })

@login_required
def asistente_paso4(request):
    """Cuarta pregunta: Materia/Tema"""
    pais = request.session.get('filtro_pais')
    genero = request.session.get('filtro_genero')
    editorial = request.session.get('filtro_editorial')
    if not (pais and genero and editorial):
        return redirect('asistente_paso1')
    
    # Obtener materias disponibles según filtros previos
    materias = Libro.objects.filter(
        pais=pais,
        genero=genero,
        editorial=editorial
    ).values_list('materia', flat=True).distinct().exclude(materia='')
    
    if request.method == 'POST':
        materia = request.POST.get('materia')
        if materia:
            request.session['filtro_materia'] = materia
            return redirect('asistente_paso5')
    
    return render(request, 'biblioteca/asistente/paso4.html', {
        **admin.site.each_context(request),
        'materias': materias,
        'pais_seleccionado': pais,
        'genero_seleccionado': genero,
        'editorial_seleccionada': editorial
    })

@login_required
def asistente_paso5(request):
    """Quinta pregunta: Ilustraciones"""
    pais = request.session.get('filtro_pais')
    genero = request.session.get('filtro_genero')
    editorial = request.session.get('filtro_editorial')
    materia = request.session.get('filtro_materia')
    if not (pais and genero and editorial and materia):
        return redirect('asistente_paso1')
    
    if request.method == 'POST':
        ilustraciones = request.POST.get('ilustraciones')
        if ilustraciones in ['true', 'false', '']:
            request.session['filtro_ilustraciones'] = ilustraciones
            return redirect('resultados_recomendaciones')
    # Construir el queryset base
    cantidad_sin_ilustraciones = Libro.objects.filter(
        pais=pais,
        genero=genero,
        editorial=editorial,
        materia=materia,
        ilustraciones=False
    ).count()

    cantidad_con_ilustraciones = Libro.objects.filter(
        pais=pais,
        genero=genero,
        editorial=editorial,
        materia=materia,
        ilustraciones=True
    ).count()


    return render(request, 'biblioteca/asistente/paso5.html', {
        **admin.site.each_context(request),
        'pais_seleccionado': pais,
        'genero_seleccionado': genero,
        'editorial_seleccionada': editorial,
        'materia_seleccionada': materia,
        "cantidad_sin_ilustraciones": cantidad_sin_ilustraciones,
        "cantidad_con_ilustraciones": cantidad_con_ilustraciones,
    })

@login_required
def resultados_recomendaciones(request):
    """Muestra los resultados finales basados en todos los filtros"""
    # Recuperar todos los filtros de la sesión
    filtros = {
        'pais': request.session.get('filtro_pais'),
        'genero': request.session.get('filtro_genero'),
        'editorial': request.session.get('filtro_editorial'),
        'materia': request.session.get('filtro_materia'),
        'ilustraciones': request.session.get('filtro_ilustraciones')
    }
    
    # Verificar que tengamos todos los filtros necesarios
    if not all([filtros['pais'], filtros['genero'], filtros['editorial'], filtros['materia']]):
        return redirect('asistente_paso1')
    
    # Construir el queryset base
    libros = Libro.objects.filter(
        pais=filtros['pais'],
        genero=filtros['genero'],
        editorial=filtros['editorial'],
        materia=filtros['materia']
    )
    
    # Aplicar filtro de ilustraciones si se especificó
    if filtros['ilustraciones'] in ['true', 'false']:
        libros = libros.filter(ilustraciones=filtros['ilustraciones'] == 'true')
    
    # Obtener los mejores libros según puntuación y popularidad
    libros_recomendados = libros.annotate(
        avg_rating=Avg('comentariolibro__puntuacion'),
        num_prestamos=Count('prestamolibro'),
        num_lecturas=Count('lecturade_libro')
    ).order_by('-avg_rating', '-num_prestamos', '-num_lecturas')
    rankings=[int(libro.avg_rating) for libro in libros_recomendados]
    # Limpiar los filtros de la sesión
    for key in list(request.session.keys()):
        if key.startswith('filtro_'):
            del request.session[key]
    
    return render(request, 'biblioteca/asistente/resultados.html', {
        **admin.site.each_context(request),
        'libros': libros_recomendados,
        'filtros': filtros,
        "rankings":rankings
    })

class LibroDigitalDetailView(DetailView):
    model = LibroDigital
    template_name = 'biblioteca/libro_digital_detail.html'
    context_object_name = 'libro'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pdf_url'] = self.object.archivo_pdf.url
        context['pdf']=self.object.archivo_pdf
        print(context['pdf'].url)
        return context

def mis_datos(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    try:
        suscriptor = Suscriptor.objects.get(user=request.user)
        datos = {
             **admin.site.each_context(request),
            'suscriptor': {
                'nombre': suscriptor.nombre,
                'edad': suscriptor.edad,
                'sexo': suscriptor.sexo,
                'telefono': suscriptor.Telefono,
                'ci': suscriptor.ci,
                'centro_trabajo': suscriptor.centro_trabajo,
                'ocupacion': suscriptor.ocupacion,
                'direccion': suscriptor.direccion,
                'sindicato': 'Sí' if suscriptor.sindicato else 'No',
                'nivel_escolar': suscriptor.nivel_escolar,
            },
            'usuario': {
                'username': request.user.username,
                'email': request.user.email,
                'first_name': request.user.first_name,
                'last_name': request.user.last_name,
                # 'date_joined': request.user.date_joined.strftime('%Y-%m-%d'),
                # 'last_login': request.user.last_login.strftime('%Y-%m-%d %H:%M') if request.user.last_login else 'Nunca',
            }
        }
        return render(request, "biblioteca/mis_datos.html", datos)
    except Suscriptor.DoesNotExist:
        return HttpResponse("No se encontró información del suscriptor", status=404)