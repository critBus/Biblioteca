from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from apps.biblioteca.models import *
from django.utils import timezone
import random
from datetime import timedelta
import faker

User = get_user_model()
fake = faker.Faker(['es_ES'])

class Command(BaseCommand):
    help = 'Popula la base de datos con datos de prueba'

    def handle(self, *args, **kwargs):
        self.stdout.write('Creando datos de prueba...')
        
        # Crear usuarios
        self.create_users()
        
        # Crear libros
        self.create_libros()
        
        # Crear revistas
        self.create_revistas()
        
        # Crear material audiovisual
        self.create_material_audiovisual()
        
        # Crear mobiliario
        self.create_mobiliario()
        
        # Crear suscriptores
        self.create_suscriptores()
        
        # Crear préstamos
        self.create_prestamos()
        
        # Crear lecturas de libros
        self.create_lecturas()
        
        # Crear muestras del mes
        self.create_muestras()
        
        # Crear configuración
        self.create_configuracion()
        
        self.stdout.write(self.style.SUCCESS('Datos de prueba creados exitosamente'))

    def create_users(self):
        # Crear usuarios de prueba
        for _ in range(10):
            username = fake.user_name()
            email = fake.email()
            password = "password123"
            User.objects.create_user(username=username, 
            email=email, 
            password=password,
            first_name=fake.first_name(),
            last_name=fake.last_name())

    def create_libros(self):
        # Crear libros de prueba
        generos = ["Ficcion", "No ficción", "Ciencia ficción", "Fantasía", "Aventura", "Policíaca", "Romántico"]
        estados = ["Bueno", "Regular", "Malo"]
        
        for _ in range(20):
            Libro.objects.create(
                titulo=fake.catch_phrase(),
                editorial=fake.company(),
                autor=fake.name(),
                fecha_publicacion=fake.date_between(start_date='-10y', end_date='today'),
                edicion=str(random.randint(1, 10)),
                estado=random.choice(estados),
                ubicacion=f"Estante {random.randint(1, 10)}",
                descripcion=fake.text(max_nb_chars=200),
                genero=random.choice(generos),
                fecha_adquisicion=fake.date_between(start_date='-5y', end_date='today'),
                numero_copias=random.randint(1, 10),
                numero_serie=random.randint(1000, 9999),
                materia=fake.word(),
                pais=fake.country(),
                resumen=fake.text(max_nb_chars=200),
                cantidad_prestamo=random.randint(0, 50),
                cantidad_paginas=random.randint(50, 500),
                peso=random.uniform(0.2, 2.0)
            )

    def create_revistas(self):
        # Crear revistas de prueba
        periodicidades = ["Semanal", "Quincenal", "Mensual", "Bimestral", "Trimestral", "Semestral", "Anual"]
        estados = ["Bueno", "Regular", "Malo"]
        
        for _ in range(15):
            Revista.objects.create(
                nombre=fake.company(),
                perioricidad=random.choice(periodicidades),
                numero=str(random.randint(1, 100)),
                numero1=str(random.randint(1, 50)),
                fecha_publicacion=fake.date_between(start_date='-5y', end_date='today'),
                editorial=fake.company(),
                Pais=fake.country(),
                estado=random.choice(estados),
                ubicacion=f"Estante {random.randint(1, 10)}",
                descripcion=fake.text(max_nb_chars=200),
                fecha_adquisicion=fake.date_between(start_date='-2y', end_date='today'),
                numero_copias=random.randint(1, 10),
                numero_serie=str(random.randint(1000, 9999)),
                cantidad_prestamo=random.randint(0, 30),
                peso=random.uniform(0.1, 1.0)
            )

    def create_material_audiovisual(self):
        # Crear material audiovisual de prueba
        generos = ["Ficción", "No ficción", "Ciencia ficción", "Fantasía", "Aventura", "Policíaca", "Romántico"]
        formatos = ["MP4", "AVI", "MOV", "WMV", "FLV", "WebM", "MPEG", "3GP", "AVCHD"]
        estados = ["Bueno", "Regular", "Malo"]
        
        for _ in range(10):
            MaterialAudiovisual.objects.create(
                titulo=fake.catch_phrase(),
                creador=fake.name(),
                fecha_produccion=fake.date_between(start_date='-8y', end_date='today'),
                productora=fake.company(),
                estado=random.choice(estados),
                ubicacion=f"Estante {random.randint(1, 10)}",
                descripcion=fake.text(max_nb_chars=200),
                genero=random.choice(generos),
                formato=random.choice(formatos),
                fecha_adquisicion=fake.date_between(start_date='-3y', end_date='today'),
                numero_copias=random.randint(1, 5),
                numero_serie=str(random.randint(1000, 9999)),
                cantidad_prestamo=random.randint(0, 20)
            )

    def create_mobiliario(self):
        # Crear mobiliario de prueba
        estados = ["Bueno", "Regular", "Malo"]
        tipos_mueble = ["Estantería", "Mesa", "Silla", "Escritorio", "Archivador"]
        
        for _ in range(8):
            Mobiliario.objects.create(
                nombre_tipoMueble=random.choice(tipos_mueble),
                numero_serie=random.randint(1000, 9999),
                ubicacion=f"Sala {random.randint(1, 5)}",
                dimenciones=f"{random.randint(30, 200)}x{random.randint(30, 200)}x{random.randint(30, 200)}",
                costo_adqisicion=random.randint(100, 1000),
                cantidad=random.randint(1, 10),
                estado=random.choice(estados)
            )

    def create_suscriptores(self):
        # Crear suscriptores de prueba
        niveles_escolares = ["Primaria", "Secundaria", "Preuniversitario", "Universitario", "Postgrado"]
        
        users = User.objects.all()
        for user in users:
            Suscriptor.objects.create(
                user=user,
                nombre=fake.name(),
                edad=random.randint(18, 70),
                sexo=random.choice(["Masculino", "Femenino"]),
                Telefono=str(random.randint(10000000, 99999999)),
                ci=random.randint(10000000000, 99999999999),
                centro_trabajo=fake.company(),
                ocupacion=fake.job(),
                direccion=fake.address(),
                sindicato=random.choice([True, False]),
                nivel_escolar=random.choice(niveles_escolares)
            )

    def create_prestamos(self):
        # Crear préstamos de prueba
        suscriptores = Suscriptor.objects.all()
        libros = Libro.objects.all()
        revistas = Revista.objects.all()
        
        for _ in range(30):
            fecha_prestamo = fake.date_between(start_date='-1y', end_date='today')
            fecha_entrega = fecha_prestamo + timedelta(days=random.randint(7, 30))
            
            tipo_material = random.choice(['libro', 'revista'])
            if tipo_material == 'libro':
                Prestamo.objects.create(
                    fecha_prestamo=fecha_prestamo,
                    fecha_entrga=fecha_entrega,
                    libro=random.choice(libros),
                    suscriptor=random.choice(suscriptores),
                    devolucion=random.choice([True, False])
                )
            else:
                Prestamo.objects.create(
                    fecha_prestamo=fecha_prestamo,
                    fecha_entrga=fecha_entrega,
                    revista=random.choice(revistas),
                    suscriptor=random.choice(suscriptores),
                    devolucion=random.choice([True, False])
                )

    def create_lecturas(self):
        # Crear lecturas de libros de prueba
        suscriptores = Suscriptor.objects.all()
        libros = Libro.objects.all()
        
        for _ in range(40):
            Lecturade_libro.objects.create(
                fecha=fake.date_between(start_date='-1y', end_date='today'),
                libro=random.choice(libros),
                suscriptor=random.choice(suscriptores)
            )

    def create_muestras(self):
        # Crear muestras del mes de prueba
        for _ in range(5):
            fecha_inicio = fake.date_between(start_date='today', end_date='+3m')
            MuestrasMes.objects.create(
                nombre_muestra=fake.catch_phrase(),
                tipo_muestra=fake.word(),
                autor=fake.name(),
                responsable=fake.name(),
                descrpcion=fake.text(max_nb_chars=200),
                genero=fake.word(),
                fecha_inicio=fecha_inicio,
                fecha_fin=fecha_inicio + timedelta(days=random.randint(7, 30)),
                horario_inicio=f"{random.randint(8, 10)}:00",
                horario_Cierre=f"{random.randint(16, 18)}:00",
                edad_minima=random.randint(5, 12),
                edad_maxima=random.randint(13, 18),
                direccion=fake.address()
            )

    def create_configuracion(self):
        # Crear configuración de la biblioteca
        if not ConfiguracionBiblio.objects.exists():
            ConfiguracionBiblio.objects.create(
                peso_maximo=10.0  # 10 kg como peso máximo por defecto
            )
