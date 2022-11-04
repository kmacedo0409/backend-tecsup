-- Utilizando la base de datos colegio, crear la tabla de los padres de los estudiantes
CREATE TABLE padres(
id INT PRIMARY KEY AUTO_INCREMENT,
nombre VARCHAR(200) NOT NULL,
ape_paterno VARCHAR(50) NOT NULL,
ape_materno VARCHAR(50) NOT NULL,
telefono VARCHAR (10) NOT NULL
);
CREATE TABLE estudiantes_padres(
id INT PRIMARY KEY AUTO_INCREMENT,
padre_id INT,
estudiante_id INT,
-- Haciendo referencia hacia las tablas respectivas
FOREIGN KEY (padre_id) REFERENCES padres(id),
FOREIGN KEY (estudiante_id) REFERENCES estudiantes(id)
);
INSERT INTO padres VALUES (DEFAULT, 'Juan', 'Rodriguez', 'Cano', '925364155'),
                          (DEFAULT, 'Angel', 'Sanchez', 'Baldarrago', '936205489'),
                          (DEFAULT, 'Jimmy', 'Jara', 'Pomareda', '914253689'),
                          (DEFAULT, 'Juan', 'Barrientos', 'Romero', '936259568'),
                          (DEFAULT, 'Nohemi', 'Ayala', 'Romero', '929655748'),
                          (DEFAULT, 'Christian', 'Martinez', 'Martinez', '976859245');
                          
INSERT INTO estudiantes_padres VALUES   (DEFAULT, 1,3),
										(DEFAULT, 1,2),
										(DEFAULT, 2,1),
										(DEFAULT, 3,2),
										(DEFAULT, 5,6),
										(DEFAULT, 3,6),
										(DEFAULT, 4,6),
										(DEFAULT, 4,4),
										(DEFAULT, 6,5),
										(DEFAULT, 6,4);
                                        
                                        
-- listar todos los padres y sus alumnos_padres
-- listar todos los alumnos y sus alumnos_padres (usando inner join)

SELECT * FROM padres INNER JOIN estudiantes_padres ON padres.id = estudiantes_padres.padre_id;
SELECT * FROM estudiantes INNER JOIN estudiantes_padres ON estudiantes.id = estudiantes_padres.estudiante_id;

SELECT * 
FROM estudiantes 
    INNER JOIN estudiantes_padres ON estudiantes.id = estudiantes_padres.estudiante_id
    INNER JOIN padres ON estudiantes_padres.padre_id = padres.id
    INNER JOIN cursos ON estudiantes.curso_id = cursos.id
WHERE padres.ape_paterno in ('Rodriguez', 'Jara');