import tkinter as tk
from tkinter import ttk
import sqlite3

class HospitalManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")

        # Connect to SQLite database
        self.conn = sqlite3.connect("hospital.db")
        self.cursor = self.conn.cursor()

        # Define entities and their fields
        self.entities = {
            "Employee": ["ID", "Name", "Phone"],
            "Staff": ["ID", "Name", "DOB", "Address"],
            "Department": ["ID", "Name", "Address"],
            "Doctor": ["ID", "Name", "DOB", "Email", "Specialty", "Department"],
            "Patient": ["ID", "Name", "DOB", "Address", "Emergency Phone", "Allergy"],
            "Appointment": ["ID", "Patient ID", "Doctor ID", "Date", "Time", "Room"],
            "Room": ["Room Code", "Name", "Address"],
            "Bill": ["ID", "Patient ID", "Service Cost", "Date"],
            "Medication": ["ID", "Name", "Dose", "Cost", "Pharmacy ID"],
            "Pharmacy": ["ID", "Name", "Address", "Phone"],
        }

        # Initialize tables for all entities
        self.initialize_tables()

        # Create GUI tabs
        self.create_tabs()

    def initialize_tables(self):
        """Initialize database tables for all entities."""
        for entity, fields in self.entities.items():
            field_definitions = ", ".join(f"{field} TEXT" for field in fields)
            sql = f"CREATE TABLE IF NOT EXISTS {entity} ({field_definitions})"
            self.cursor.execute(sql)
        self.conn.commit()

    def create_tabs(self):
        """Creates tabs for each entity."""
        self.tab_control = ttk.Notebook(self.root)

        # Create a tab for each entity
        self.tabs = {}
        for entity, fields in self.entities.items():
            self.create_tab(entity, fields)

        self.tab_control.pack(expand=1, fill="both")

    def create_tab(self, entity_name, fields):
        """Creates a tab with form fields for an entity."""
        tab = ttk.Frame(self.tab_control)
        self.tab_control.add(tab, text=entity_name)
        self.tabs[entity_name] = {
            "tab": tab,
            "fields": fields,
            "entries": {},  # To store Entry widgets
        }
        self.create_form(tab, entity_name, fields)

    def create_form(self, tab, entity_name, fields):
        """Creates a form with labels and entry boxes for the given fields."""
        for i, field in enumerate(fields):
            label = ttk.Label(tab, text=field)
            label.grid(row=i, column=0, padx=10, pady=5, sticky="w")
            entry = ttk.Entry(tab)
            entry.grid(row=i, column=1, padx=10, pady=5)
            self.tabs[entity_name]["entries"][field] = entry

        # Add Submit button
        submit_button = ttk.Button(tab, text="Submit", command=lambda: self.submit_data(entity_name))
        submit_button.grid(row=len(fields), column=0, columnspan=2, pady=10)

        # Add Fetch button
        fetch_button = ttk.Button(tab, text="Fetch Data", command=lambda: self.fetch_data(entity_name))
        fetch_button.grid(row=len(fields) + 1, column=0, columnspan=2, pady=10)

        # Add Update button
        update_button = ttk.Button(tab, text="Update Data", command=lambda: self.update_data(entity_name))
        update_button.grid(row=len(fields) + 2, column=0, columnspan=2, pady=10)

        # Add Delete button
        delete_button = ttk.Button(tab, text="Delete Data", command=lambda: self.delete_data(entity_name))
        delete_button.grid(row=len(fields) + 3, column=0, columnspan=2, pady=10)

        # Add Treeview to display data
        tree = ttk.Treeview(tab, columns=fields, show="headings")
        tree.grid(row=len(fields) + 4, column=0, columnspan=2, padx=10, pady=10)
        for field in fields:
            tree.heading(field, text=field)
            tree.column(field, width=100)
        self.tabs[entity_name]["tree"] = tree

    def submit_data(self, entity_name):
        """Insert data into the corresponding database table."""
        try:
            entries = self.tabs[entity_name]["entries"]
            data = {field: entry.get() for field, entry in entries.items()}

            fields = ", ".join(data.keys())
            placeholders = ", ".join(f":{field}" for field in data.keys())
            sql = f"INSERT INTO {entity_name} ({fields}) VALUES ({placeholders})"

            self.cursor.execute(sql, data)
            self.conn.commit()
            print(f"Data submitted successfully to {entity_name}.")
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")

    def fetch_data(self, entity_name):
        """Fetch and display data from the database for a specific entity."""
        try:
            self.cursor.execute(f"SELECT * FROM {entity_name}")
            records = self.cursor.fetchall()

            # Clear the treeview
            tree = self.tabs[entity_name]["tree"]
            for item in tree.get_children():
                tree.delete(item)

            # Insert new data
            for record in records:
                tree.insert("", "end", values=record)
        except sqlite3.Error as e:
            print(f"An error occurred while fetching data: {e}")

    def update_data(self, entity_name):
        """Update data in the database for a specific entity."""
        try:
            entries = self.tabs[entity_name]["entries"]
            data = {field: entry.get() for field, entry in entries.items()}

            identifier_field = list(data.keys())[0]
            identifier_value = data[identifier_field]

            updates = ", ".join(f"{field} = :{field}" for field in data.keys() if field != identifier_field)
            sql = f"UPDATE {entity_name} SET {updates} WHERE {identifier_field} = :{identifier_field}"

            self.cursor.execute(sql, data)
            self.conn.commit()
            print(f"Data updated successfully in {entity_name}.")
        except sqlite3.Error as e:
            print(f"An error occurred while updating data: {e}")

    def delete_data(self, entity_name):
        """Delete data from the database for a specific entity."""
        try:
            entries = self.tabs[entity_name]["entries"]
            identifier_field = list(entries.keys())[0]
            identifier_value = entries[identifier_field].get()

            sql = f"DELETE FROM {entity_name} WHERE {identifier_field} = ?"
            self.cursor.execute(sql, (identifier_value,))
            self.conn.commit()
            print(f"Record with {identifier_field} = {identifier_value} deleted successfully.")
        except sqlite3.Error as e:
            print(f"An error occurred while deleting data: {e}")

    def __del__(self):
        """Close the database connection on exit."""
        self.conn.close()

if __name__ == "__main__":
    root = tk.Tk()
    app = HospitalManagementSystem(root)
    root.mainloop()
