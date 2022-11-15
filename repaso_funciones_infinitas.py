def prueba(**argumentos):
    print(argumentos)


prueba(nombre='eduardo', apellido='de rivero')

persona={

    'nombre':'eduardo',
    'apellido': 'de rivero'
}

prueba(persona=persona)

# cuando nosotros en una funcion pasamos un DICCIONARIO pero con doble asterisco antes (** )significa que sacrá las llaves 
# (keys) 
prueba(**persona)
prueba(nombre=persona['nombre'], apellido=persona['apellido'])

def saludar(nombre, apellido):
    print(nombre,apellido)

usuario={
    'nombre': 'eduardo',
    'apellido':'de rivero'
}
usuario2={
    'nombrecito':'juanito'
}

saludar(**usuario)
saludar (**usuario2)
saludar(nombrecito='pedrito')