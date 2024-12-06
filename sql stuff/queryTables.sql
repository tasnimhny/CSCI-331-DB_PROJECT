-- Retrieve Patients
SELECT P.Name AS PatientName, D.Name AS DoctorName
FROM Patient P
JOIN Appointment A ON P.ID = A.Patient_ID
JOIN Doctor D ON A.Doctor_ID = D.ID
WHERE D.Name = 'Dr. Alice Smith';

-- List Appointment by Data
SELECT *
FROM Appointment
WHERE Date = '2024-12-10';

-- Get Medications for Appointment
SELECT M.Name, M.Dose, M.Cost
FROM Prescribed P
JOIN Medication M ON P.Medication_ID = M.ID
WHERE P.Appointment_ID = 401;

-- Generate bill
SELECT P.Name AS PatientName, A.Date, B.Service_Cost
FROM Bill B
JOIN Appointment A ON B.Appointment_ID = A.ID
JOIN Patient P ON A.Patient_ID = P.ID
WHERE P.ID = 101;

-- Assign Doctor to dept
INSERT INTO Belongs_To (Department_ID, Doctor_ID)
VALUES (301, 201);

-- Find doctor in specific dept
SELECT D.Name AS DoctorName, Dept.Name AS DepartmentName
FROM Belongs_To B
JOIN Doctor D ON B.Doctor_ID = D.ID
JOIN Department Dept ON B.Department_ID = Dept.ID
WHERE Dept.Name = 'Cardiology Department';
