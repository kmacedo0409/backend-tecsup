from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models.usuarios import UsuarioModel

class UsuarioRequestDto(SQLAlchemyAutoSchema):
    # pasar atrubutos a la clase que estamos heredando
    class Meta:
        # Esta clase permitira definir atributos necesarias para la clase que estamos heredando
        # Model> estaremos indicando a SQLALchemyAutoschema
        model= UsuarioModel