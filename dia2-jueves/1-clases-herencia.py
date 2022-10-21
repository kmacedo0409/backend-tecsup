#herencia > sirve para reutilizar una clase previamente definida

class Usuario:
    def __init__(self, nombre, apellido, correo):
        self.nombre=nombre
        self.apellido=apellido
        self.correo=correo

    def mostrar_resumen(self):
        return{
            "nombre":self.nombre,
            "apellido":self.apellido,
            "correo":self.correo
        }
class Alumno(Usuario):
    def __init__(self,nombre, apellido, correo, telefono_emergencia):
        self.telefono_emergencia=telefono_emergencia
        super().__init__(nombre, apellido, correo)
    def saludar(self):
        print("Hola soy la clase alumno y el nombre es {}" .format(self.nombre))
    def mostrar_resumen(self):
        # Polimorfismo >poli>muchas| morfa>muchas formas
        resumen=super().mostrar_resumen()
        resumen["telefono_emergencia"]=self.telefono_emergencia
        return resumen

usuario01=Usuario(nombre="karina", apellido="Macedo", correo="kmacedo0409@gmail.com")

print(usuario01.mostrar_resumen())
alumno01=Alumno("Juan", "Martinez", "jmartinez@yahoo.es","976489076")
alumno01.saludar()
print(alumno01.mostrar_resumen())