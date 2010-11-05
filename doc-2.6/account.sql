-- phpMyAdmin SQL Dump
-- version 2.9.0-rc1
-- http://www.phpmyadmin.net
-- 
-- Host: localhost
-- Generation Time: Jun 05, 2008 at 10:42 PM
-- Server version: 5.0.45
-- PHP Version: 5.2.4
-- 
-- Database: `blend_site`
-- 

-- --------------------------------------------------------

-- 
-- Table structure for table `accounts`
-- 

CREATE TABLE `accounts` (
  `account_id` int(12) unsigned NOT NULL auto_increment,
  `account_time` date NOT NULL,
  `account_activate_time` date NOT NULL,
  `account_enabled` tinyint(4) NOT NULL,
  `account_activated` tinyint(4) NOT NULL,
  `account_account_type` int(12) NOT NULL,
  `account_fname` varchar(85) NOT NULL,
  `account_lname` varchar(85) NOT NULL,
  `account_email` varchar(85) NOT NULL,
  `account_phone` varchar(125) NOT NULL,
  `account_address` varchar(255) NOT NULL,
  `account_city` varchar(85) NOT NULL,
  `account_state` varchar(85) NOT NULL,
  `account_zip` varchar(85) NOT NULL,
  `name` varchar(85) NOT NULL,
  `password` varchar(85) NOT NULL,
  PRIMARY KEY  (`account_id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=590 ;

###
Dependent user management files:
getUserDetails
getUserDetails_sql
CookieCrumbler (Standalone)
