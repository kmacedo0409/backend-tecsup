from django.contrib.auth.models import BaseUserManager
#manager es el administrador que se encargrada de la creacion del usuario por comando

class UsuarioManager(BaseUserManager):

    def create_superuser(self, correo, nombre, apellido, tipoUsuario, password):
        # metodo que se mandara a llamar cuandos e ejecute el comando createsuperuser

        if not correo:
            raise ValueError('El usuario debe indicar obligatoriamente el correo')

        correoNormalizado=self.normalize_email(correo)

        nuevoUsuario=self.model(correo=correoNormalizado, nombre=nombre, apellido=apellido, tipoUsuario=tipoUsuario)

        # este sirve para generar el hash de la contraseña para que no se guarde de manera original 

        nuevoUsuario.set_password(password)
        nuevoUsuario.is_superuser=True
        # is_staff > sirve para indicar si el usuario pertenece al equipo de trabajo y puede tener 
        nuevoUsuario.is_staff=True

        # ._db sirve para referenciar a la base de datos por default en el caso que tengamos varias conexiones a diferentes base de datos
        # de momento el self._db estara vacia por lo que usara la conexion a la base de datos por defecto, caso contrario si tuviesemos 
        # mas de una conexion a alguna base de datos entonces indicariamos a que base de datos queremos conectarnos
        # https://stackoverflow.com/questions/57667334/what-is-the-value-of-self-db-by-default-in-django
        nuevoUsuario.save(using=self._db)
