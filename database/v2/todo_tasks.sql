CREATE DATABASE  IF NOT EXISTS `todo` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `todo`;
-- MySQL dump 10.13  Distrib 8.0.24, for Win64 (x86_64)
--
-- Host: localhost    Database: todo
-- ------------------------------------------------------
-- Server version	8.0.24

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
-- Table structure for table `tasks`
--

DROP TABLE IF EXISTS `tasks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tasks` (
  `taskId` int NOT NULL AUTO_INCREMENT,
  `taskDescription` varchar(100) DEFAULT NULL,
  `taskTypeId` int DEFAULT NULL,
  `creationDate` timestamp NOT NULL,
  `updatedTime` timestamp NOT NULL,
  `statusId` int DEFAULT NULL,
  `priorityId` int DEFAULT NULL,
  `tagId` int DEFAULT NULL,
  PRIMARY KEY (`taskId`),
  KEY `taskTypeId_idx` (`taskTypeId`),
  KEY `statusId_idx` (`statusId`),
  KEY `priorityId_idx` (`priorityId`),
  KEY `tagId_idx` (`tagId`),
  CONSTRAINT `priorityId` FOREIGN KEY (`priorityId`) REFERENCES `prioritytypes` (`priorityId`),
  CONSTRAINT `statusId` FOREIGN KEY (`statusId`) REFERENCES `statustypes` (`statusId`),
  CONSTRAINT `tagId` FOREIGN KEY (`tagId`) REFERENCES `tags` (`tagId`),
  CONSTRAINT `taskTypeId` FOREIGN KEY (`taskTypeId`) REFERENCES `tasktypes` (`typeId`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tasks`
--

LOCK TABLES `tasks` WRITE;
/*!40000 ALTER TABLE `tasks` DISABLE KEYS */;
INSERT INTO `tasks` VALUES (1,'Test edit',1,'2021-05-23 06:00:00','2021-05-23 06:00:00',1,1,1),(6,'Test',1,'2021-05-23 06:00:00','2021-05-23 06:00:00',1,1,1),(11,'Test2',1,'2021-05-23 06:00:00','2021-05-23 06:00:00',1,1,1),(15,'Test2',1,'2021-05-23 06:00:00','2021-05-23 06:00:00',1,1,1),(16,'Test2',1,'2021-05-23 06:00:00','2021-05-23 06:00:00',1,1,1),(17,'Test1000',1,'2021-05-26 01:22:12','2021-05-26 01:22:12',1,1,1);
/*!40000 ALTER TABLE `tasks` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-05-25 21:55:25
