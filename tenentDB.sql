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
-- Ex. Inserting a user with a lease file
    --INSERT INTO Users (Name, DoB, Address, AptUnit, StateID, LeaseFile, RegistrationDate)
    --VALUES ('John Doe', '1990-05-15', '123 Main St', 'Apt 101', '654M920', FILE_READ(“mylease.pdf”), '2024-03-30');
--Ex. Inserting a prompt with all options and result IDs
    --INSERT INTO Prompts (PromptName, Description, Option1, Option2, Option3, Option4, ResultID1, ResultID2, ResultID3, ResultID4)
    --VALUES ('Favorite Color', 'What is your favorite color?', 'Red', 'Blue', 'Green', 'Other', 1, 2, 3, 4);
--Ex. Inserting a prompt with fewer options and result IDs
   --INSERT INTO Prompts (PromptName, Description, Option1, Option2, ResultID1, ResultID2)
   --VALUES ('Preferred Music Genre', 'What is your preferred music genre?', 'Rock', 'Pop', 1, 2);


