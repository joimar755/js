CREATE TABLE `empleados`(
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `nombre` VARCHAR(255) NOT NULL,
    `apellidos` VARCHAR(255) NOT NULL,
    `puesto` VARCHAR(255) NOT NULL,
    `salario` DECIMAL(8, 2) NOT NULL,
    `edad` VARCHAR(255) NOT NULL,
    `celular` VARCHAR(255) NOT NULL,
    `dirección` VARCHAR(255) NOT NULL
);
INSERT INTO empleados VALUES (1, 'Juan', 'Perez Lopez', 'Gerente', 75000.00, '45', '5551234567', 'Calle Principal 123');
INSERT INTO empleados VALUES (2, 'Maria', 'Gomez Sanchez', 'Contadora', 48000.50, '30', '5559876543', 'Avenida Central 456');
INSERT INTO empleados VALUES (3, 'Carlos', 'Hernandez Diaz', 'Ingeniero', 55000.00, '35', '5556547890', 'Boulevard del Sol 789');
INSERT INTO empleados VALUES (4, 'Ana', 'Martinez Ruiz', 'Diseñadora', 47000.00, '28', '5554321098', 'Calle de la Luna 321');
INSERT INTO empleados VALUES (5, 'Luis', 'Ramirez Torres', 'Vendedor', 42000.00, '40', '5558765432', 'Calle del Rio 654');
INSERT INTO empleados VALUES (6, 'Sofia', 'Fernandez Jimenez', 'Secretaria', 38000.00, '25', '5555678901', 'Avenida del Bosque 987');
INSERT INTO empleados VALUES (7, 'Jorge', 'Lopez Garcia', 'Analista', 52000.00, '33', '5552345678', 'Boulevard de las Flores 111');
INSERT INTO empleados VALUES (8, 'Elena', 'Castro Morales', 'Supervisora', 60000.00, '37', '5556789012', 'Calle del Parque 222');
INSERT INTO empleados VALUES (9, 'Roberto', 'Vega Herrera', 'Tecnico', 45000.00, '29', '5553456789', 'Avenida del Lago 333');
INSERT INTO empleados VALUES (10, 'Laura', 'Sanchez Ortega', 'Recepcionista', 36000.00, '26', '5557890123', 'Calle del Jardin 444');

select nombre, salario from  empleados where salario > 45000.00;
select puesto, nombre from  empleados where edad > '30';
update empleados set salario = 8525.00 where id = 2;
update empleados set salario = 8525.00 where id = 6;

update empleados set celular = 35890000 where id = 7;
update empleados set celular = 39500050 where id = 8; 

delete from empleados where id = 9;
delete from empleados where id = 10;

drop table empleados;


select * from empleados;
