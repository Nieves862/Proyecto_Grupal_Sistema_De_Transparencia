#--Evidencia I

create database sistema_de_transparencia;
--

use sistema_de_transparencia;
--

create table cuarto_año (
ID_Estudiante int auto_increment,
Apellido varchar(20) not null,
Nombre varchar(15) not null,
E_mail VARCHAR(40) NULL DEFAULT NULL,
Sexo char (1) null,
DNI int (8) not null,
Fecha_De_Nacimiento date not null,
Edad integer (2) unsigned not null,
Dirección varchar (35),
Localidad varchar (20),
Provincia varchar (15),
primary key (ID_Estudiante),
UNIQUE INDEX E_mail (E_mail ASC) VISIBLE)
ENGINE = InnoDB
AUTO_INCREMENT = 1
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;
--

insert into cuarto_año (Apellido, Nombre, E_mail, Sexo, DNI, Fecha_De_Nacimiento, Edad, Dirección, Localidad, Provincia) 
values ('RINCON', 'Avril', 'rincona@escuelasproa.edu.ar', 'F','49223074', '2009/04/16', '15', 'Río Negro', 'Despeñaderos', 'Cba'),
       ('GALAN', 'Candelaria', 'galana@escuelasproa.edu.ar','F', '49223069', '2009/03/27','15', 'Zona Rural', 'Despeñaderos', 'Cba'),
       ('LURASCHI', 'Tiara', 'luraschit@escuelasproa.edu.ar','F', '48669838', '2008/11/19','15', 'Argentina', 'Despeñaderos', 'Cba'),
       ('MERCADO', 'Matias', 'mercadom@escuelasproa.edu.ar','M', '48469838', '2008/11/12','15', 'Independencia', 'Despeñaderos', 'Cba'),
       ('ARREGUI', 'Agustina', 'arreguia@escuelasproa.edu.ar', 'F', '48452855', '2008/07/10','15', 'Intendente Penna', 'Despeñaderos', 'Cba');
       --
       
       select @@sql_safe_updates;
       set SQL_SAFE_UPDATES=1;
       set SQL_SAFE_UPDATES=0;
       --
       
       update cuarto_año set Provincia ='Córdoba';
       --
       
       describe cuarto_año;
       --

CREATE TABLE IF NOT EXISTS materia(
ID_Materia INT NOT NULL AUTO_INCREMENT,
Espacio VARCHAR(25) NOT NULL,
Profesor VARCHAR(25) NOT NULL,
Detalle TEXT NULL DEFAULT NULL,
Carga_Horaria INT NOT NULL,
PRIMARY KEY (ID_Materia))
ENGINE = InnoDB
AUTO_INCREMENT = 6
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;
--

CREATE TABLE IF NOT EXISTS asistencia (
ID_Asistencia INT NOT NULL AUTO_INCREMENT,
ID_Estudiante INT NOT NULL,
ID_Materia INT NOT NULL,
Fecha_Clase DATE NOT NULL,
Asistencia ENUM('Presente', 'Ausente') NOT NULL,
Justificación TEXT NULL DEFAULT NULL,
PRIMARY KEY (ID_Asistencia),
INDEX ID_Estudiante (ID_Estudiante ASC) VISIBLE,
INDEX ID_Materia (ID_Materia ASC) VISIBLE,
CONSTRAINT asistencia_ibfk_1
FOREIGN KEY ( ID_Estudiante)
REFERENCES cuarto_año (ID_Estudiante),
CONSTRAINT asistencia_ibfk_2
FOREIGN KEY (ID_Materia)
REFERENCES materia (ID_Materia))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;
--

CREATE TABLE IF NOT EXISTS grupo (
ID_Grupo INT NOT NULL AUTO_INCREMENT,
Nombre_Grupo VARCHAR(50) NOT NULL,
ID_Estudiante INT NOT NULL,
PRIMARY KEY (ID_Grupo),
INDEX ID_Estudiante (ID_Estudiante ASC) VISIBLE,
CONSTRAINT grupo_ibfk_1
FOREIGN KEY (ID_Estudiante)
REFERENCES cuarto_año (ID_Estudiante))
ENGINE = InnoDB
AUTO_INCREMENT = 21
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;
--

CREATE TABLE IF NOT EXISTS nota_formativa (
ID_NOTA_Formativa INT NOT NULL AUTO_INCREMENT,
ID_Estudiante INT NOT NULL,
ID_Materia INT NOT NULL,
Nota INT NULL DEFAULT NULL,
Fecha_Exámen DATE NOT NULL,
Tipo_Exámen ENUM ('Recuperatorio','Final') NOT NULL,
PRIMARY KEY (ID_Nota_Formativa),
INDEX ID_Estudiante (ID_Estudiante ASC) VISIBLE,
INDEX ID_Materia (ID_Materia ASC) VISIBLE,
CONSTRAINT nota_formativa_ibfk_1
FOREIGN KEY (ID_Estudiante)
REFERENCES cuarto_año (ID_Estudiante),
CONSTRAINT nota_formativa_ibfk_2
FOREIGN KEY (ID_Materia)
REFERENCES materia (ID_MATERIA))
ENGINE = InnoDB
AUTO_INCREMENT = 51
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;
--
