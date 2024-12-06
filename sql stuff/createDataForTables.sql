-- Hospital
INSERT INTO Hospital (ID, Name, Phone, Address, Emergency_Phone)
VALUES (1, 'City Hospital', '123-456-7890', '123 Main St', '987-654-3210');

-- Patient
INSERT INTO Patient (ID, Name, DOB, Address, Medical_Records, Allergy)
VALUES (101, 'John Doe', '1985-07-15', '456 Elm St', 'Asthma History', 'Peanuts');

-- Staff and Doctor I think nurse
INSERT INTO Staff (ID, Name, DOB, Email, Address, Specialty)
VALUES (201, 'Dr. Alice Smith', '1970-05-10', 'alice.smith@hospital.com', '789 Oak St', 'Cardiology');

INSERT INTO Doctor (ID, Specialty)
VALUES (201, 'Cardiology');

-- Department
INSERT INTO Department (ID, Name, Address)
VALUES (301, 'Cardiology Department', 'Building A');

-- Appointment
INSERT INTO Appointment (ID, Patient_ID, Doctor_ID, Nurse_ID, Room_Code, Date, Time, Lab_Report)
VALUES (401, 101, 201, NULL, '101A', '2024-12-10', '10:30:00', 'Normal Results');
