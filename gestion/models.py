from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .authManager import UsuarioManager

# Create your models here.

class PlatoModel(models.Model):
    id= models.AutoField(primary_key=True, null=False, unique=True)
    nombre=models.CharField(max_length=50, null=False)
    precio=models.DecimalField(max_digits=5, decimal_places=1, null=False)
    disponibilidad=models.BooleanField(default=True)
    fechaCreacion=models.DateTimeField(auto_now_add=True, db_column='fecha_creacion')




    class Meta:
        db_table='platos'
        ordering=['-precio']

class UsuarioModel(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True, unique=True)
    nombre=models.CharField(max_length=50, null=False)
    apellido=models.CharField(max_length=50, null=False)
    correo=models.EmailField(max_length=50, unique=True, null=False)
    password=models.TextField(null=False)
    tipoUsuario=models.CharField(max_length=40, choices=[('ADMIN', 'ADMIN'), ('USER', 'USER')], db_column='tipo_usuario')

    # utilizamos los siguientes atributos si queremos seguir trabajando con el pane administrativo 
    is_staff = models.BooleanField(default=False)
    is_active= models.BooleanField(default=True)
    createdAt= models.DateTimeField(auto_now_add=True, db_column='created_at')


    objects = UsuarioManager()
    USERNAME_FIELD='correo'

    REQUIRED_FIELDS= ['nombre', 'apellido', 'tipoUsuario']

    class Meta:
        db_table ='usuarios'

