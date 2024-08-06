from django.db import models

# Create your models here.
from tabnanny import verbose
from turtle import mode

from django.db import models
from apps.users.models import *
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
import datetime
from django.core.exceptions import ValidationError


def not_empty_validation(texto):
    if len(str(texto).strip()) == 0:
        raise ValidationError("No puede estar compuesto solo por espacios")


def length_validation_8(texto):
    cantidad_caracteres = 8
    if len(str(texto).strip()) != cantidad_caracteres:
        raise ValidationError(
            f"Tiene que tener exactamente {cantidad_caracteres} caracteres "
        )


def length_validation_11(texto):
    cantidad_caracteres = 11
    if len(str(texto).strip()) != cantidad_caracteres:
        raise ValidationError(
            f"Tiene que tener exactamente {cantidad_caracteres} caracteres "
        )


class Libro(models.Model):
    class Meta:
        verbose_name = "Libro"
        verbose_name_plural = "Libros"

    titulo = models.CharField(
        max_length=256,
        verbose_name="Título",
        validators=[RegexValidator(r"^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$")],
    )
    editorial = models.CharField(
        max_length=256,
        verbose_name="Editorial",
        validators=[RegexValidator(r"^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$")],
    )
    autor = models.CharField(
        max_length=256,
        verbose_name="Autor",
        validators=[RegexValidator(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$")],
    )
    fecha_publicacion = models.DateField(verbose_name="Fecha de Publicación")
    edicion = models.CharField(
        max_length=256,
        verbose_name="Edición",
        validators=[RegexValidator(r"^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$")],
    )
    estado = models.CharField(
        max_length=256,
        verbose_name="Estado",
        choices=(
            ("Bueno", "Bueno"),
            ("Regular", "Regular"),
            ("Malo", "Malo"),
        ),
    )
    ubicacion = models.CharField(
        max_length=256,
        verbose_name="Ubicación",
        validators=[RegexValidator(r"^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$")],
    )
    descripcion = models.CharField(
        max_length=256,
        verbose_name="Descripción",
        validators=[RegexValidator(r"^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$")],
    )
    genero = models.CharField(
        max_length=256,
        verbose_name="Género",
        choices=[
            ("Ficcion", "Ficcion"),
            ("No ficción", "No ficción"),
            ("Ciencia ficción", "Ciencia ficción"),
            ("Fantasía", "Fantasía"),
            ("Aventura", "Aventura"),
            ("Policíaca", "Policíaca"),
            ("Romántico", "Romántico"),
        ],
    )
    fecha_adquisicion = models.DateField(verbose_name="Fecha de Adquisición")
    numero_copias = models.IntegerField(
        verbose_name="Número de Copias Disponibles",
        validators=[
            MinValueValidator(1),
        ],
    )
    numero_serie = models.IntegerField(
        max_length=256,
        verbose_name="Número de Serie",
        validators=[
            MinValueValidator(1),
        ],
    )

    def clean(self):
        super().clean()
        if self.fecha_adquisicion and self.fecha_publicacion:
            if self.fecha_adquisicion <= self.fecha_publicacion:
                raise ValidationError(
                    "La fecha de Publicación debe ser inferior a la fecha de Adquisición "
                )

    def __str__(self):
        return self.titulo

class Revista(models.Model):
    class Meta:
        verbose_name = "Revista"
        verbose_name_plural = "Revista"

    nombre = models.CharField(
        max_length=256,
        verbose_name="Nombre de la Revista",
        validators=[RegexValidator(r"^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$")],
    )
    perioricidad = models.CharField(
        max_length=256,
        verbose_name="Perioricidad",
        validators=[RegexValidator(r"^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$")],
    )
    numero = models.CharField(
        max_length=256,
        verbose_name="Número de Volumen",
        validators=[
            MinValueValidator(1),
        ],
    )
    fecha_publicacion = models.DateField(verbose_name="Fecha de Publicación")
    editorial = models.CharField(
        max_length=256,
        verbose_name="Editorial",
        validators=[RegexValidator(r"^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$")],
    )
    estado = models.CharField(
        max_length=256,
        verbose_name="Estado",
        choices=(
            ("Bueno", "Bueno"),
            ("Regular", "Regular"),
            ("Malo", "Malo"),
        ),
    )
    ubicacion = models.CharField(
        max_length=256,
        verbose_name="Ubicación",
        validators=[RegexValidator(r"^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$")],
    )
    descripcion = models.CharField(
        max_length=256,
        verbose_name="Descripción",
        validators=[RegexValidator(r"^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$")],
    )
    fecha_adquisicion = models.DateField(verbose_name="Fecha de Adquisición")
    numero_copias = models.IntegerField(
        verbose_name="Número de Copias Disponibles",
        validators=[
            MinValueValidator(1),
        ],
    )
    numero_serie = models.CharField(
        max_length=256,
        verbose_name="Número de Serie",
        validators=[
            MinValueValidator(1),
        ],
    )
    def clean(self):
        super().clean()
        if self.fecha_adquisicion and self.fecha_publicacion:
            if self.fecha_adquisicion <= self.fecha_publicacion:
                raise ValidationError(
                    "La fecha de Publicación debe ser inferior a la fecha de Adquisición "
                )


class MaterialAudiovisual(models.Model):
    class Meta:
        verbose_name = "Material Audivisual"
        verbose_name_plural = "Materiales Audiovisuales"

    titulo = models.CharField(
        max_length=256,
        verbose_name="Título",
        validators=[RegexValidator(r"^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$")],
    )
    creador = models.CharField(
        max_length=256,
        verbose_name="Creador o Autor",
        validators=[RegexValidator(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$")],
    )
    fecha_produccion = models.DateField(verbose_name="Fecha de Producción")
    productora = models.CharField(
        max_length=256,
        verbose_name="Productora",
        validators=[RegexValidator(r"^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$")],
    )
    estado = models.CharField(
        max_length=256,
        verbose_name="Estado",
        choices=(
            ("Bueno", "Bueno"),
            ("Regular", "Regular"),
            ("Malo", "Malo"),
        ),
    )
    ubicacion = models.CharField(
        max_length=256,
        verbose_name="Ubicación",
        validators=[RegexValidator(r"^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$")],
    )
    descripcion = models.CharField(
        max_length=256,
        verbose_name="Descripción",
        validators=[RegexValidator(r"^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$")],
    )
    genero = models.CharField(
        max_length=256,
        verbose_name="Género o Categoria",
        choices=[
            ("Ficcion", "Ficcion"),
            ("No ficción", "No ficción"),
            ("Ciencia ficción", "Ciencia ficción"),
            ("Fantasía", "Fantasía"),
            ("Aventura", "Aventura"),
            ("Policíaca", "Policíaca"),
            ("Romántico", "Romántico"),
        ],
    )
    formato = models.CharField(
        max_length=256,
        verbose_name="Formato",
        validators=[RegexValidator(r"^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$")],
    )
    fecha_adquisicion = models.DateField(verbose_name="Fecha de Adquisición")
    numero_copias = models.IntegerField(
        verbose_name="Número de Copias Disponibles",
        validators=[
            MinValueValidator(1),
        ],
    )
    numero_serie = models.CharField(
        max_length=256,
        verbose_name="Número de Serie",
        validators=[
            MinValueValidator(1),
        ],
    )

    def clean(self):
        super().clean()
        if self.fecha_adquisicion and self.fecha_produccion:
            if self.fecha_adquisicion <= self.fecha_produccion:
                raise ValidationError(
                    "La fecha de Producción debe ser inferior a la fecha de Adquisición "
                )


class Mobiliario(models.Model):
    class Meta:
        verbose_name = "Mobiliario"
        verbose_name_plural = "Mobiliario"

    nombre_tipoMueble = models.CharField(
        max_length=256,
        verbose_name="Nombre del Mueble",
        validators=[RegexValidator(r"^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$")],
    )
    numero_serie = models.IntegerField(
        verbose_name="Número de Serie",
        validators=[
            MinValueValidator(1),
        ],
    )
    ubicacion = models.CharField(
        max_length=256,
        verbose_name="Ubicación",
        validators=[RegexValidator(r"^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$")],
    )
    dimenciones = models.CharField(
        max_length=256,
        verbose_name="Dimenciones",
        validators=[RegexValidator(r"^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$")],
    )
    costo_adqisicion = models.IntegerField(
        verbose_name="Costo de Adquisición",
        validators=[
            MinValueValidator(1),
        ],
    )
    cantidad = models.IntegerField(
        verbose_name="Cantidad",
        validators=[
            MinValueValidator(1),
        ],
    )
    estado = models.CharField(
        max_length=256,
        verbose_name="Estado",
        choices=(
            ("Bueno", "Bueno"),
            ("Regular", "Regular"),
            ("Malo", "Malo"),
        ),
    )


class MuestrasMes(models.Model):
    class Meta:
        verbose_name = "Muestra del Mes"
        verbose_name_plural = "Muestras del Mes"

    nombre_muestra = models.CharField(
        max_length=256,
        verbose_name="Título",
        validators=[RegexValidator(r"^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$")],
    )
    tipo_muestra = models.CharField(
        max_length=256,
        verbose_name="Tipo de Muestra",
        validators=[RegexValidator(r"^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$")],
    )
    autor = models.CharField(
        max_length=256,
        verbose_name="Autor",
        validators=[RegexValidator(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$")],
    )
    responsable = models.CharField(
        max_length=256,
        verbose_name="Responsable",
        validators=[RegexValidator(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$")],
    )
    descrpcion = models.CharField(
        max_length=256,
        verbose_name="Descripción",
        validators=[RegexValidator(r"^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$")],
    )
    genero = models.CharField(
        max_length=256,
        verbose_name="Género o Categoria",
        validators=[RegexValidator(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$")],
    )
    fecha_inicio = models.DateField(verbose_name="Fecha de Inicio")
    fecha_fin = models.DateField(verbose_name="Fecha de Fin")
    horario_inicio = models.DateTimeField(verbose_name="Horario de inicio")
    horario_Cierre = models.DateTimeField(verbose_name="Horario de cierre")
    edad_minima = models.IntegerField(
        verbose_name="Edad Minima Recomendada",
        validators=[
            MinValueValidator(1),
        ],
    )
    edad_maxima = models.IntegerField(
        verbose_name="Edad Máxima Recomendada",
        validators=[
            MinValueValidator(1),
        ],
    )
    direccion = models.CharField(
        max_length=256,
        verbose_name="Dirección",
        validators=[RegexValidator(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$")],
    )
    def clean(self):
        super().clean()
        if self.fecha_fin and self.fecha_inicio:
            if self.fecha_fin <= self.fecha_inicio:
                raise ValidationError(
                    "La fecha de inicio debe ser inferior a la fecha de fin "
                )
        if self.edad_maxima and self.edad_minima:
            if self.edad_maxima <= self.edad_minima:
                raise ValidationError(
                    "La Edad de Minima debe ser inferior a la Edad de Maxima "
                )


class Suscriptor(models.Model):
    class Meta:
        verbose_name = "Suscriptor"
        verbose_name_plural = "Suscriptores"

    nombre = models.CharField(
        max_length=256,
        verbose_name="Nombre",
        validators=[RegexValidator(r"^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$")],
    )
    edad = models.IntegerField(
        verbose_name="Edad",
        validators=[
            MinValueValidator(1),
        ],
    )
    sexo = models.CharField(
        max_length=256,
        verbose_name="Sexo",
        choices=(
            ("Masculino", "Masculino"),
            ("Femenino", "Femenino"),
        ),
    )
    Telefono = models.CharField(
        max_length=8,
        verbose_name="Teléfono",
        unique=True,
        validators=[
            length_validation_8,
            RegexValidator(r"^[0-9]{8}$"),
            not_empty_validation,
        ],
    )
    ci = models.IntegerField(
        verbose_name="CI",
        validators=[
            length_validation_11,
            RegexValidator(r"^[0-9]{11}$"),
            not_empty_validation,
        ],
    )
    centro_trabajo = models.CharField(
        max_length=256, verbose_name="Centro de Trbajo o Estudio "
    )
    ocupacion = models.CharField(
        max_length=256,
        verbose_name="Ocupación",
        validators=[RegexValidator(r"^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$")],
    )
    direccion = models.CharField(
        max_length=256,
        verbose_name="Dirección",
        validators=[RegexValidator(r"^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$")],
    )
    sindicato = models.BooleanField(default=False)
    nivel_escolar = models.CharField(
        max_length=256,
        verbose_name="Nivel de Escolaridad",
        validators=[RegexValidator(r"^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$")],
    )

    def __str__(self):
        return self.nombre


class LibrosDelMes(models.Model):
    class Meta:
        verbose_name = "Lobro del mes"
        verbose_name_plural = "Libros del Mes"

    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    fecha = models.DateField(verbose_name="Fecha")

    def clean(self):
        if LibrosDelMes.objects.filter(
            fecha__month=self.fecha.month, fecha__year=self.fecha.year
        ).exists():
            raise ValidationError("Solo puede ser un libro en el mes")


class Inventario(models.Model):
    class Meta:
        verbose_name = "Inventario"
        verbose_name_plural = "Inventarios"

    fecha = models.DateField(verbose_name="Fecha")
    libros = models.ManyToManyField(Libro)
    revistas = models.ManyToManyField(Revista)
    mobiliarios = models.ManyToManyField(Mobiliario)
    materiales_audiovisuales = models.ManyToManyField(MaterialAudiovisual)


class Lecturade_libro(models.Model):
    class Meta:
        verbose_name = "Lesctura de libro"
        verbose_name_plural = "Lescturas de libros"

    fecha = models.DateField(verbose_name="Fecha")
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    suscriptor = models.ForeignKey(Suscriptor, on_delete=models.CASCADE)


class Prestamo(models.Model):
    class Meta:
        verbose_name = "Prestamo"
        verbose_name_plural = "Pretamos"

    fecha_prestamo = models.DateField(verbose_name="Fecha de Prestamo")
    fecha_entrga = models.DateField(verbose_name="Fecha de Entrega")
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    suscriptor = models.ForeignKey(Suscriptor, on_delete=models.CASCADE)

    def clean(self):
        super().clean()
        if self.fecha_entrga and self.fecha_prestamo:
            if self.fecha_entrga <= self.fecha_prestamo:
                raise ValidationError(
                    "La fecha de Prestamo debe ser inferior a la fecha de Entrega "
                )

class Concurso(models.Model):
    class Meta:
        verbose_name = "Concurso"
        verbose_name_plural = "Concursos"

    fecha_inicio = models.DateField(verbose_name="Fecha de Inicio")
    fecha_cierre = models.DateField(verbose_name="Fecha de Cierre")
    nombre = models.CharField(
        max_length=256,
        verbose_name="Nombre",
        validators=[RegexValidator(r"^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$")],
    )
    descrpcion = models.CharField(
        max_length=256,
        verbose_name="Descripción",
        validators=[RegexValidator(r"^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$")],
    )
    categorias = models.CharField(
        max_length=256,
        verbose_name="Categoria",
        validators=[RegexValidator(r"^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$")],
    )
    modalidad = models.CharField(
        max_length=256,
        verbose_name="Modalidad",
        validators=[RegexValidator(r"^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ,]+$")],
    )

    def clean(self):
        super().clean()
        if self.fecha_cierre and self.fecha_inicio:
            if self.fecha_cierre <= self.fecha_inicio:
                raise ValidationError(
                    "La fecha de inicio debe ser inferior a la fecha de fin "
                )


class Trabajador(models.Model):
    class Meta:
        verbose_name = "Trabajador"
        verbose_name_plural = "Trabajadores"

    nombre = models.CharField(
        max_length=256,
        verbose_name="Nombre",
        validators=[RegexValidator(r"^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$")],
    )
    edad = models.IntegerField(
        verbose_name="Edad",
        validators=[
            MinValueValidator(1),
        ],
    )
    sexo = models.CharField(
        max_length=256,
        verbose_name="Sexo",
        choices=(
            ("Masculino", "Masculino"),
            ("Femenino", "Femenino"),
        ),
    )
    Telefono = models.CharField(
        max_length=256,
        verbose_name="Teléfono",
        validators=[
            length_validation_8,
            RegexValidator(r"^[0-9]{8}$"),
            not_empty_validation,
        ],
    )
    ci = models.IntegerField(
        verbose_name="CI",
        validators=[
            length_validation_11,
            RegexValidator(r"^[0-9]{11}$"),
            not_empty_validation,
        ],
    )
    expediente = models.IntegerField(
        verbose_name="Expediente",
        validators=[
            MinValueValidator(1),
        ],
    )
    direccion = models.CharField(
        max_length=256,
        verbose_name="Dirección",
        validators=[RegexValidator(r"^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$")],
    )
    sindicato = models.BooleanField(default=False)
    nivel_escolar = models.CharField(
        max_length=256,
        verbose_name="Nivel de Escolaridad",
        validators=[RegexValidator(r"^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$")],
    )
    def __str__(self):
        return self.nombre


class Asistencia(models.Model):
    class Meta:
        verbose_name = "Informe de Assitecias"
        verbose_name_plural = "Informes de Asistencias"

    fecha = models.DateField(verbose_name="Fecha")
    trabajador = models.ForeignKey(Trabajador, on_delete=models.CASCADE)
    horas = models.IntegerField(verbose_name="Horas Trabajadas",)