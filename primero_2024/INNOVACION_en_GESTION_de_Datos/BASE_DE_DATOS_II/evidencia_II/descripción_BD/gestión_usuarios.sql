#1 Creación de la Base de Datos:----------------------------------
CREATE DATABASE gestion_usuarios;
#2 Selecciona la base de datos para empezar a trabajar en ella:---
USE gestion_usuarios;
#3 Creación de las Tablas Usuario y Acceso------------------------
CREATE TABLE Usuario (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    User_name VARCHAR(50) UNIQUE NOT NULL,
    Password  VARCHAR(255) NOT NULL,
    E_mail VARCHAR(100) UNIQUE NOT NULL
);
-------------------------------------------------------------------
CREATE TABLE Acceso (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Fecha_Ingreso DATETIME NOT NULL,
    Fecha_Salida DATETIME,
    Usuario_Logueado INT,
    FOREIGN KEY (Usuario_Logueado) REFERENCES Usuario(id) ON DELETE CASCADE
);
#5 Inserción de Datos de Prueba:-------------------------------------
INSERT INTO Usuario (User_name, Password, E_mail) VALUES
('RINCONAvril', '4922307424', 'aerincnvergara@escuelasproa.edu.ar'),
('GALANCandelaria', '4922306924', 'cgalanvergara@escuelasproa.edu.ar'),
('LURASCHITiara', '4866983824', 'tluraschi@escuelasproa.edu.ar'),
('MERCADOMatias', '4846983824', 'mbmercado@escuelasproa.edu.ar'),
('ARREGUIAgustina', '4845285524', 'aarreguipicca@escuelasproa.edu.ar');
#6-------------------------------------------------------------------------------
INSERT INTO Acceso (Fecha_Ingreso, Fecha_Salida, Usuario_Logueado) VALUES
('2024-08-06 17:00:00', '2024-08-06 19:00:00', 1),
('2024-08-05 14:00:00', '2024-08-05 16:00:00', 1),
('2024-09-04 10:30:00', '2024-09-04 12:30:00', 2),
('2024-09-03 08:00:00', NULL, 3);
#7 Operaciones CRUD para la Tabla Usuario: Agregar un Nuevo Usuario:--------------
INSERT INTO Usuario (User_name, Password, E_mail) VALUES
('ZARATEJazmín', '4922308024', 'jzarate@escuelasproa.edu.ar'),
('CARRIZOAgustina', '4922305624','macarrizo@escuelasproa.edu.ar');
# Modificar un Usuario:----------------------------------------------------------
UPDATE Usuario
SET E_mail = 'acarrizo@escuelasproa.edu.ar'
WHERE User_name = 'CARRIZOAgustina';
# Eliminar un Usuario (por User_name o E_mail): ------------------------------------
DELETE FROM Usuario
WHERE User_name = 'ZARATEJazmín';
-------------------------------------------------------------------------------------
DELETE FROM Usuario
WHERE E_mail = 'jzarate@escuelasproa.edu.ar';
# Buscar por User_name o E_mail:------------------------------------------------------
SELECT * FROM Usuario
WHERE User_name = 'MERCADOMatias';
-------------------------------------------------------------------------------------
SELECT * FROM Usuario
WHERE E_mail = 'mbmercado@escuelasproa.edu.ar';
# Mostrar Todos los Usuarios:--------------------------------------------------------
SELECT * FROM Usuario;
#8 Consultas SQL con JOIN - Obtener Todos los Accesos de un Usuario Específico:------
SELECT Acceso.ID, Acceso.Fecha_Ingreso, Acceso.Fecha_Salida
FROM Acceso
JOIN Usuario ON Acceso.Usuario_Logueado = Usuario.ID
WHERE Usuario.User_name = 'GALANCandelaria';
# Listar Usuarios con la Cantidad de Accesos que Tienen:-----------------------------
SELECT Usuario.User_name, Usuario.E_mail, COUNT(Acceso.ID) AS cantidadAccesos
FROM Usuario
LEFT JOIN Acceso ON Usuario.ID = Acceso.Usuario_Logueado
GROUP BY Usuario.ID, Usuario.User_name, Usuario.E_mail;
