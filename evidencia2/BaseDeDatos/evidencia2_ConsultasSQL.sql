-- Active: 1728175686495@@127.0.0.1@3306@evidencia2
#CRUD
SELECT * from materia `Dias`

UPDATE estudiante
SET Correo_electronico = 'florenciamendoza@gmail.com'
WHERE Nombre_Apellido = 'Florencia Mendoza';

INSERT INTO estudiante (Nombre_Apellido, Fecha_nacimiento, Edad, Correo_electronico, Telefono)
VALUES ('Ignacio Lopez', '2002-04-18', 22, 'iglopez@gmail.com', '5551234567');


select * from curso `Nombre_Curso`

DELETE FROM curso
WHERE `Nombre_Curso` = "Analisis Matematico";



#Consulta Inner Join
SELECT *
FROM materia A
INNER JOIN profesor B
ON A.`ID_Profesor` = `B`.`ID_Profesor`


#Consulta Left Join
SELECT *
FROM inscripcion C
LEFT JOIN estudiante D
ON C.`ID_Estudiante` = D.`ID_Estudiante`


#Consulta Right Join
SELECT *
FROM curso_profesor E
RIGHT JOIN profesor B
ON E.`ID_Profesor` = B.`ID_Profesor`


#Consulta Full Join
#No me dejaba usar "Full Outer Join" ni "Full Join"
SELECT *
FROM usuario F
LEFT JOIN usuario_logueado G ON F.id_usuario = G.id_usuario
UNION
SELECT *
FROM usuario F
RIGHT JOIN usuario_logueado G ON F.id_usuario = G.id_usuario;

