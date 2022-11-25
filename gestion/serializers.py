
from .models import UsuarioModel,PlatoModel
from rest_framework import serializers

class UsuarioSerializer(serializers.ModelSerializer):

    def save(self):

        
        

        nuevoUsuario=UsuarioModel(**self.validated_data)
        # encriptamos la contraseña
        nuevoUsuario.set_password(self.validated_data.get('password'))
        # 3 guardamos el usuario en la base de datos
        nuevoUsuario.save()
        return nuevoUsuario
    class Meta:
        fields= '__all__'
        model= UsuarioModel

        # Definimos un atributo llamado extra_kwargs en el cual se realiza mediante un diccionario y se utilizara para indicar parametros adicionales
        # a nuesras columnas.
        extra_kwargs={
            'password':{
                'write_only':True
            },
            'id':{
                'read_only':True
            }
        }

class PlatoSerializer(serializers.ModelSerializer):
    class Meta:
        model=PlatoModel
        fields='__all__'

        #utilizando el atributo extrakwargs indicar que solamente la disponibilidad de solo lectura

        extra_kwargs={
            'disponibilidad':{
                'read_only':True
            },
            
        }