CREATE DATABASE colegio;
USE colegio;
-- En la bd colegio necesitamos almacenar los alumnos pero con la siguiente informacion:
-- id PK entero autoincrementable, nombre string hasta 100 caracteres, ape_paterno string
-- hasta 50 caracteres, ape_materno string hasta 50 caracteres, correo no se puede repetir va a ser
-- texto, num_emergencia string hasta 10 caracteres.
CREATE TABLE estudiantes(
id INT PRIMARY KEY AUTO_INCREMENT,
nombre VARCHAR (100) NOT NULL,
ape_paterno VARCHAR (50) NOT NULL,
ape_materno VARCHAR (50),
correo VARCHAR (250) UNIQUE NOT NULL,
num_emergencia VARCHAR (10),
curso_id INT,
FOREIGN KEY (curso_id ) REFERENCES cursos (id)
);
DROP TABLE cursos;
DROP TABLE estudiantes;
CREATE TABLE cursos(
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    color TEXT,
    dificultad ENUM('FACIL','MEDIO','DIFICIL')
);

CREATE TABLE estudiantes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    ape_paterno VARCHAR(50) NOT NULL,
    ape_materno VARCHAR(50) NOT NULL,
    correo VARCHAR(250) UNIQUE NOT NULL,
    num_emergencia VARCHAR(10),
    -- Creo una columna referenciando segun el nombre de la tabla_nombre columna
    curso_id INT,
    -- Ahora relacionamos esa columna con la tabla alumnos
    FOREIGN KEY(curso_id) REFERENCES cursos(id)
);
INSERT INTO cursos VALUES   (DEFAULT, 'MATEMATICA', 'AMARILLO', 'MEDIO'),
                            (DEFAULT, 'CTS', 'NARANJA', 'DIFICIL'),
                            (DEFAULT, 'ARTE', 'MORADO', 'FACIL'),
                            (DEFAULT, 'EDUCACION FISICA', 'VERDE', 'MEDIO'),
                            (DEFAULT, 'INGLES', 'CELESTE', 'FACIL'),
                            (DEFAULT, 'COMUNICACION', 'ROJO', 'DIFICIL');
                            
INSERT INTO estudiantes VALUES  (DEFAULT, 'Eduardo', 'de Rivero', 'Manrique', 'ederiveroman@gmail.com','974207075',1),
                            (DEFAULT, 'Carla', 'Monterrosa', 'Macedo', 'cmonterrosa@gmail.com','974207074',3),
                            (DEFAULT, 'Juan', 'Perez', 'Rodriguez', 'jperez@gmail.com','974207076',5),
                            (DEFAULT, 'Rodrigo', 'Buenaventura', 'Rodrigues', 'rbuenaventura@gmail.com','974159075',2),
                            (DEFAULT, 'Sofia', 'Baldarrago', 'Vera', 'sbaldarrago@gmail.com','972503648',6);
                            
SELECT * FROM estudiantes;
SELECT * FROM cursos;

-- seleccionar todos los cursos que sean facil o dificil 
-- seleccionar todos los cursos que sean color amarillo o celeste y que sean dificultad medio 

SELECT * FROM cursos WHERE dificultad IN ('FACIL', 'DIFICIL');
SELECT * FROM cursos WHERE color IN ('AMARILLO', 'CELESTE') AND dificultad= 'MEDIO';

SELECT * FROM estudiantes INNER JOIN cursos ON estudiantes.curso_id=cursos.id WHERE correo LIKE '%gmail%';
INSERT INTO estudiantes VALUES (DEFAULT, 'Jhonatan', 'Maicelo', 'Roman', 'jmaicelo@gmail.com', '925361048', NULL);

-- LEFT JOIN
SELECT * FROM estudiantes LEFT JOIN cursos ON estudiantes.curso_id = cursos.id;

-- RIGHT JOIN
SELECT * FROM estudiantes RIGHT JOIN cursos ON estudiantes.curso_id = cursos.id;