from django.db import models

# Create your models here.
from tabnanny import verbose
from turtle import mode

from django.db import models
from django.utils import timezone
from solo.models import SingletonModel

from apps.users.models import *
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
import datetime
from django.core.exceptions import ValidationError

from config import settings


def no_futuro(fecha: datetime):
    hoy = timezone.now()
    if isinstance(fecha, datetime.date):
        hoy = hoy.date()
    # print(f"hoy>=fecha {hoy>=fecha}")
    if hoy < fecha:
        raise ValidationError("El día no ha transcurrido")


def no_pasado(fecha: datetime):
    hoy = timezone.now()
    if isinstance(fecha, datetime.date):
        hoy = hoy.date()
    # print(f"hoy>=fecha {hoy>=fecha}")
    if hoy > fecha:
        raise ValidationError("El día ya paso")


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


NOMBRE_ROL_BIBLIOTECARIO = "BIBLIOTECARIO"
NOMBRE_ROL_SUSCRIPTOR = "SUSCRIPTOR"
NOMBRE_ROL_ADMINISTRADOR = "ADMINISTRADOR"


class Libro(models.Model):
    class Meta:
        verbose_name = "Libro"
        verbose_name_plural = "Libros"

    TIPO_CHOICES = [
        ('normal', 'Libro Normal'),
        ('infantil', 'Libro Infantil')
    ]
    tipo_libro = models.CharField(
        max_length=10,
        choices=TIPO_CHOICES,
        default='normal',
        verbose_name="Tipo de Libro"
    )
    factor_estancia = models.FloatField(default=0)
    peso = models.FloatField(default=0)
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
    fecha_publicacion = models.DateField(
        verbose_name="Fecha de Publicación", validators=[no_futuro]
    )
    edicion = models.CharField(
        max_length=256,
        verbose_name="Edición",
        null=True,
        blank=True,
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
        null=True,
        blank=True,
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
    fecha_adquisicion = models.DateField(
        verbose_name="Fecha de Adquisición", validators=[no_futuro]
    )
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
    materia = models.CharField(
        max_length=256,
        verbose_name="Materia",
        validators=[RegexValidator(r"^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$")],
    )
    pais = models.CharField(
        max_length=256,
        verbose_name="País",
        validators=[RegexValidator(r"^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$")],
    )
    resumen = models.CharField(
        max_length=256,
        verbose_name="Resumen del Contenido",
        validators=[RegexValidator(r"^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$")],
    )
    cantidad_prestamo = models.IntegerField(
        verbose_name="Cantidad de Préstamos",
        validators=[
            MinValueValidator(0,)
        ],
    )
    cantidad_paginas = models.IntegerField(
        verbose_name="Cantidad de Páginas",
        validators=[
            MinValueValidator(0, )
        ],
    )
    ilustraciones = models.BooleanField(default=False, verbose_name="Tiene Ilustraciones")
    edad_minima = models.IntegerField(
        verbose_name="Edad Mínima Recomendada",
        null=True,
        blank=True,
        validators=[
            MinValueValidator(1),
        ],
    )
    edad_maxima = models.IntegerField(
        verbose_name="Edad Máxima Recomendada",
        null=True,
        blank=True,
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

    def save(self, *args, **keyargs):
        es_nuevo = self.pk is None

        annos_publicados = datetime.datetime.now().date().year-self.fecha_publicacion.year
        annos_estancia = datetime.datetime.now().date().year-self.fecha_adquisicion.year
        if annos_estancia!=0:
            self.factor_estancia=(annos_publicados+1)/(annos_estancia+1)

        self.peso = self.cantidad_prestamo*self.factor_estancia
        
        # Aplicar factor de ilustraciones si es libro infantil
        if self.tipo_libro == 'infantil' and self.ilustraciones:
            self.factor_estancia *= 1.05
            
        return super().save(*args, **keyargs)

    def __str__(self):
        return self.titulo


class Revista(models.Model):
    class Meta:
        verbose_name = "Revista"
        verbose_name_plural = "Revistas"

    factor_estancia = models.FloatField(default=0)
    peso = models.FloatField(default=0)
    nombre = models.CharField(
        max_length=256,
        verbose_name="Nombre de la Revista",
        validators=[RegexValidator(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$")],
    )
    perioricidad = models.CharField(
        max_length=256,
        verbose_name="Perioricidad",
        choices=(
            ("Semanal", "Semanal"),
            ("Quincenal", "Quincenal"),
            ("Mensual", "Mensual"),
            ("Bimestral", "Bimestral"),
            ("Trimestral", "Trimestral"),
            ("Semestral", "Semestral"),
            ("Anual", "Anual"),
            ("Irregular", "Irregular"),
        ),
    )
    numero = models.CharField(
        max_length=256, verbose_name="Número de Volumen", null=True, blank=True
    )
    numero1 = models.CharField(
        max_length=256, verbose_name="Número", null=True, blank=True
    )
    fecha_publicacion = models.DateField(
        verbose_name="Fecha de Publicación", validators=[no_futuro]
    )
    editorial = models.CharField(
        max_length=256,
        verbose_name="Editorial",
        validators=[RegexValidator(r"^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$")],
    )
    Pais = models.CharField(
        max_length=256,
        verbose_name="País",
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
    fecha_adquisicion = models.DateField(
        verbose_name="Fecha de Adquisición", validators=[no_futuro]
    )
    numero_copias = models.IntegerField(
        verbose_name="Número de Copias Disponibles",
        validators=[
            MinValueValidator(1),
        ],
    )
    numero_serie = models.CharField(
        max_length=256,
        verbose_name="Número de Serie",
    )
    cantidad_prestamo = models.IntegerField(
        verbose_name="Cantidad de préstamos",
        validators=[
            MinValueValidator(1),
        ],
    )

    def __str__(self):
        return self.nombre

    def clean(self):
        super().clean()
        if self.fecha_adquisicion and self.fecha_publicacion:
            if self.fecha_adquisicion <= self.fecha_publicacion:
                raise ValidationError(
                    "La fecha de Publicación debe ser inferior a la fecha de Adquisición "
                )

    def save(self, *args, **keyargs):
        es_nuevo = self.pk is None

        meses_publicados = (datetime.datetime.now().date() - self.fecha_publicacion).days/30
        annos_estancia = datetime.datetime.now().date().year - self.fecha_adquisicion.year
        if annos_estancia != 0:
            self.factor_estancia = (meses_publicados + 1) / ((annos_estancia *10)+1)
        self.peso = self.cantidad_prestamo * self.factor_estancia
        return super().save(*args, **keyargs)


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
    fecha_produccion = models.DateField(
        verbose_name="Fecha de Producción", validators=[no_futuro]
    )
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
        verbose_name="Género o Categoría",
        null=True,
        blank=True,
        choices=[
            ("Ficción", "Ficción"),
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
        null=True,
        blank=True,
        choices=(
            ("MP4", "MP4"),
            ("AVI", "AVI"),
            ("MOV", "MOV"),
            ("WMV", "WMV"),
            ("FLV", "FLV"),
            ("WebM", "WebM"),
            ("MPEG", "MPEG"),
            ("3GP", "3GP"),
            ("AVCHD", "AVCHD"),
        ),
    )
    fecha_adquisicion = models.DateField(
        verbose_name="Fecha de Adquisición", validators=[no_futuro]
    )
    numero_copias = models.IntegerField(
        verbose_name="Número de Copias Disponibles",
        validators=[
            MinValueValidator(1),
        ],
    )
    numero_serie = models.CharField(
        max_length=256,
        verbose_name="Número de Serie",
    )
    cantidad_prestamo = models.IntegerField(
        verbose_name="Cantidad de préstamos",
        validators=[
            MinValueValidator(1),
        ],
    )

    def __str__(self):
        return self.titulo

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
        verbose_name_plural = "Mobiliarios"

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
        verbose_name="Dimensiones",
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

    def __str__(self):
        return self.nombre_tipoMueble


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
        verbose_name="Género o Categoría",
        null=True,
        blank=True,
        validators=[RegexValidator(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$")],
    )
    fecha_inicio = models.DateField(verbose_name="Fecha de Inicio")
    fecha_fin = models.DateField(verbose_name="Fecha de Fin")
    horario_inicio = models.TimeField(verbose_name="Horario de inicio")
    horario_Cierre = models.TimeField(verbose_name="Horario de cierre")
    edad_minima = models.IntegerField(
        verbose_name="Edad Mínima Recomendada",
        null=True,
        blank=True,
        validators=[
            MinValueValidator(1),
        ],
    )
    edad_maxima = models.IntegerField(
        verbose_name="Edad Máxima Recomendada",
        null=True,
        blank=True,
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
                    "La Edad de Mínima debe ser inferior a la Edad de Máxima "
                )


class Suscriptor(models.Model):
    class Meta:
        verbose_name = "Suscriptor"
        verbose_name_plural = "Suscriptores"

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    nombre = models.CharField(
        max_length=256,
        verbose_name="Nombre",
        validators=[RegexValidator(r"^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$")],
    )
    edad = models.IntegerField(
        verbose_name="Edad",
        validators=[MinValueValidator(1), MaxValueValidator(120)],
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
        max_length=256,
        verbose_name="Centro de Trbajo o Estudio ",
        null=True,
        blank=True,
    )
    ocupacion = models.CharField(
        max_length=256,
        verbose_name="Ocupación",
        null=True,
        blank=True,
        validators=[RegexValidator(r"^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$")],
    )
    direccion = models.CharField(
        max_length=256,
        verbose_name="Dirección",
        validators=[RegexValidator(r"^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ/# ]+$")],
    )
    sindicato = models.BooleanField(default=False)
    nivel_escolar = models.CharField(
        max_length=256,
        verbose_name="Nivel de Escolaridad",
        validators=[RegexValidator(r"^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$")],
    )
    def get_peso_acumulado(self):
        prestamos=PrestamoLibro.objects.filter(suscriptor=self, devolucion=False, fecha_entrga__lt=datetime.datetime.now().date())
        peso_total=0
        for prestamo in prestamos:
            peso_total+=prestamo.get_peso()
        return peso_total

    def __str__(self):
        return self.nombre


class LibrosDelMes(models.Model):
    class Meta:
        verbose_name = "Libro del mes"
        verbose_name_plural = "Libros del Mes"
        
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    fecha = models.DateField(verbose_name="Fecha", validators=[no_futuro])

    
    

    def clean(self):
        super().clean()
        if LibrosDelMes.objects.filter(
            fecha__month=self.fecha.month, fecha__year=self.fecha.year
        ).exists():
            raise ValidationError("Solo puede ser un libro en el mes")

def calcular_libro_mes():
    """Calcula el libro del mes basado en préstamos y lecturas del mes actual"""
    fecha_actual = timezone.now().date()
    mes_actual = fecha_actual.replace(day=1)
    
    # Obtener todos los libros con sus préstamos y lecturas
    libros = Libro.objects.all()
    libro_mas_popular = None
    max_peso = -1

    for libro in libros:
        # Calcular peso basado en préstamos y lecturas del mes actual
        prestamos_mes = PrestamoLibro.objects.filter(
            libro=libro,  # Buscar en ambos modelos
            fecha_prestamo__year=mes_actual.year,
            fecha_prestamo__month=mes_actual.month
        ).count()

        lecturas_mes = Lecturade_libro.objects.filter(
            libro=libro,
            fecha__year=mes_actual.year,
            fecha__month=mes_actual.month
        ).count()
        
        peso_total = (
            libro.peso +  # Peso base del libro (incluye factor_estancia)
            prestamos_mes * 2 +  # Doble peso por préstamos del mes
            lecturas_mes  # Peso por lecturas del mes
        )
        
        if peso_total > max_peso:
            max_peso = peso_total
            libro_mas_popular = libro

    if libro_mas_popular:
        # Actualizar o crear el libro del mes
        libro_mes=LibrosDelMes.objects.filter(
            fecha__year=mes_actual.year,
            fecha__month=mes_actual.month,
            ).first()
        if libro_mes:
            libro_mes.libro = libro_mas_popular
            libro_mes.fecha = fecha_actual  # Actualizar la fecha al día actual
            libro_mes.save()
            return libro_mes
        else:
            libro_mes = LibrosDelMes.objects.create(
                fecha=fecha_actual,
                libro=libro_mas_popular,
                )
            return libro_mes

        # libro_mes, created = LibrosDelMes.objects.get_or_create(
        #     fecha__year=mes_actual.year,
        #     fecha__month=mes_actual.month,
        #     defaults={
        #         'libro': libro_mas_popular,
        #         'fecha': fecha_actual  # Usar la fecha actual en lugar del primer día del mes
        #     }
        # )
        #
        # if not created:
        #     libro_mes.libro = libro_mas_popular
        #     libro_mes.fecha = fecha_actual  # Actualizar la fecha al día actual
        #     libro_mes.save()
        #
        # return libro_mes
    return None
class Inventario(models.Model):
    class Meta:
        verbose_name = "Inventario"
        verbose_name_plural = "Inventarios"

    fecha = models.DateTimeField(
        verbose_name="Fecha", validators=[no_futuro], auto_now_add=True
    )
    libros = models.ManyToManyField(Libro)
    revistas = models.ManyToManyField(Revista)
    mobiliarios = models.ManyToManyField(Mobiliario)
    materiales_audiovisuales = models.ManyToManyField(MaterialAudiovisual)


class Lecturade_libro(models.Model):
    class Meta:
        verbose_name = "Lectura de libro"
        verbose_name_plural = "Lecturas de libros"

    fecha = models.DateField(verbose_name="Fecha", validators=[no_futuro])
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    suscriptor = models.ForeignKey(Suscriptor, on_delete=models.CASCADE)


class PrestamoLibro(models.Model):
    class Meta:
        verbose_name = "Préstamo de Libro"
        verbose_name_plural = "Préstamos de Libros"

    fecha_prestamo = models.DateField(
        verbose_name="Fecha de Préstamo", validators=[no_futuro]
    )
    fecha_entrga = models.DateField(verbose_name="Fecha de Entrega")
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, null=True, blank=True)
    suscriptor = models.ForeignKey(Suscriptor, on_delete=models.CASCADE,null=False, blank=False)
    devolucion = models.BooleanField(default=False)
    def get_peso(self):
        if self.libro:
            return self.libro.peso
        # if self.revista:
        #     return self.revista.peso

    def clean(self):
        super().clean()
        if self.fecha_entrga and self.fecha_prestamo:
            if self.fecha_entrga <= self.fecha_prestamo:
                raise ValidationError(
                    "La fecha de Préstamo debe ser inferior a la fecha de Entrega "
                )
        # if self.suscriptor:
        #     if self.suscriptor.get_peso_acumulado()>ConfiguracionBiblio.get_solo().peso_maximo:
        #         raise ValidationError(
        #             "Exedió el peso máximo"
        #         )

    def save(self, *args, **keyargs):
        es_nuevo = self.pk is None
        if es_nuevo:
            if self.libro:
                self.libro.cantidad_prestamo += 1
                self.libro.save()
            # if self.revista:
            #     self.revista.cantidad_prestamo += 1
            #     self.revista.save()
        return super().save(*args, **keyargs)

class PrestamoRevista(models.Model):
    class Meta:
        verbose_name = "Préstamo de Revistas"
        verbose_name_plural = "Préstamos de Revistas"

    fecha_prestamo = models.DateField(
        verbose_name="Fecha de Préstamo", validators=[no_futuro]
    )
    fecha_entrga = models.DateField(verbose_name="Fecha de Entrega")
    revista = models.ForeignKey(Revista, on_delete=models.CASCADE, null=True, blank=True)
    suscriptor = models.ForeignKey(Suscriptor, on_delete=models.CASCADE,null=False, blank=False)
    devolucion = models.BooleanField(default=False)

    def get_peso(self):
        if self.revista:
            return self.revista.peso

    def clean(self):
        super().clean()
        if self.fecha_entrga and self.fecha_prestamo:
            if self.fecha_entrga <= self.fecha_prestamo:
                raise ValidationError(
                    "La fecha de Préstamo debe ser inferior a la fecha de Entrega "
                )
    def save(self, *args, **keyargs):
        es_nuevo = self.pk is None
        if es_nuevo:
            if self.revista:
                self.revista.cantidad_prestamo += 1
                self.revista.save()
        return super().save(*args, **keyargs)

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
        verbose_name="Categoría",
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
        validators=[MinValueValidator(17), MaxValueValidator(100)],
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
            length_validation_11,
            RegexValidator(r"^[0-9]{11}$"),
            not_empty_validation,
        ],
    )
    direccion = models.CharField(
        max_length=256,
        verbose_name="Dirección",
        validators=[RegexValidator(r"^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ#/ ]+$")],
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
        verbose_name = "Informe de Asitecias"
        verbose_name_plural = "Informes de Asistencias"

    fecha = models.DateField(verbose_name="Fecha", validators=[no_futuro])
    trabajador = models.ForeignKey(Trabajador, on_delete=models.CASCADE)
    horas = models.IntegerField(
        verbose_name="Horas Trabajadas",
    )


class UsuariosEventuales(models.Model):
    class Meta:
        verbose_name = "Usuario Eventual"
        verbose_name_plural = "Usuarios Eventuales"

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        unique=True
    )
    fecha = models.DateField(verbose_name="Fecha de vencimiento", validators=[no_pasado])

    def mover_a_archivo(self):
        """Mueve el usuario a archivo histórico y elimina el registro actual"""
        Archivo.objects.create(
            user=self.user,
            fecha_inicio=timezone.now().date() - timezone.timedelta(days=30),  # Estimación de fecha inicio (30 días antes)
            fecha_fin=self.fecha
        )
        self.user.is_active = False
        self.user.save()

        self.delete()

    @classmethod
    def verificar_usuarios_vencidos(cls):
        """Verifica y mueve usuarios vencidos al archivo histórico"""
        fecha_actual = timezone.now().date()
        usuarios_vencidos = cls.objects.filter(fecha__lt=fecha_actual)
        
        for usuario in usuarios_vencidos:
            usuario.mover_a_archivo()

def verificar_usuarios_vencidos():
    """Verifica y mueve usuarios vencidos al archivo histórico"""
    fecha_actual = timezone.now().date()
    usuarios_vencidos = UsuariosEventuales.objects.filter(fecha__lt=fecha_actual)
    
    for usuario in usuarios_vencidos:
        usuario.mover_a_archivo()

class ConfiguracionBiblio(SingletonModel):
    class Meta:
        verbose_name = "Configuraciones de la Biblioteca"
        verbose_name_plural = "Configuraciones de la Biblioteca "

    peso_maximo = models.FloatField(default=0)


class Archivo(models.Model):
    class Meta:
        verbose_name = "Archivo Histórico"
        verbose_name_plural = "Archivos Históricos"

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        unique=True
    )
    fecha_inicio = models.DateField(verbose_name="Fecha de inicio")
    fecha_fin = models.DateField(verbose_name="Fecha de fin")

    def __str__(self):
        return f"{self.user} - {self.fecha_inicio} a {self.fecha_fin}"

class ComentarioLibro(models.Model):
    class Meta:
        verbose_name = "Comentario de Libro"
        verbose_name_plural = "Comentarios de Libros"
        unique_together = ['libro', 'suscriptor']  # Evita comentarios duplicados del mismo usuario

    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, verbose_name="Libro")
    suscriptor = models.ForeignKey(Suscriptor, on_delete=models.CASCADE, verbose_name="Suscriptor")
    comentario = models.TextField(verbose_name="Comentario", validators=[RegexValidator(r"^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ,.!¡¿?]+$")])
    puntuacion = models.IntegerField(
        verbose_name="Puntuación",
        validators=[
            MinValueValidator(1, message="La puntuación mínima es 1"),
            MaxValueValidator(5, message="La puntuación máxima es 5")
        ]
    )
    fecha = models.DateTimeField(verbose_name="Fecha", auto_now_add=True)

    def __str__(self):
        return f"Comentario de {self.suscriptor} en {self.libro}"

    def clean(self):
        super().clean()


class ArchivoEntrada(models.Model):
    class Meta:
        verbose_name = "Archivo de Entrada y Salida"
        verbose_name_plural = "Archivos de Entradas y Salidas"

    nombre = models.CharField(
        max_length=256,
        verbose_name="Nombre",
        validators=[RegexValidator(r"^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$")],
    )
    apellido = models.CharField(
        max_length=256,
        verbose_name="Apellido",
        validators=[RegexValidator(r"^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$")],
    )
    ci = models.IntegerField(
        verbose_name="CI",
        validators=[
            length_validation_11,
            RegexValidator(r"^[0-9]{11}$"),
            not_empty_validation,
        ],
    )
    horaentrada = models.DateTimeField(verbose_name="Hora de Entrada")
    horasalida = models.DateTimeField(verbose_name="Hora de Salida")


class LibroDigital(models.Model):
    class Meta:
        verbose_name = "Libro Digital"
        verbose_name_plural = "Libros Digitales"

    titulo = models.CharField(
        max_length=256,
        verbose_name="Título",
        validators=[RegexValidator(r"^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$")],
    )
    autor = models.CharField(
        max_length=256,
        verbose_name="Autor",
        validators=[RegexValidator(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$")],
    )
    archivo_pdf = models.FileField(
        upload_to='libros_digitales/',
        verbose_name="Archivo PDF",
        help_text="Sube el archivo PDF del libro"
    )
    fecha_subida = models.DateTimeField(
        verbose_name="Fecha de Subida",
        auto_now_add=True
    )
    descripcion = models.TextField(
        verbose_name="Descripción",
        validators=[RegexValidator(r"^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ,.!¡¿?]+$")],
        null=True,
        blank=True
    )
    genero = models.CharField(
        max_length=256,
        verbose_name="Género",
        null=True,
        blank=True,
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
    edad_minima = models.IntegerField(
        verbose_name="Edad Mínima Recomendada",
        null=True,
        blank=True,
        validators=[
            MinValueValidator(1),
        ],
    )
    edad_maxima = models.IntegerField(
        verbose_name="Edad Máxima Recomendada",
        null=True,
        blank=True,
        validators=[
            MinValueValidator(1),
        ],
    )

    def __str__(self):
        return self.titulo

