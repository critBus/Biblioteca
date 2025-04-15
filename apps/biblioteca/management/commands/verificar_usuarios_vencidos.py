from django.core.management.base import BaseCommand
from biblioteca.models import UsuariosEventuales

class Command(BaseCommand):
    help = 'Verifica y mueve usuarios eventuales vencidos al archivo histórico'

    def handle(self, *args, **options):
        UsuariosEventuales.verificar_usuarios_vencidos()
        self.stdout.write(self.style.SUCCESS('Verificación de usuarios vencidos completada'))
