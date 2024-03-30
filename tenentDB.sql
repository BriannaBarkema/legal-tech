-- Create the TenentDB database if it does not exist
CREATE DATABASE IF NOT EXISTS TenentDB;

-- Use the TenentDB database
USE TenentDB;

-- Create a table called 'Users' to store user information
CREATE TABLE IF NOT EXISTS Users (
    UserID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(100) NOT NULL,
    DoB VARCHAR(100) NOT NULL,
	Address VARCHAR(100) NOT NULL,
	AptUnit VARCHAR(100) NOT NULL,
    StateID VARCHAR(100) NOT NULL,
	LeaseFile BLOB NOT NULL,
    RegistrationDate DATE
);

-- Create a table called 'Prompts' to store product information
CREATE TABLE IF NOT EXISTS Prompts (
    PromptID INT PRIMARY KEY AUTO_INCREMENT,
    PromptName VARCHAR(100) NOT NULL,
    Description TEXT NOT NULL,
	Option1 VARCHAR(100) NOT NULL,
	Option2 VARCHAR(100),
	Option3 VARCHAR(100),
	Option4 VARCHAR(100),
	ResultID1 INT,
	ResultID2 INT,
	ResultID3 INT,
	ResultID4 INT
);