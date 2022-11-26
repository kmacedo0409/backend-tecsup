from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.request import Request
from django.contrib.auth.models import AnonymousUser

class SoloAdmin(BasePermission):
    message = 'Tu no tienes los permisos necesarios'
   
    def has_permission(self, request:Request, view):

        # el safe methods es un listado en el cual me muestra los metodos seguros ( los que nos afectan la modificacion de datos ())
        print(SAFE_METHODS)
        if request.method in SAFE_METHODS:

            # si el metodo que se esta utilizando para acceder es get options o head  no necesita 
            return True
            # si no se esta proveyendo una token el request.user sera un usuario anonimo
        if isinstance(request.user, AnonymousUser):
            return False
        #print(request.user)
        #print(view)
        if request.user.tipoUsuario == 'ADMIN':
            return True
        else:

            return False
        