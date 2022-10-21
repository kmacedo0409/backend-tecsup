from xmlrpc.client import ServerProxy


def sumar(num1, num2, num3):
    return num1 + num2 + num3


def sumar_n_numeros(*args):
    # args > arguments sera recibir N (ilimitado) numero de parametros
    print(args)
    # sumar todos los valores de la tupla args utilizando un for
    total = 0
    # Utilizando el contenido de la tupla directamente
    for numero in args:
        total = total + numero
    
    # Usando los numeros de las posiciones
    total2= 0    
    for posicion in range(len(args)):
        total2 = total2 + args[posicion]
    
    print(total2)
    return total

print(sumar(5,10, 7))

resultado = sumar_n_numeros(10,5,18,7,22,56,89)
print(resultado)

resultado = sumar_n_numeros(10,5,18,7,22,56,89,15,14,13,15,18,19,14,17,20)
print(resultado)

def filtro(**kwargs):
    #kwargs keyword argument> recibiremos un numero ilimitado de parametros pero utilizando el nombre del parametro y su valor
    print(kwargs)
    for llave in kwargs.keys():
        print(llave)
        valor=kwargs.get(llave)
        print(llave, ":", valor)


filtro(nombre="eduardo", edad=33, sexo="M")
filtro(nombre="eduardo", edad=33, sexo="M", nacionalidad="peruano")

curso={
    "nombre":"Matematica",
    "dificultad":"Intermedio",
    "experiencia":"ninguna"
}
print(curso)
print(curso.keys())
print(curso.values())
print(curso["dificultad"])

curso["mas_info"]="esta es una informacion adicional"
print(curso)
