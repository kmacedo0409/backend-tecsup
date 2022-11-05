from flask import Flask, render_template, request
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

@app.route('/mostrar_estudiantes', methods=['GET'])
def devolver_estudiantes():
    cursor=mysql.connection.cursor()
    cursor.execute("SELECT * FROM estudiantes")
    resultado = cursor.fetchall()
    print(resultado)
    resultado_final=[]
    for estudiante in resultado:
        print(estudiante)
        estudiante_diccionario ={
            'id': estudiante[0],
            'nombre': estudiante[1],
            'ape_paterno': estudiante[2],
            'ape_materno': estudiante [3],
            'correo': estudiante[4],
            'num_emergencia': estudiante[5],
            'curso_id': estudiante[6]
        }
        print(estudiante_diccionario)
        resultado_final.append(estudiante_diccionario)


    #return{
    #   'message': 'Los estudiantes son:',
    #   'content': resultado_final
    #}

    return render_template('mostrar_estudiantes.html', estudiantes=resultado_final, mensaje='Hola desde Flask')

@app.route("/agregar_estudiante", methods=['GET','POST'])
def agregar_estudiante():
    print(request.method)
    if request.method == 'GET':
        return render_template('agregar_estudiante.html')
    elif request.method == 'POST':
        body = request.get_json()
        print(body)
        cursor=mysql.connection.cursor()
        cursor.execute("INSERT INTO estudiantes (id, nombre, ape_paterno, ape_materno, correo, num_emergencia) VALUES (DEFAULT, '%s', '%s', '%s', '%s', '%s' )" % (
            body.get('nombre'), body.get('ape_paterno'), body.get('ape_materno'), body.get('correo'), body.get('num_emergencia')))

        mysql.connection.commit()
        cursor.close()
        return{
            'message': 'estudiante agregado exitosamente'
        }


app.run(debug=True)
