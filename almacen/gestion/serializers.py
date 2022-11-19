from rest_framework import serializers
from .models import DepartamentoModel


class PruebaSerializer(serializers.Serializer):
    nombre = serializers.CharField(max_length=40, allow_null=False)
    apellido = serializers.CharField(allow_null=False)

class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model=DepartamentoModel
        fields= '__all__' #['id', 'nombre']
        # si quisiera utilizar todas las columnas exceptuando una o dos voy a utilizar exclue= ['nombre']
        