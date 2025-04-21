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
    lecturas=Lecturade_libro.objects.all()
    datos={
        "lecturas":[{
            "suscriptor": lectura.suscriptor.nombre,
            "libro" : lectura.libro.titulo,
            "fecha":lectura.fecha.strftime('%Y-%m-%d'),
            "id":lectura.id
        } for lectura in lecturas]
    }
    return render(request, "biblioteca/tabla_lectura_libros.html",datos)

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
            return HttpResponseRedirect("/admin/biblioteca/prestamo/")
            
    else:
        if comentario_existente:
            form = ComentarioLibroForm(instance=comentario_existente)
        else:
            form = ComentarioLibroForm()
    
    return render(request, "biblioteca/agregar_comentario.html", {
        'form': form,
        'libro': libro,
        'suscriptor': suscriptor
    })

def tabla_prestamos(request):
    prestamos = Prestamo.objects.all().order_by('-fecha_prestamo')
    datos = {
        "prestamos": [{
            "suscriptor": prestamo.suscriptor.nombre,
            "libro": prestamo.libro.titulo if prestamo.libro else prestamo.revista.nombre,
            "fecha_prestamo": prestamo.fecha_prestamo.strftime('%Y-%m-%d'),
            "fecha_entrega": prestamo.fecha_entrga.strftime('%Y-%m-%d'),
            "devolucion": prestamo.devolucion,
            "id": prestamo.id,
            "libro_id": prestamo.libro.id if prestamo.libro else None
        } for prestamo in prestamos]
    }
    return render(request, "biblioteca/tabla_prestamos.html", datos)

def delete_prestamo(request, id):
    Prestamo.objects.filter(id=id).delete()
    return redirect('tabla_prestamos')