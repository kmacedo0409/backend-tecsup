from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import PruebaSerializer, DepartamentoSerializer
from rest_framework import status
from .models import DepartamentoModel

@api_view(http_method_names=['GET', 'POST'])
def saludar(request: Request):

    # request.data > es el cuerpo (body) que me envía el cliente
    print(request.data)
    # es la informacion enviada por la Url pero en formato de llave =valor
    print(request.query_params)
    if request.method == 'GET':
        return Response(data={
        'message': 'Bienvenido a mi API'
    }, status=200)
    elif request.method == 'POST':
        body = request.data
        nombre = body.get('nombre')

        # EN BASE AL NOMBRE QUE VAMOS A RECIBIR POR EL BODY EN VEZ DE QUE DIGA
        return Response(data={
            'message': 'Hola {}'.format(nombre)
            
           
            
        })

@api_view(http_method_names=['GET'])
def parametros(request: Request, nombre):
    print(nombre)
    return Response(data={
        'message': 'Bienvenido al endpoint de parametros'
    })

class PruebaApiView(ListCreateAPIView):

    serializer_class= PruebaSerializer
    queryset = [{
        'nombre':'Eduardo',
        'apellido': 'De Rivero'
    },{
        'nombre':'Raul',
        'apellido': 'Martinez'
    }, {
        'nombre':'Ximena',
        'apellido': 'Recabarren'
    

    }]

    def post(self, request:Request):
        print(request.data)
        body=request.data
        serializador = PruebaSerializer(data=body)
        dataValida = serializador.is_valid()
        if not dataValida:
            return Response(data={
            'message': 'Data incorrecta',
            'content': serializador.errors
            })
        else:
            print(serializador.validated_data)
            self.queryset.append(serializador.validated_data)
        return Response(data={
            'message': 'Usuario agregado exitosamente'
        }, status=status.HTTP_201_CREATED)

class DepartamentosApiView(ListCreateAPIView):
    serializer_class=DepartamentoSerializer
    queryset = DepartamentoModel.objects.all()

class DepartamentoApiView(RetrieveUpdateDestroyAPIView):
    serializer_class =DepartamentoSerializer
    queryset=DepartamentoModel.objects.all()


# Tarea realizar el crud con los almacenes
