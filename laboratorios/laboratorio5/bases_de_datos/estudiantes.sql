CREATE TABLE Estudiantes(
  id int AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(100) NOT NULL,
  edad INT NOT NULL,
  ciudad VARCHAR(100) NOT NULL
)

INSERT INTO Estudiantes (id,nombre, edad, ciudad) VALUES
(1,'María Gómez', 20, 'Bogota'),
(2,'Juan Pérez', 22, 'Medellin'),
(3,'Ana Torres', 19, 'Cali'),
(4,'Luis Martínez', 21, 'Barranquilla'),
(5,'Carla Sánchez', 23, 'Cartagena');
select * from Estudiantes
select nombre, ciudad  from Estudiantes WHERE ciudad = 'Medellin';
select nombre, edad  from Estudiantes WHERE edad > 20
