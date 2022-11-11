from marshmallow import Schema, fields

# dto objeto de transferencia de datos

class PruebaDto(Schema):


    id= fields.Int()
    nombre = fields.Str(required=True, error_messages={'required': 'Este campo es obligatorio'})
    correo= fields.Email(error_messages={'invalid': 'Correo electronico inválido'})