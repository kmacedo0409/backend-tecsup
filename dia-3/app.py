from flask import Flask
from config import conexion
from models.participantes import ParticipanteModel
app = Flask(__name__)
# formato para las cadenas de conexion de las bases de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Karinita1989@localhost:3306/flask_sqlalchemy'

# configuro mi conexion de sqlalchemy con la aplicacion de flask
conexion.init_app(app)
#indicaremos la creacion de las nuevas tablas que no se encuentran registradas en la base de datos PERO esos modelos, 
# tiene que ser utilizado en el proyecto para que se pueda crear la tabla en la base de datos, emitira un error si no logro conectar a la base de datos
# PARA UTILIZAR EL METODO CREATE_ALL NECESITA ESTA DENTRODE UN ENDPOINT O UNA FUNCIONABILIDAD DE FLASK, EN ESTE CASOE STAMOS UTILIZANDO UN METODO LLAMDO BEFORE_FIRST
# QUE SE JECUTARA ANTES DE REALIZAR LA PRIMERA PETICION DE LA API.

def inicializacion():
    conexion.create_all()
app.before_first_request(inicializacion)

@app.route('/participantes', methods=['GET'])
def participantes():
    # SELECT * FROM participantes
    resultado = conexion.session.query(ParticipanteModel).all()
    print(resultado)
    print(resultado[0].nombre)
    print(resultado[0].apellido)
    return{
        'message': 'Los participantes son'
    }
    
app.run(debug=True)