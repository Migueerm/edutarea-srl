CREATE DATABASE  IF NOT EXISTS `edutareas` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `edutareas`;
-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: edutareas
-- ------------------------------------------------------
-- Server version	8.0.36

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `calendario`
--

DROP TABLE IF EXISTS `calendario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `calendario` (
  `ID_Calendario` int NOT NULL AUTO_INCREMENT,
  `Tipo` varchar(50) NOT NULL,
  `Fecha` date NOT NULL,
  `ID_Profesor` int NOT NULL,
  PRIMARY KEY (`ID_Calendario`),
  KEY `FK_Profesor_idx` (`ID_Profesor`),
  CONSTRAINT `FK_Id_Profesor` FOREIGN KEY (`ID_Profesor`) REFERENCES `profesor` (`ID_Profesor`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `calendario`
--

LOCK TABLES `calendario` WRITE;
/*!40000 ALTER TABLE `calendario` DISABLE KEYS */;
INSERT INTO `calendario` VALUES (1,'parcial de matematicas','2024-12-12',1),(2,'parcial sociales','2024-07-12',1);
/*!40000 ALTER TABLE `calendario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `compartir`
--

DROP TABLE IF EXISTS `compartir`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `compartir` (
  `ID_Compartir` int NOT NULL,
  `Compartir` text NOT NULL,
  `ID_Tareas` int NOT NULL,
  PRIMARY KEY (`ID_Compartir`),
  KEY `FK_Tareas_idx` (`ID_Tareas`),
  CONSTRAINT `FK_Id_Tareas` FOREIGN KEY (`ID_Tareas`) REFERENCES `tarea` (`ID_Tarea`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `compartir`
--

LOCK TABLES `compartir` WRITE;
/*!40000 ALTER TABLE `compartir` DISABLE KEYS */;
/*!40000 ALTER TABLE `compartir` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `curso`
--

DROP TABLE IF EXISTS `curso`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `curso` (
  `ID_Curso` int NOT NULL AUTO_INCREMENT,
  `Nombre_Curso` varchar(100) NOT NULL,
  `Descripcion_Curso` text NOT NULL,
  PRIMARY KEY (`ID_Curso`)
) ENGINE=InnoDB AUTO_INCREMENT=13214 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `curso`
--

LOCK TABLES `curso` WRITE;
/*!40000 ALTER TABLE `curso` DISABLE KEYS */;
INSERT INTO `curso` VALUES (1,'Analisis Matematico','Curso ciencia basicas'),(2,'Programación Inicial','Curso de programacion'),(3,'Gestion de negocios','admistracion');
/*!40000 ALTER TABLE `curso` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `curso_evento`
--

DROP TABLE IF EXISTS `curso_evento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `curso_evento` (
  `ID_Curso` int NOT NULL,
  `ID_Evento` int NOT NULL,
  PRIMARY KEY (`ID_Curso`,`ID_Evento`),
  KEY `FK_Id_Evento_cm_idx` (`ID_Evento`),
  CONSTRAINT `FK_Id_Curso_cmnew` FOREIGN KEY (`ID_Curso`) REFERENCES `curso` (`ID_Curso`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `FK_Id_Evento_cm` FOREIGN KEY (`ID_Evento`) REFERENCES `evento` (`ID_Evento`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `curso_evento`
--

LOCK TABLES `curso_evento` WRITE;
/*!40000 ALTER TABLE `curso_evento` DISABLE KEYS */;
/*!40000 ALTER TABLE `curso_evento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `curso_materia`
--

DROP TABLE IF EXISTS `curso_materia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `curso_materia` (
  `ID_Materia` int NOT NULL,
  `ID_Curso` int NOT NULL,
  PRIMARY KEY (`ID_Materia`,`ID_Curso`),
  KEY `FK_Id_Curso_idx` (`ID_Curso`),
  CONSTRAINT `FK_Id_Curso_cm` FOREIGN KEY (`ID_Curso`) REFERENCES `curso` (`ID_Curso`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `FK_Id_Materia_cm` FOREIGN KEY (`ID_Materia`) REFERENCES `materia` (`ID_Materia`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `curso_materia`
--

LOCK TABLES `curso_materia` WRITE;
/*!40000 ALTER TABLE `curso_materia` DISABLE KEYS */;
/*!40000 ALTER TABLE `curso_materia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `curso_profesor`
--

DROP TABLE IF EXISTS `curso_profesor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `curso_profesor` (
  `ID_Profesor` int NOT NULL,
  `ID_Curso` int NOT NULL,
  `Año_Academico` year NOT NULL,
  `Semestre` varchar(10) NOT NULL,
  PRIMARY KEY (`ID_Profesor`,`ID_Curso`),
  KEY `FK_Id_Curso_new_idx` (`ID_Curso`),
  CONSTRAINT `FK_Id_Curso_new` FOREIGN KEY (`ID_Curso`) REFERENCES `curso` (`ID_Curso`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `FK_Id_Profesor_new` FOREIGN KEY (`ID_Profesor`) REFERENCES `profesor` (`ID_Profesor`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `curso_profesor`
--

LOCK TABLES `curso_profesor` WRITE;
/*!40000 ALTER TABLE `curso_profesor` DISABLE KEYS */;
INSERT INTO `curso_profesor` VALUES (1,2,2024,'1'),(2,1,2002,'1');
/*!40000 ALTER TABLE `curso_profesor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `estudiante`
--

DROP TABLE IF EXISTS `estudiante`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `estudiante` (
  `ID_Estudiante` int NOT NULL AUTO_INCREMENT,
  `Nombre_Apellido` varchar(50) NOT NULL,
  `Fecha_nacimiento` date DEFAULT NULL,
  `Edad` int NOT NULL,
  `Correo_electronico` varchar(100) NOT NULL,
  `Telefono` varchar(15) NOT NULL,
  PRIMARY KEY (`ID_Estudiante`),
  UNIQUE KEY `Nombre_Apellido_UNIQUE` (`Nombre_Apellido`)
) ENGINE=InnoDB AUTO_INCREMENT=1235 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `estudiante`
--

LOCK TABLES `estudiante` WRITE;
/*!40000 ALTER TABLE `estudiante` DISABLE KEYS */;
INSERT INTO `estudiante` VALUES (1,'Miguel Perez','1996-05-10',28,'mperez@gmail.com','153456723'),(2,'Florencia Mendoza','1990-09-12',33,'florenciam@gmail.com','152346576'),(3,'Carlota Olmedo','1998-07-12',26,'colmedo@gmail.com','154765856');
/*!40000 ALTER TABLE `estudiante` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `estudiante_compartir`
--

DROP TABLE IF EXISTS `estudiante_compartir`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `estudiante_compartir` (
  `ID_Estudiante` int NOT NULL,
  `ID_Compartir` int NOT NULL,
  PRIMARY KEY (`ID_Estudiante`,`ID_Compartir`),
  KEY `FK_Id_Compartir_newcm_idx` (`ID_Compartir`),
  CONSTRAINT `FK_Id_Compartir_newcm` FOREIGN KEY (`ID_Compartir`) REFERENCES `compartir` (`ID_Compartir`),
  CONSTRAINT `FK_Id_Estudiante_newcm` FOREIGN KEY (`ID_Estudiante`) REFERENCES `estudiante` (`ID_Estudiante`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `estudiante_compartir`
--

LOCK TABLES `estudiante_compartir` WRITE;
/*!40000 ALTER TABLE `estudiante_compartir` DISABLE KEYS */;
/*!40000 ALTER TABLE `estudiante_compartir` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `estudiante_tarea`
--

DROP TABLE IF EXISTS `estudiante_tarea`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `estudiante_tarea` (
  `ID_Estudiante` int NOT NULL,
  `ID_Tarea` int NOT NULL,
  PRIMARY KEY (`ID_Estudiante`,`ID_Tarea`),
  KEY `FK_Id_Tarea_new_idx` (`ID_Tarea`),
  CONSTRAINT `FK_Id_Estudiante_newcmnew` FOREIGN KEY (`ID_Estudiante`) REFERENCES `estudiante` (`ID_Estudiante`) ON DELETE CASCADE,
  CONSTRAINT `FK_Id_Tarea_newcmnew` FOREIGN KEY (`ID_Tarea`) REFERENCES `tarea` (`ID_Tarea`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `estudiante_tarea`
--

LOCK TABLES `estudiante_tarea` WRITE;
/*!40000 ALTER TABLE `estudiante_tarea` DISABLE KEYS */;
/*!40000 ALTER TABLE `estudiante_tarea` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `evento`
--

DROP TABLE IF EXISTS `evento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `evento` (
  `ID_Evento` int NOT NULL AUTO_INCREMENT,
  `Fecha` date NOT NULL,
  `ID_Calendario` int NOT NULL,
  PRIMARY KEY (`ID_Evento`),
  KEY `FK_Calendario_idx` (`ID_Calendario`),
  CONSTRAINT `FK_Id_Calendario` FOREIGN KEY (`ID_Calendario`) REFERENCES `calendario` (`ID_Calendario`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `evento`
--

LOCK TABLES `evento` WRITE;
/*!40000 ALTER TABLE `evento` DISABLE KEYS */;
INSERT INTO `evento` VALUES (1,'2024-10-12',1),(2,'2024-07-01',2);
/*!40000 ALTER TABLE `evento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `inscripcion`
--

DROP TABLE IF EXISTS `inscripcion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inscripcion` (
  `ID_Estudiante` int NOT NULL,
  `ID_Curso` int NOT NULL,
  `Fecha_Inscripcion` date NOT NULL,
  `Nota_Final` float NOT NULL,
  PRIMARY KEY (`ID_Estudiante`,`ID_Curso`),
  KEY `FK_Id_Curso_idx` (`ID_Curso`),
  CONSTRAINT `FK_Id_Curso` FOREIGN KEY (`ID_Curso`) REFERENCES `curso` (`ID_Curso`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `FK_Id_Estudiante` FOREIGN KEY (`ID_Estudiante`) REFERENCES `estudiante` (`ID_Estudiante`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inscripcion`
--

LOCK TABLES `inscripcion` WRITE;
/*!40000 ALTER TABLE `inscripcion` DISABLE KEYS */;
INSERT INTO `inscripcion` VALUES (2,2,'2024-06-29',7),(3,2,'2024-07-12',9);
/*!40000 ALTER TABLE `inscripcion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `materia`
--

DROP TABLE IF EXISTS `materia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `materia` (
  `ID_Materia` int NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(100) NOT NULL,
  `ID_Profesor` int NOT NULL,
  `Ubicacion` varchar(45) NOT NULL,
  `Horario` time NOT NULL,
  `Dias` varchar(12) NOT NULL,
  PRIMARY KEY (`ID_Materia`),
  KEY `FK_materia_profesor_idx` (`ID_Profesor`),
  CONSTRAINT `FK_Id_Profesor_new_cm` FOREIGN KEY (`ID_Profesor`) REFERENCES `profesor` (`ID_Profesor`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `materia`
--

LOCK TABLES `materia` WRITE;
/*!40000 ALTER TABLE `materia` DISABLE KEYS */;
INSERT INTO `materia` VALUES (1,'Humanidades',1,'C','00:00:10','lunes'),(2,'Comunicacion',2,'B','00:00:09','jueves'),(4,'Analisis matematico',1,'A','00:00:08','viernes');
/*!40000 ALTER TABLE `materia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `profesor`
--

DROP TABLE IF EXISTS `profesor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `profesor` (
  `ID_Profesor` int NOT NULL AUTO_INCREMENT,
  `Nombre_Apellido` varchar(100) NOT NULL,
  `Correo_electronico` varchar(50) NOT NULL,
  PRIMARY KEY (`ID_Profesor`),
  UNIQUE KEY `Correo_eléctronico_UNIQUE` (`Correo_electronico`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `profesor`
--

LOCK TABLES `profesor` WRITE;
/*!40000 ALTER TABLE `profesor` DISABLE KEYS */;
INSERT INTO `profesor` VALUES (1,'Mateo Caceres','materocaceres@gmail.com'),(2,'Micaela Peralta','mperalta@gmail.com'),(3,'Hugo Zanata','hugozanata@gmail.com');
/*!40000 ALTER TABLE `profesor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `recordatorio`
--

DROP TABLE IF EXISTS `recordatorio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `recordatorio` (
  `ID_Recordatorio` int NOT NULL AUTO_INCREMENT,
  `Mensaje` text NOT NULL,
  `Fecha` varchar(45) NOT NULL,
  `Hora` time NOT NULL,
  `Descripcion` text NOT NULL,
  `ID_Tarea` int NOT NULL,
  PRIMARY KEY (`ID_Recordatorio`),
  KEY `FK_Id_Tarea_idx` (`ID_Tarea`),
  CONSTRAINT `FK_Id_Tarea` FOREIGN KEY (`ID_Tarea`) REFERENCES `tarea` (`ID_Tarea`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recordatorio`
--

LOCK TABLES `recordatorio` WRITE;
/*!40000 ALTER TABLE `recordatorio` DISABLE KEYS */;
INSERT INTO `recordatorio` VALUES (1,'Hacer trabajo practico','2024-07-13','09:30:00','Hacer trabajo practico de analisis matematico',3),(2,'Estudiar para evaluacion matematica','2024-08-12','10:00:00','Estudiar modulos integrador',6);
/*!40000 ALTER TABLE `recordatorio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `recordatorio_evento`
--

DROP TABLE IF EXISTS `recordatorio_evento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `recordatorio_evento` (
  `ID_Evento` int NOT NULL,
  `ID_Recordatorio` int NOT NULL,
  PRIMARY KEY (`ID_Evento`,`ID_Recordatorio`),
  KEY `FK_Id_Recordatorio_newcm_idx` (`ID_Recordatorio`),
  CONSTRAINT `FK_Id_Evento_newcm` FOREIGN KEY (`ID_Evento`) REFERENCES `evento` (`ID_Evento`),
  CONSTRAINT `FK_Id_Recordatorio_newcm` FOREIGN KEY (`ID_Recordatorio`) REFERENCES `recordatorio` (`ID_Recordatorio`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recordatorio_evento`
--

LOCK TABLES `recordatorio_evento` WRITE;
/*!40000 ALTER TABLE `recordatorio_evento` DISABLE KEYS */;
/*!40000 ALTER TABLE `recordatorio_evento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tarea`
--

DROP TABLE IF EXISTS `tarea`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tarea` (
  `ID_Tarea` int NOT NULL AUTO_INCREMENT,
  `Titulo` varchar(100) NOT NULL,
  `Prioridad` varchar(10) NOT NULL,
  `Descripcion` text NOT NULL,
  `Fecha_Entrega` date NOT NULL,
  `Estado` varchar(20) NOT NULL,
  PRIMARY KEY (`ID_Tarea`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tarea`
--

LOCK TABLES `tarea` WRITE;
/*!40000 ALTER TABLE `tarea` DISABLE KEYS */;
INSERT INTO `tarea` VALUES (3,'Problematica matematica','Alta','Resolver ejercicios matematicos','2024-06-23','Inicio'),(5,'TP Humanidades','Alta','Hacer trabajo practico consigna a','2024-07-12','Inicio'),(6,'Estadistica','Medio','Hacer ejercicio del cuadernillo modular','2024-07-17','Bajo'),(7,'Tp Humanidades inicial','Medio','Hacer trabajo practico consigna a','2024-07-12','Intermedio');
/*!40000 ALTER TABLE `tarea` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tarea_materia`
--

DROP TABLE IF EXISTS `tarea_materia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tarea_materia` (
  `ID_Tarea` int NOT NULL,
  `ID_Materia` int NOT NULL,
  PRIMARY KEY (`ID_Tarea`,`ID_Materia`),
  KEY `FK_Id_Materia_idx` (`ID_Materia`),
  CONSTRAINT `FK_Id_Materia_new` FOREIGN KEY (`ID_Materia`) REFERENCES `materia` (`ID_Materia`),
  CONSTRAINT `FK_Id_Tarea_new` FOREIGN KEY (`ID_Tarea`) REFERENCES `tarea` (`ID_Tarea`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tarea_materia`
--

LOCK TABLES `tarea_materia` WRITE;
/*!40000 ALTER TABLE `tarea_materia` DISABLE KEYS */;
/*!40000 ALTER TABLE `tarea_materia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'edutareas'
--
/*!50003 DROP PROCEDURE IF EXISTS `ListAllTables` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `ListAllTables`()
BEGIN
    DECLARE done INT DEFAULT 0;
    DECLARE tbl_name VARCHAR(255);
    DECLARE cur CURSOR FOR SELECT table_name FROM information_schema.tables WHERE table_schema = DATABASE();
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

    OPEN cur;

    read_loop: LOOP
        FETCH cur INTO tbl_name;
        IF done THEN
            LEAVE read_loop;
        END IF;
        SET @s = CONCAT('SELECT * FROM ', tbl_name, ' LIMIT 1000;');
        PREPARE stmt FROM @s;
        EXECUTE stmt;
        DEALLOCATE PREPARE stmt;
    END LOOP;

    CLOSE cur;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-06-13 14:52:04
