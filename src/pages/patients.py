import customtkinter as tk
from src.utils.colors import *
from src.utils.pop_up import open_popup
from src.utils.patient import Patient
class PatientsList:
    def __init__(self, root, patients):
        self.root = root
        self.patients = patients
        self.filtered_patients = patients

        self.frame = tk.CTkFrame(root)
        self.frame.grid(row=0, column=0, sticky="nsew")
        self.frame.grid_rowconfigure(1, weight=1)  
        self.frame.grid_columnconfigure(0, weight=1)  

        # Search bar
        self.search_entry = tk.CTkEntry(self.frame, placeholder_text="Search by ID")
        self.search_entry.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        self.search_entry.bind("<KeyRelease>", self.filter_patients)

        # Scrollable canvas
        self.canvas = tk.CTkCanvas(self.frame)
        self.canvas.grid(row=1, column=0, sticky="nsew")

        # Scrollbar for the canvas
        self.scrollbar = tk.CTkScrollbar(self.frame, orientation="vertical", command=self.canvas.yview)
        self.scrollbar.grid(row=1, column=1, sticky="ns")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Frame to hold patient entries
        self.entries_frame = tk.CTkFrame(self.canvas)
        self.entries_frame.grid(sticky="nsew")
        self.canvas.create_window((0, 0), window=self.entries_frame, anchor="nw")
        self.entries_frame.grid_rowconfigure(0, weight=1)
        self.entries_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)

        # Header labels
        # tk.CTkLabel(self.entries_frame, text="Name").grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        tk.CTkLabel(self.entries_frame, text="Patient ID").grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        tk.CTkLabel(self.entries_frame, text="Biopsy Recommendation").grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        tk.CTkLabel(self.entries_frame, text="Manoma Classification").grid(row=0, column=2, padx=10, pady=10, sticky="ew")

        self.populate_patients()

        # Add Patient Button
        self.add_patient_button = tk.CTkButton(self.frame, text="Add Patient", command=self.add_patient,fg_color=btn_color)
        self.add_patient_button.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

        self.entries_frame.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

    def populate_patients(self):
        # Clear existing entries
        for widget in self.entries_frame.winfo_children():
            widget.destroy()

        # Header labels
        # tk.CTkLabel(self.entries_frame, text="Name").grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        tk.CTkLabel(self.entries_frame, text="Patient ID").grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        tk.CTkLabel(self.entries_frame, text="Biopsy Recommendation").grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        tk.CTkLabel(self.entries_frame, text="Manoma Classification").grid(row=0, column=2, padx=10, pady=10, sticky="ew")

        # Populate with filtered patient data
        for self.i, patient in enumerate(self.filtered_patients):
            # tk.CTkLabel(self.entries_frame, text=patient.name).grid(row=self.i + 1, column=0, padx=10, pady=5, sticky="ew")
            tk.CTkLabel(self.entries_frame, text=patient.patient_id).grid(row=self.i + 1, column=0, padx=10, pady=5, sticky="ew")
            tk.CTkLabel(self.entries_frame, text=patient.biopsy_recommendation).grid(row=self.i + 1, column=1, padx=10, pady=5, sticky="ew")
            tk.CTkLabel(self.entries_frame, text=patient.manoma_classification).grid(row=self.i + 1, column=2, padx=10, pady=5, sticky="ew")
            self.select_patient = tk.CTkButton(self.entries_frame, text="Select", command=lambda patient=patient:self.activate_patient(patient), width=200, height=50,fg_color=btn_color).grid(row=self.i+1,column=3, padx=10, pady=5, sticky="ew")
            



    def filter_patients(self, event):
        search_query = self.search_entry.get().lower()
        self.filtered_patients = [patient for patient in self.patients if search_query in patient.patient_id.lower()]
        self.populate_patients()
    def activate_patient(self,patient):
        print(patient.patient_id)
        self.root.activate_patient(patient)
    def add_patient(self):
        # Add functionality to add a new patient
        open_popup(self,"Add Patient")
        pass
    def save_data(self):
        # tk.CTkLabel(self.entries_frame, text="New Patient").grid(row=self.i + 1, column=0, padx=10, pady=5, sticky="ew")
        self.i+=1
        self.patients.append(Patient(self.entry.get(),self.biopsy_switch.get(),self.manoma_switch.get()))
        tk.CTkLabel(self.entries_frame, text=self.entry.get()).grid(row=self.i + 1, column=0, padx=10, pady=5, sticky="ew")
        tk.CTkLabel(self.entries_frame, text=self.biopsy_switch.get()).grid(row=self.i + 1, column=1, padx=10, pady=5, sticky="ew")
        tk.CTkLabel(self.entries_frame, text= self.manoma_switch.get()).grid(row=self.i + 1, column=2, padx=10, pady=5, sticky="ew")
        tk.CTkButton(self.entries_frame, text="Select",command=self.activate_patient(self.patients[self.i]), width=200, height=50,fg_color=btn_color).grid(row=self.i+1,column=3, padx=10, pady=5, sticky="ew")
        self.populate_patients()
        
        
        
