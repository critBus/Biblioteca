from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib import messages
from .models import Archivo

class ArchivoAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        User = get_user_model()
        try:
            # Intentamos obtener el usuario por nombre de usuario
            user = User.objects.get(username=username)
            
            # Verificamos si el usuario está en archivo histórico
            if Archivo.objects.filter(user=user).exists():
                if request:
                    messages.error(request, settings.LOGIN_ERROR_MESSAGE)
                return None
            
            # Verificamos la contraseña
            if user.check_password(password):
                return user
            
        except User.DoesNotExist:
            pass
        
        # Si llegamos aquí, las credenciales son incorrectas
        if request:
            messages.error(request, settings.LOGIN_ERROR_MESSAGE)
        return None

    def get_user(self, user_id):
        User = get_user_model()
        try:
            user = User.objects.get(pk=user_id)
            # Si el usuario existe en el archivo histórico, no permitimos la sesión
            if Archivo.objects.filter(user=user).exists():
                return None
            return user
        except User.DoesNotExist:
            return None
