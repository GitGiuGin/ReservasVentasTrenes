-- Active: 1717107082209@@127.0.0.1@3306@reservas_trenes
-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: localhost    Database: reservas_trenes
-- ------------------------------------------------------
-- Server version	5.5.5-10.4.32-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `reservas_trenes`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `reservas_trenes` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_bin */;

USE `reservas_trenes`;

--
-- Table structure for table `asiento`
--

DROP TABLE IF EXISTS `asiento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `asiento` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `numero_asiento` varchar(20) NOT NULL,
  `estado` tinyint(1) NOT NULL,
  `reserva_id` bigint(20) DEFAULT NULL,
  `ruta_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `asiento_reserva_id_c0130c2d_fk_reserva_id` (`reserva_id`),
  KEY `asiento_ruta_id_a0b7b05b_fk_ruta_id` (`ruta_id`),
  CONSTRAINT `asiento_reserva_id_c0130c2d_fk_reserva_id` FOREIGN KEY (`reserva_id`) REFERENCES `reserva` (`id`),
  CONSTRAINT `asiento_ruta_id_a0b7b05b_fk_ruta_id` FOREIGN KEY (`ruta_id`) REFERENCES `ruta` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=121 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `asiento`
--

LOCK TABLES `asiento` WRITE;
/*!40000 ALTER TABLE `asiento` DISABLE KEYS */;
INSERT INTO `asiento` VALUES (1,'1A',1,NULL,1),(2,'1B',1,NULL,1),(3,'1C',1,NULL,1),(4,'1D',1,NULL,1),(5,'2A',1,NULL,1),(6,'2B',1,NULL,1),(7,'2C',1,NULL,1),(8,'2D',1,NULL,1),(9,'3A',1,NULL,1),(10,'3B',1,NULL,1),(11,'3C',1,NULL,1),(12,'3D',1,NULL,1),(13,'4A',1,NULL,1),(14,'4B',1,NULL,1),(15,'4C',1,NULL,1),(16,'4D',1,NULL,1),(17,'5A',1,NULL,1),(18,'5B',1,NULL,1),(19,'5C',1,NULL,1),(20,'5D',1,NULL,1),(21,'1A',1,NULL,2),(22,'1B',1,NULL,2),(23,'1C',1,NULL,2),(24,'1D',1,NULL,2),(25,'2A',1,NULL,2),(26,'2B',1,NULL,2),(27,'2C',1,NULL,2),(28,'2D',1,NULL,2),(29,'3A',1,NULL,2),(30,'3B',1,NULL,2),(31,'3C',1,NULL,2),(32,'3D',1,NULL,2),(33,'4A',1,NULL,2),(34,'4B',1,NULL,2),(35,'4C',1,NULL,2),(36,'4D',1,NULL,2),(37,'5A',1,NULL,2),(38,'5B',1,NULL,2),(39,'5C',1,NULL,2),(40,'5D',1,NULL,2),(41,'1A',1,NULL,3),(42,'1B',1,NULL,3),(43,'1C',1,NULL,3),(44,'1D',1,NULL,3),(45,'2A',1,NULL,3),(46,'2B',1,NULL,3),(47,'2C',1,NULL,3),(48,'2D',1,NULL,3),(49,'3A',1,NULL,3),(50,'3B',1,NULL,3),(51,'3C',1,NULL,3),(52,'3D',1,NULL,3),(53,'4A',1,NULL,3),(54,'4B',1,NULL,3),(55,'4C',1,NULL,3),(56,'4D',1,NULL,3),(57,'5A',1,NULL,3),(58,'5B',1,NULL,3),(59,'5C',1,NULL,3),(60,'5D',1,NULL,3),(61,'1A',1,NULL,4),(62,'1B',1,NULL,4),(63,'1C',1,NULL,4),(64,'1D',1,NULL,4),(65,'2A',1,NULL,4),(66,'2B',1,NULL,4),(67,'2C',1,NULL,4),(68,'2D',1,NULL,4),(69,'3A',1,NULL,4),(70,'3B',1,NULL,4),(71,'3C',1,NULL,4),(72,'3D',1,NULL,4),(73,'4A',1,NULL,4),(74,'4B',1,NULL,4),(75,'4C',1,NULL,4),(76,'4D',1,NULL,4),(77,'5A',1,NULL,4),(78,'5B',1,NULL,4),(79,'5C',1,NULL,4),(80,'5D',1,NULL,4),(81,'1A',1,NULL,5),(82,'1B',1,NULL,5),(83,'1C',1,NULL,5),(84,'1D',1,NULL,5),(85,'2A',1,NULL,5),(86,'2B',1,NULL,5),(87,'2C',1,NULL,5),(88,'2D',1,NULL,5),(89,'3A',1,NULL,5),(90,'3B',1,NULL,5),(91,'3C',1,NULL,5),(92,'3D',1,NULL,5),(93,'4A',1,NULL,5),(94,'4B',1,NULL,5),(95,'4C',1,NULL,5),(96,'4D',1,NULL,5),(97,'5A',1,NULL,5),(98,'5B',1,NULL,5),(99,'5C',1,NULL,5),(100,'5D',1,NULL,5),(101,'1A',1,NULL,6),(102,'1B',1,NULL,6),(103,'1C',1,NULL,6),(104,'1D',1,NULL,6),(105,'2A',1,NULL,6),(106,'2B',1,NULL,6),(107,'2C',1,NULL,6),(108,'2D',1,NULL,6),(109,'3A',1,NULL,6),(110,'3B',1,NULL,6),(111,'3C',1,NULL,6),(112,'3D',1,NULL,6),(113,'4A',1,NULL,6),(114,'4B',1,NULL,6),(115,'4C',1,NULL,6),(116,'4D',1,NULL,6),(117,'5A',1,NULL,6),(118,'5B',1,NULL,6),(119,'5C',1,NULL,6),(120,'5D',1,NULL,6);
/*!40000 ALTER TABLE `asiento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add Asiento',7,'add_asiento'),(26,'Can change Asiento',7,'change_asiento'),(27,'Can delete Asiento',7,'delete_asiento'),(28,'Can view Asiento',7,'view_asiento'),(29,'Can add Cliente',8,'add_cliente'),(30,'Can change Cliente',8,'change_cliente'),(31,'Can delete Cliente',8,'delete_cliente'),(32,'Can view Cliente',8,'view_cliente'),(33,'Can add Reserva',9,'add_reserva'),(34,'Can change Reserva',9,'change_reserva'),(35,'Can delete Reserva',9,'delete_reserva'),(36,'Can view Reserva',9,'view_reserva'),(37,'Can add Ruta',10,'add_ruta'),(38,'Can change Ruta',10,'change_ruta'),(39,'Can delete Ruta',10,'delete_ruta'),(40,'Can view Ruta',10,'view_ruta'),(41,'Can add Tren',11,'add_tren'),(42,'Can change Tren',11,'change_tren'),(43,'Can delete Tren',11,'delete_tren'),(44,'Can view Tren',11,'view_tren');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cliente`
--

DROP TABLE IF EXISTS `cliente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cliente` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `nombres` varchar(50) NOT NULL,
  `apellido_paterno` varchar(50) NOT NULL,
  `apellido_materno` varchar(50) NOT NULL,
  `correo` varchar(128) NOT NULL,
  `telefono` varchar(15) NOT NULL,
  `direccion` varchar(255) NOT NULL,
  `contraseña` varchar(128) NOT NULL,
  `estado` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cliente`
--

LOCK TABLES `cliente` WRITE;
/*!40000 ALTER TABLE `cliente` DISABLE KEYS */;
INSERT INTO `cliente` VALUES (1,'Edith Monica','Espejo','Ayme','emeespejo@gmail.com','77204380','Catayud Y Uyustus','Valentina29*',1);
/*!40000 ALTER TABLE `cliente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `column_statistics`
--

DROP TABLE IF EXISTS `column_statistics`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `column_statistics` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre_tabla` varchar(255) NOT NULL,
  `nombre_columna` varchar(255) NOT NULL,
  `tipo_dato` varchar(100) DEFAULT NULL,
  `conteo_nulos` int(11) DEFAULT 0,
  `conteo_distintos` int(11) DEFAULT 0,
  `valor_maximo` varchar(255) DEFAULT NULL,
  `valor_minimo` varchar(255) DEFAULT NULL,
  `valor_promedio` decimal(18,2) DEFAULT NULL,
  `desviacion_estandar` decimal(18,2) DEFAULT NULL,
  `ultima_actualizacion` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `column_statistics`
--

LOCK TABLES `column_statistics` WRITE;
/*!40000 ALTER TABLE `column_statistics` DISABLE KEYS */;
/*!40000 ALTER TABLE `column_statistics` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(7,'asientos','asiento'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(8,'clientes','cliente'),(5,'contenttypes','contenttype'),(9,'reservas','reserva'),(10,'rutas','ruta'),(6,'sessions','session'),(11,'trenes','tren');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2024-09-20 17:54:33.700006'),(2,'auth','0001_initial','2024-09-20 17:54:34.147488'),(3,'admin','0001_initial','2024-09-20 17:54:34.286547'),(4,'admin','0002_logentry_remove_auto_add','2024-09-20 17:54:34.296477'),(5,'admin','0003_logentry_add_action_flag_choices','2024-09-20 17:54:34.309539'),(6,'trenes','0001_initial','2024-09-20 17:54:34.329073'),(7,'rutas','0001_initial','2024-09-20 17:54:34.435342'),(8,'clientes','0001_initial','2024-09-20 17:54:34.465945'),(9,'reservas','0001_initial','2024-09-20 17:54:34.566560'),(10,'asientos','0001_initial','2024-09-20 17:54:34.673063'),(11,'contenttypes','0002_remove_content_type_name','2024-09-20 17:54:34.756760'),(12,'auth','0002_alter_permission_name_max_length','2024-09-20 17:54:34.820331'),(13,'auth','0003_alter_user_email_max_length','2024-09-20 17:54:34.879151'),(14,'auth','0004_alter_user_username_opts','2024-09-20 17:54:34.892143'),(15,'auth','0005_alter_user_last_login_null','2024-09-20 17:54:34.943522'),(16,'auth','0006_require_contenttypes_0002','2024-09-20 17:54:34.953099'),(17,'auth','0007_alter_validators_add_error_messages','2024-09-20 17:54:34.965667'),(18,'auth','0008_alter_user_username_max_length','2024-09-20 17:54:34.987078'),(19,'auth','0009_alter_user_last_name_max_length','2024-09-20 17:54:35.004098'),(20,'auth','0010_alter_group_name_max_length','2024-09-20 17:54:35.065072'),(21,'auth','0011_update_proxy_permissions','2024-09-20 17:54:35.087683'),(22,'auth','0012_alter_user_first_name_max_length','2024-09-20 17:54:35.110649'),(23,'sessions','0001_initial','2024-09-20 17:54:35.163318');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reserva`
--

DROP TABLE IF EXISTS `reserva`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reserva` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `fecha_reserva` date NOT NULL,
  `estado` tinyint(1) NOT NULL,
  `cliente_id` bigint(20) DEFAULT NULL,
  `tren_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `reserva_cliente_id_b1289b29_fk_cliente_id` (`cliente_id`),
  KEY `reserva_tren_id_4a29075c_fk_tren_id` (`tren_id`),
  CONSTRAINT `reserva_cliente_id_b1289b29_fk_cliente_id` FOREIGN KEY (`cliente_id`) REFERENCES `cliente` (`id`),
  CONSTRAINT `reserva_tren_id_4a29075c_fk_tren_id` FOREIGN KEY (`tren_id`) REFERENCES `tren` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reserva`
--

LOCK TABLES `reserva` WRITE;
/*!40000 ALTER TABLE `reserva` DISABLE KEYS */;
/*!40000 ALTER TABLE `reserva` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ruta`
--

DROP TABLE IF EXISTS `ruta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ruta` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `origen` varchar(50) NOT NULL,
  `destino` varchar(50) NOT NULL,
  `duracion` smallint(6) NOT NULL,
  `dia_salida` varchar(50) DEFAULT NULL,
  `horario_salida` time(6) DEFAULT NULL,
  `dia_retorno` varchar(50) DEFAULT NULL,
  `horario_retorno` time(6) DEFAULT NULL,
  `precio` decimal(10,2) NOT NULL,
  `tren_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ruta_tren_id_510b6cc8_fk_tren_id` (`tren_id`),
  CONSTRAINT `ruta_tren_id_510b6cc8_fk_tren_id` FOREIGN KEY (`tren_id`) REFERENCES `tren` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ruta`
--

LOCK TABLES `ruta` WRITE;
/*!40000 ALTER TABLE `ruta` DISABLE KEYS */;
INSERT INTO `ruta` VALUES (1,'La Paz','Cochabamba',245,'Lunes','09:00:00.000000',NULL,NULL,80.00,1),(2,'Cochabamba','La Paz',245,NULL,NULL,'Miércoles','13:50:00.000000',80.00,1),(3,'La Paz','Potosi',540,'Martes','10:00:00.000000',NULL,NULL,120.00,2),(4,'Potosi','La Paz',540,NULL,NULL,'Jueves','15:00:00.000000',120.00,2),(5,'La Paz','Chuquisaca',660,'Miércoles','08:00:00.000000',NULL,NULL,86.00,3),(6,'Chuquisaca','La Paz',660,NULL,NULL,'Sábado','13:00:00.000000',86.00,3);
/*!40000 ALTER TABLE `ruta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tren`
--

DROP TABLE IF EXISTS `tren`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tren` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `capacidad` smallint(6) NOT NULL,
  `estado` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tren`
--

LOCK TABLES `tren` WRITE;
/*!40000 ALTER TABLE `tren` DISABLE KEYS */;
INSERT INTO `tren` VALUES (1,'Metropolitano Cochabamba',20,1),(2,'Expreso Del Sur',20,1),(3,'Ferroviaria Oriental',20,0);
/*!40000 ALTER TABLE `tren` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-09-20 15:30:11
