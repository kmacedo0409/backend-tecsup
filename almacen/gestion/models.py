from django.db import models

class DepartamentoModel(models.Model):
    id = models.AutoField(primary_key=True, unique=True, null=False)
    nombre = models.CharField(max_length=50, null=False)
    codigoPostal = models.CharField(max_length=10, unique=True, db_column='codigo_postal')

    class Meta:
        db_table='departamentos'

class AlmacenModel(models.Model):
    tipoAlmacen =[
        ('A', 'SECO'), 
        ('B', 'SEMI-SECO'), 
        ('C', 'HUMEDO')
        ]

    class TipoAlmacenOpciones(models.TextChoices):

        SECO= ('A', 'SECO')
        SEMISECO=('B', 'SEMI-SECO')
        HUMEDO=('C', 'HUMEDO')
    espacioAnaquel=models.IntegerField(db_column='espacio_anaquel')
    tipo=models.CharField(max_length=100, choices=tipoAlmacen)
    direccion=models.TextField()
    # RELACIONES ONE-TO-ONE
    # on_delete > se guardara la informacion de como debe actuar el almacen si es que se elimina el departamento (el registro con ese modelo)
    # CASCADE > se elimina el departamento y en forma de cascada se elimina el almacen
    # PROTECT > evita la eliminacion y lanza un error de tipo ProtectedError
    # RESTRICT > muy similar al PROTECT pero emite un error de tipo RestrictedError
    # SET_NULL > elimina el departamento y a este valor lo cambia a null
    # SET_DEFAULT > elimina el departamento pero tenemos que indicar un valor por default para que le cambie a ese valor
    # DO_NOTHING > elimina el departamento PERO conserva el valor (FK) con lo que genera una mala integridad de informacion, NO USAR ESTE porque malogra la calidad de la data

    departamento = models.OneToOneField(to=DepartamentoModel, on_delete=models.CASCADE,
    db_column='departamento_id')

    class Meta:
        db_table= 'almacenes'


# Create your models here.
