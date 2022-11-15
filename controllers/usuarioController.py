from flask_restful import Resource, request
from config import conexion
from models.usuarios import UsuarioModel
from dtos.usuarioDto import UsuarioRequestDto


class UsuariosController(Resource):

    #los metodos que nosotros queramos utilizar (GET,POST) lo tendremos que definir como metodo de la clase

    def get(self):

        usuarios=conexion.session.query(UsuarioModel).all()

        serializador = UsuarioRequestDto(many=True)
        #  este metodo le pasamos información proveniente de la base de datos y lo convertira a un tipo de dato que pueda ser legible por el frontend
        data=serializador.dump(usuarios)
        # _________________________________________
        #MODO PRINCIPIANTE
        # hacer un for en el cual se iteren todos los usuarios y cada usuario convertirlo a un diccionario que tenga el siguiente formato
        #usuariosFinales=[]

        #for usuario in usuarios:
            #usuarioDiccionario={
                #'id': usuario.id,
                #'nombre': usuario.nombre,
                #'correo': usuario.correo,
                #'telefono': usuario.telefono
            #}
            #usuariosFinales.append(usuarioDiccionario)
        



        return{
        'message':'Los usuarios son:',
        'content': data
        }

    def post(self):


        body= request.get_json()
        try:
            # Instancia de mi Dto de usuario
            serializador =UsuarioRequestDto()
            dataSerializada=serializador.load(body)
            print(dataSerializada)
            #Primero creo una instancia de mi clase Model
            #para mayor informacion revisa el archivo repaso_funciones_infinitas.py
        
            nuevoUsuario =UsuarioModel(**dataSerializada)
            # aca asignamos valores a lo satributos provenientes del body
            # Insert into Uusuarios (nombre, correo, telefono) y sus Values
            # Forma principiante
            # nuevoUsuario.correo=body.get('correo')
            # nuevoUsuario.nombre=body.get('nombre')
            # nuevoUsuario.telefono=body.get('telefono')
            #ahora agregamos a la base de datos ese nuevo registro creado en base a la instancia
            conexion.session.add(nuevoUsuario)
            #guardar de manera permanente la informacion 

            conexion.session.commit()
            
            return{
                'message': 'Usuario creado exitosamente'
            }

        except Exception as error:
            print(error)
        return{
            'message': 'Error al crear el usuario',
            'content': error.args

        }

class UsuarioController(Resource):
    def get (self, id):
        usuarioEncontrado = conexion.session.query(UsuarioModel).filter_by(id=id).first()
        # utilizando el usuariorequestDto pasarle el usuarioencontrado y devolver esa informacion
        serializador = UsuarioRequestDto()
        data=serializador.dump(usuarioEncontrado)
        return {
            'content': data
        }
    def put(self,id):
        try:

            # buscare ese usuario por el id
            usuarioEncontrado= conexion.session.query(UsuarioModel).filter_by(id=id).first()
            # si no hay un usuario con ese id
            if usuarioEncontrado is None:
                raise Exception('Usuario no existe')
            body=request.get_json()
            serializador = UsuarioRequestDto()
            data= serializador.load(body)

            # podemos utilizar un try-except dentro de otro pero este funcionara solamente para el 
            #codigo que esta dentro del try y cada uno actuara de manera independiente
            
            # si el usuario no me envía el telefono entonces conservr el valor anterior pero si 
            # me envia el valo "null " ahi si le eliminamos el telefono
            telefono = usuarioEncontrado.telefono
            try:
                telefono= data['telefono']
            except:
                pass

            # aca sobreescribimos la información nueva del usuario
            usuarioEncontrado.nombre = data.get('nombre')
            usuarioEncontrado.correo = data.get('correo')
            usuarioEncontrado.telefono = telefono

            conexion.session.commit()
            return{
                'message': 'Usuario actualizado exitosamente'
            }

        except Exception as error:
            return{
                'message': 'Error al actualizar el usuario',
                'content': error.args
            }

    def delete(self,id):
        try:
            usuarioEncontrado=conexion.session.query(UsuarioModel).filter_by(id=id).first()
            if usuarioEncontrado is None:
                raise Exception('Usuario no existe')
            conexion.session.delete(usuarioEncontrado)
            conexion.session.commit()

            return{
                'message': 'El usuario se elimino exitosamente'
            }

        except Exception as error:
            return{
                'message': 'Error al eliminar el usuario',
                'content': error.args
            }


