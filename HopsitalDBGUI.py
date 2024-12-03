import tkinter as tk
from tkinter import ttk


class HospitalDBGUI:
    def __init__(self, root):
        # Initialize the main window
        self.root = root
        self.root.title("Hospital Management System")

        # Create tabs for different entities
        self.create_tabs()

    def create_tabs(self):
        """Create tabs for different entities like Patient, Doctor, etc."""
        tab_control = ttk.Notebook(self.root)

        # Patient Tab
        self.patient_tab = ttk.Frame(tab_control)
        tab_control.add(self.patient_tab, text="Patient")
        self.create_patient_form()

        # Doctor Tab
        self.doctor_tab = ttk.Frame(tab_control)
        tab_control.add(self.doctor_tab, text="Doctor")
        self.create_doctor_form()

        # Appointment Tab
        self.appointment_tab = ttk.Frame(tab_control)
        tab_control.add(self.appointment_tab, text="Appointment")
        self.create_appointment_form()

        # Pharmacy Tab
        self.pharmacy_tab = ttk.Frame(tab_control)
        tab_control.add(self.pharmacy_tab, text="Pharmacy")
        self.create_pharmacy_form()

        # Display tabs
        tab_control.pack(expand=1, fill="both")

    def create_patient_form(self):
        """Create form fields for Patient entity."""
        fields = ["ID", "Name", "DOB", "Emergency Phone", "Address", "Allergy"]
        self.create_form(self.patient_tab, fields)

    def create_doctor_form(self):
        """Create form fields for Doctor entity."""
        fields = ["ID", "Name", "DOB", "Email", "Specialty", "Department"]
        self.create_form(self.doctor_tab, fields)

    def create_appointment_form(self):
        """Create form fields for Appointment entity."""
        fields = ["ID", "Patient ID", "Doctor ID", "Date", "Time", "Room"]
        self.create_form(self.appointment_tab, fields)

    def create_pharmacy_form(self):
        """Create form fields for Pharmacy entity."""
        fields = ["Pharmacy ID", "Name", "Address", "Phone", "Medication Name", "Dose"]
        self.create_form(self.pharmacy_tab, fields)

    def create_form(self, tab, fields):
        """Generic method to create form fields in a tab."""
        for i, field in enumerate(fields):
            # Create and place labels and entry boxes
            label = ttk.Label(tab, text=field)
            label.grid(row=i, column=0, padx=10, pady=5, sticky="w")
            entry = ttk.Entry(tab)
            entry.grid(row=i, column=1, padx=10, pady=5)

        # Add a Submit button at the bottom
        submit_button = ttk.Button(tab, text="Submit", command=self.submit_data)
        submit_button.grid(row=len(fields), column=0, columnspan=2, pady=10)

    def submit_data(self):
        """Placeholder method for Submit button."""
        print("Data submitted. Connect this to a database later.")


if __name__ == "__main__":
    print("Starting the Hospital Management System GUI...")
    root = tk.Tk()
    app = HospitalDBGUI(root)
    root.mainloop()
