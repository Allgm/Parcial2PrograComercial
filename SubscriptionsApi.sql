-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               8.0.30 - MySQL Community Server - GPL
-- Server OS:                    Win64
-- HeidiSQL Version:             12.1.0.6537
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dumping database structure for parcial2
CREATE DATABASE IF NOT EXISTS `parcial2` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `parcial2`;

-- Dumping structure for table parcial2.subscriptions
CREATE TABLE IF NOT EXISTS `subscriptions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `topic` varchar(100) NOT NULL,
  `email` varchar(100) DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `subscription_date` date NOT NULL,
  `active` varchar(50) NOT NULL,
  `notification_type` varchar(100) NOT NULL,
  `additional_info` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table parcial2.subscriptions: ~0 rows (approximately)
INSERT INTO `subscriptions` (`id`, `user_id`, `topic`, `email`, `phone`, `subscription_date`, `active`, `notification_type`, `additional_info`) VALUES
	(2, 1, 'test_topic', 'user@example.com', '1234567890', '2024-09-27', 'inactive', 'email', 'some_info'),
	(3, 1, 'test_topic', 'user@example.com', '1234567890', '2024-09-27', 'active', 'email', 'some_info'),
	(4, 1, 'test_topic', 'user@example.com', '1234567890', '2024-09-27', 'active', 'email', 'some_info'),
	(5, 1, 'test_topic', 'user@example.com', '1234567890', '2024-09-27', 'active', 'email', 'some_info'),
	(6, 1, 'test_topic', 'user@example.com', '1234567890', '2024-09-27', 'active', 'email', 'some_info'),
	(7, 1, 'test_topic', 'user@example.com', '1234567890', '2024-09-27', 'active', 'email', 'some_info'),
	(8, 1, 'test_topic', 'user@example.com', '1234567890', '2024-09-27', 'active', 'email', 'some_info');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
