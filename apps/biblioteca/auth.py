from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from .models import Archivo

class ArchivoAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        # Primero intentamos autenticar usando el backend por defecto
        user = super().authenticate(request, username=password, **kwargs)
        
        if user:
            # Si el usuario existe en el archivo histórico, no permitimos el login
            if Archivo.objects.filter(user=user).exists():
                return None
        
        return user

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
