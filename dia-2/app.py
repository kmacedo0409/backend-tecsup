from flask import Flask, render_template
from flask_mysqldb import MySQL
from os import environ
from dotenv import load_dotenv

load_dotenv()

# print(environ)
app= Flask(__name__)
# ALMACENA TODAS LAS VARIABLES DE CONFIGURACION DE LA APLICACION DE FLASK
app.config['MYSQL_HOST']= environ.get('MYSQL_HOST')
app.config['MYSQL_USER']= environ.get('MYSQL_USER')
app.config['MYSQL_PASSWORD']= environ.get('MYSQL_PASSWORD')
app.config['MYSQL_DB']= environ.get('MYSQL_DB')
app.config['MYSQL_PORT']= int(environ.get('MYSQL_PORT'))



#print (app.config)
mysql=MySQL(app)



# un decorador es la forma en la cual nosotros podemos modificar el comportamiento de un método de una clase sin la
# necesidad de modificarlo directamente, es como utilizar la herencia para poder modificar su comportamiento, 
# en este caso, dependiendo de sus rutas y su metodo
@app.route('/', methods=['GET'])
def inicio():
    return{
        'message': 'Bienvenido a mi Api de colegios'
    }


@app.route('/inicio', methods=['GET'])
def pagina_inicial():
    return render_template('inicio.html')

@app.route('/estudiantes', methods=['GET'])
def devolver_estudiantes():
    cursor=mysql.connection.cursor()
    cursor.execute("SELECT * FROM estudiantes")
    resultado=cursor.fetchall()
    print(resultado)
    return{
        'message': 'Los estudiantes son:'
    }


app.run(debug=True)
