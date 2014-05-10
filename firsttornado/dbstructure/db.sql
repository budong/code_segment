-- MySQL dump 10.13  Distrib 5.6.16, for osx10.7 (x86_64)
--
-- Host: localhost    Database: cdndb_1
-- ------------------------------------------------------
-- Server version	5.6.16

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `CDN_idc`
--

DROP TABLE IF EXISTS `CDN_idc`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `CDN_idc` (
  `idc_id` int(11) NOT NULL AUTO_INCREMENT,
  `idc_name` varchar(64) NOT NULL DEFAULT '-',
  `max_bandwidth` int(11) NOT NULL DEFAULT '0',
  `domain` varchar(128) NOT NULL DEFAULT '-',
  PRIMARY KEY (`idc_id`),
  UNIQUE KEY `idc_name_unique` (`idc_name`)
) ENGINE=InnoDB AUTO_INCREMENT=87 DEFAULT CHARSET=utf8 COMMENT='idc信息表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `CDN_machine`
--

DROP TABLE IF EXISTS `CDN_machine`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `CDN_machine` (
  `machine_id` int(11) NOT NULL AUTO_INCREMENT,
  `idc_id` int(11) NOT NULL DEFAULT '0' COMMENT '所属idc的id',
  `host` varchar(32) NOT NULL DEFAULT '0.0.0.0' COMMENT '公网ip',
  `total_disk` bigint(20) NOT NULL DEFAULT '0' COMMENT '总磁盘量',
  `use_disk` bigint(20) NOT NULL DEFAULT '0' COMMENT '已使用磁盘量',
  `save_disk` bigint(20) NOT NULL DEFAULT '0' COMMENT '固化磁盘使用量',
  `max_bandwidth` bigint(20) NOT NULL DEFAULT '0',
  `use_bandwidth` bigint(20) NOT NULL DEFAULT '0',
  PRIMARY KEY (`machine_id`),
  UNIQUE KEY `host_unique` (`host`)
) ENGINE=InnoDB AUTO_INCREMENT=384 DEFAULT CHARSET=utf8 COMMENT='边缘节点机器信息表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `CDN_region`
--

DROP TABLE IF EXISTS `CDN_region`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `CDN_region` (
  `region_id` int(11) NOT NULL,
  `region_name` varchar(64) NOT NULL,
  PRIMARY KEY (`region_id`),
  UNIQUE KEY `region_name_unique` (`region_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='地区名称对应表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `CDN_sp`
--

DROP TABLE IF EXISTS `CDN_sp`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `CDN_sp` (
  `sp_id` int(11) NOT NULL,
  `sp_name` varchar(64) NOT NULL,
  PRIMARY KEY (`sp_id`),
  UNIQUE KEY `sp_name_unique` (`sp_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='运营商名称对应表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `CDN_strategy`
--

DROP TABLE IF EXISTS `CDN_strategy`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `CDN_strategy` (
  `sp` int(11) NOT NULL DEFAULT '0',
  `region` int(11) NOT NULL DEFAULT '0',
  `idc_list` varchar(1024) NOT NULL DEFAULT '-' COMMENT 'idc id，用逗号分隔',
  `weight` varchar(1024) NOT NULL DEFAULT '-',
  PRIMARY KEY (`sp`,`region`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='cdn调度策略表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `CDN_users`
--

DROP TABLE IF EXISTS `CDN_users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `CDN_users` (
  `id` mediumint(8) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `password` char(32) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2014-05-10 16:31:33
