# las tablas que originalmente las creamos en la base de datos directamente, 
# ahora se crearan en forma de clases y cada tributo será una columna de esa tabla.
from config import conexion
from sqlalchemy import Column, types

#asi seria si queremos utilizar un tipo de dato de una bd en especifico 
# from sqlalchemy.dialects.mysql import Json
class ParticipanteModel(conexion.Model):
    # Ahora esta clase tendrá un comportamiento como si fuera una tabla, es decir todos sus atributos formaran columnas
    id = Column(type_= types.Integer, autoincrement=True, primary_key=True)
    nombre = Column(type_=types.String(length=45), nullable=False)
    apellido= Column(type_ =types.String(length=50), nullable=False)

    __tablename__ = 'participantes'