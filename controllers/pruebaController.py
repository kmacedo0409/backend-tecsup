from flask_restful import Resource, request
from marshmallow.exceptions import ValidationError
from dtos.prueba import PruebaDto

class PruebaController(Resource):
    def post(self):
        try:
            data= request.get_json()
            validador=PruebaDto()
            dataValidada = validador.load(data)
            print(dataValidada)
            return{
                'message':'ok'
            }

        except ValidationError as error:
            return{
                'message': 'Error al hacer la consulta',
                'content':  error.args
            }