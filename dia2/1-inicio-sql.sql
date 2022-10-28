-- Esto es un comentario

-- SQL (Structured Query Language) Lenguaje estructurado de consultas
-- En SQL siempre hay que colocar el; al final de cada consulta
-- Dos sublenguajes de manejo de informacion
-- DDL (Data Definition Language) > Lenguaje de definicion de datos

-- Create
CREATE DATABASE pruebas;
-- Sirve para listar las bases de datos que hay en este servidor 
SHOW DATABASES;
USE pruebas;
-- Siempre las palabras reservadas se recomienda en mayuscula
-- Nota: las tabñas siempre deben tener nombre pluralizados
CREATE TABLE alumnos(
-- Ahora definimos las columnas
-- nombre_col_tipo_dato [parametros opcionales]
id INT PRIMARY KEY AUTO_INCREMENT,
nombre VARCHAR(100) NOT NULL,
-- ENUM es un tipo de dato que permite guardar determinados valores
sexo ENUM('FEMENINO', 'MASCULINO', 'BINARIO', 'OTRO', 'HELICOPTERO'),
-- agregar la columna tipo_documento que solamente puede ser DNI, C.E., PASAPORTE 
-- y la columna num_documento que solamente puede tener hasta 10 caracteres
tipo_documento ENUM('DNI', 'C.E', 'PASAPORTE') DEFAULT 'DNI',
num_documento VARCHAR(10) NOT NULL,
fec_nacimiento DATETIME

);
-- DML (Data Manipulation Language
-- Lenguaje de Manipulacion de datos
SELECT nombre, sexo FROM alumnos;
SELECT * FROM alumnos;

-- INSERT 
INSERT INTO alumnos (nombre, sexo, num_documento, fec_nacimiento) VALUES
					('EDUARDO', 'MASCULINO', '73500745', '1992-08-01');
INSERT INTO alumnos (nombre, sexo, num_documento, fec_nacimiento) VALUES
					('Ronald', 'BINARIO', '75268256', '1995-07-25'),
                    ('Karim', 'FEMENINO', '85234716', '1991-01-15'),
                    ('Alexa', 'HELICOPTERO', '14729583', '1995-06-08');
                    
SELECT * FROM ALUMNOS;
INSERT INTO alumnos VALUES 
                    (DEFAULT, 'Romina', 'FEMENINO', 'C.E', '456789132', '1987-05-14'),
                    (DEFAULT, 'Roberto', 'BINARIO', 'PASAPORTE', '15946789', '1985-01-01'),
                    (DEFAULT, 'Jair', 'MASCULINO', DEFAULT, '34598746', '1995-04-09');

SELECT * FROM ALUMNOS;
SELECT * FROM ALUMNOS;
-- delete from tabla WHERE condicional
DELETE FROM alumnos WHERE id>=10 AND id <=12;
SELECT * FROM ALUMNOS;
-- UPDATE tabla SET columna='Nuevo valor' WHERE condicional
UPDATE alumnos SET nombre='Marimar' WHERE id = 8;
UPDATE alumnos SET num_documento = '99564879', nombre = 'Rodrigo' WHERE id = 9;

SELECT * FROM alumnos;

INSERT INTO alumnos (nombre, sexo, num_documento, fec_nacimiento) VALUES
					('Maria Alejandra', 'BINARIO', '49596785', '1995-06-19');
                    
SELECT * FROM alumnos;

-- mostrar todos los alumnos que tengan carnet de extranjeria
-- mostrar todos los alumnos que tengan sexo masculino o femenino
-- mostrar a todos los alumnos que nacieron antes del 1990

SELECT * FROM alumnos WHERE tipo_documento = 'C.E';
SELECT * FROM alumnos WHERE sexo IN ('MASCULINO', 'FEMENINO');
SELECT * FROM alumnos WHERE fec_nacimiento < '1990-01-01';

SELECT nombre FROM alumnos WHERE nombre like '%a%';
SELECT nombre FROM alumnos WHERE nombre like '%a';
-- con la propiedad bynary le indicamos que haga la comparacion a nivel de binarios
SELECT nombre FROM alumnos WHERE nombre LIKE '%d%u%';

SELECT nombre FROM alumnos WHERE nombre LIKE '_o%';
SELECT nombre FROM alumnos WHERE nombre LIKE '%d_u%';

SELECT nombre FROM alumnos WHERE nombre LIKE '%n%';
SELECT nombrealumnos FROM alumnos WHERE num_documento LIKE '_8%';

                    
                  
