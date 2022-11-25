
from rest_framework.generics import CreateAPIView, ListCreateAPIView, UpdateAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from .models import UsuarioModel, PlatoModel
from .serializers import UsuarioSerializer, PlatoSerializer

# Create your views here.
class RegistroUsuarioApiView(CreateAPIView):
    queryset= UsuarioModel.objects.all()
    serializer_class=UsuarioSerializer

    def post(self, request: Request):
        informacion = self.serializer_class(data= request.data)
        es_valida=informacion.is_valid()
        if not es_valida:
            return Response(data={
                'message': 'Error al crear el usuario',
                'content': informacion.errors
            }, status=status.HTTP_400_BAD_REQUEST)

        else:
            nuevoUsuario=informacion.save()
            nuevoUsuarioSerializado = self.serializer_class(instance=nuevoUsuario)
            return Response(data={
                'message':'Usuario creado exitosamente, ya se puede loguear',
                'content': nuevoUsuarioSerializado.data
            }, status=status.HTTP_201_CREATED)

class PlatosApiView(ListCreateAPIView):
    queryset=PlatoModel.objects.all()
    serializer_class=PlatoSerializer

    def post(self, request:Request):
        data=self.serializer_class(data=request.data)
        data.is_valid(raise_exception=True)
        nuevoPlato=data.save()
        return Response(data={
            'message': 'plato creado exitosamente',
            'content': self.serializer_class(instance=nuevoPlato).data
        })

    def get(self, request: Request):
        # ejecuta el queryset para que otraves se vuelva a llamar a la extraccion de la informacion
        platos=PlatoModel.objects.filter(disponibilidad=True).all()
        # many sirve para indicar al serializador que se le pasara un conjunto de instancias y las tiene que iterar para poder serializarlas/ deserializarlas
        platos_serializados=self.serializer_class(instance=platos, many=True)

        return Response(data={
            'message': 'Los platos son:',
            'content': platos_serializados.data
        })

class PlatoToggleApiView(UpdateAPIView):
    queryset=PlatoModel.objects.all()
    serializer_class=PlatoSerializer
    def put(self, request:Request, id: str):
        # primero buscamos si existe el plato
        # select * from platos Where id= 

        platoEncontrado = PlatoModel.objects.filter(id = id).first()
        if platoEncontrado is None:
            return Response(data={
                'message': 'plato no encontrado'
            }, status=status.HTTP_404_NOT_FOUND)
        # actualizare el estado de la disponibilidad 
        # la nueva disponibilidad sera la anterior al reves
        platoEncontrado.disponibilidad = not platoEncontrado.disponibilidad
        platoEncontrado.save()
        return Response(data={
            'message': 'plato actualizado exitosamente',
            'content': self.serializer_class(instance=platoEncontrado).data
        }, status=status.HTTP_201_CREATED)

class PlatoUpdateApiView(UpdateAPIView):
    queryset=PlatoModel.objects.all()
    serializer_class=PlatoSerializer