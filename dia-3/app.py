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
# 

def inicializacion():
    conexion.create_all()
app.before_first_request(inicializacion)

@app.route('/participantes', methods=['GET'])
def participantes():
    resultado = conexion.session.query(ParticipanteModel).all()
    print(resultado)
    

app.run(debug=True)