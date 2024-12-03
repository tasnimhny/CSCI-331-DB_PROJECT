import tkinter as tk
from tkinter import ttk

class HospitalManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.create_tabs()

    def create_tabs(self):
        """Creates tabs for each entity in the ER diagram."""
        tab_control = ttk.Notebook(self.root)

        # Create tabs for entities
        self.create_tab(tab_control, "Employee", ["ID", "Name", "Phone"])
        self.create_tab(tab_control, "Staff", ["ID", "Name", "DOB", "Address"])
        self.create_tab(tab_control, "Department", ["ID", "Name", "Address"])
        self.create_tab(tab_control, "Doctor", ["ID", "Name", "DOB", "Email", "Specialty", "Department"])
        self.create_tab(tab_control, "Patient", ["ID", "Name", "DOB", "Address", "Emergency Phone", "Allergy"])
        self.create_tab(tab_control, "Appointment", ["ID", "Patient ID", "Doctor ID", "Date", "Time", "Room"])
        self.create_tab(tab_control, "Room", ["Room Code", "Name", "Address"])
        self.create_tab(tab_control, "Bill", ["ID", "Patient ID", "Service Cost", "Date"])
        self.create_tab(tab_control, "Medication", ["ID", "Name", "Dose", "Cost", "Pharmacy ID"])
        self.create_tab(tab_control, "Pharmacy", ["ID", "Name", "Address", "Phone"])

        # Pack all tabs
        tab_control.pack(expand=1, fill="both")

    def create_tab(self, tab_control, entity_name, fields):
        """Generic function to create a tab with form fields."""
        tab = ttk.Frame(tab_control)
        tab_control.add(tab, text=entity_name)
        self.create_form(tab, fields)

    def create_form(self, tab, fields):
        """Creates a form with labels and entry boxes based on fields."""
        for i, field in enumerate(fields):
            # Add label and entry for each field
            label = ttk.Label(tab, text=field)
            label.grid(row=i, column=0, padx=10, pady=5, sticky="w")
            entry = ttk.Entry(tab)
            entry.grid(row=i, column=1, padx=10, pady=5)

        # Add Submit button
        submit_button = ttk.Button(tab, text="Submit", command=self.submit_data)
        submit_button.grid(row=len(fields), column=0, columnspan=2, pady=10)

    def submit_data(self):
        """Placeholder for handling data submission."""
        print("Data submitted. (Implement database integration here.)")

if __name__ == "__main__":
    root = tk.Tk()
    app = HospitalManagementSystem(root)
    root.mainloop()
