-- Hospital Table
CREATE TABLE Hospital (
    ID INT PRIMARY KEY,
    Name VARCHAR(255),
    Phone VARCHAR(15),
    Address TEXT,
    Emergency_Phone VARCHAR(15)
);

-- Patient Table
CREATE TABLE Patient (
    ID INT PRIMARY KEY,
    Name VARCHAR(255),
    DOB DATE,
    Address TEXT,
    Medical_Records TEXT,
    Allergy TEXT
);

-- Staff Table 
CREATE TABLE Staff (
    ID INT PRIMARY KEY,
    Name VARCHAR(255),
    DOB DATE,
    Email VARCHAR(255),
    Address TEXT,
    Specialty VARCHAR(255) NULL
);

-- Nurse Table (Subtype)
CREATE TABLE Nurse (
    ID INT PRIMARY KEY REFERENCES Staff(ID)
);

-- Doctor Table (Subtype)
CREATE TABLE Doctor (
    ID INT PRIMARY KEY REFERENCES Staff(ID),
    Specialty VARCHAR(255)
);

-- Department Table
CREATE TABLE Department (
    ID INT PRIMARY KEY,
    Name VARCHAR(255),
    Address TEXT
);

-- Appointment Table
CREATE TABLE Appointment (
    ID INT PRIMARY KEY,
    Patient_ID INT REFERENCES Patient(ID),
    Doctor_ID INT REFERENCES Doctor(ID),
    Nurse_ID INT REFERENCES Nurse(ID),
    Room_Code VARCHAR(50),
    Date DATE,
    Time TIME,
    Lab_Report TEXT
);

-- Room Table
CREATE TABLE Room (
    Code VARCHAR(50) PRIMARY KEY,
    Name VARCHAR(255),
    Address TEXT
);

-- Medication Table
CREATE TABLE Medication (
    ID INT PRIMARY KEY,
    Name VARCHAR(255),
    Dose VARCHAR(50),
    Date DATE,
    Cost DECIMAL(10, 2)
);

-- Pharmacy Table
CREATE TABLE Pharmacy (
    ID INT PRIMARY KEY,
    Name VARCHAR(255),
    Address TEXT,
    Phone VARCHAR(15)
);

-- Bill Table
CREATE TABLE Bill (
    ID INT PRIMARY KEY,
    Appointment_ID INT REFERENCES Appointment(ID),
    Service_Cost DECIMAL(10, 2),
    Date DATE
);

-- Relationships Mapping
CREATE TABLE Prescribed (
    Appointment_ID INT REFERENCES Appointment(ID),
    Medication_ID INT REFERENCES Medication(ID),
    PRIMARY KEY (Appointment_ID, Medication_ID)
);

CREATE TABLE Belongs_To (
    Department_ID INT REFERENCES Department(ID),
    Doctor_ID INT REFERENCES Doctor(ID),
    PRIMARY KEY (Department_ID, Doctor_ID)
);
