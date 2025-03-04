import customtkinter as tk

class Patient:
    def __init__(self, patient_id, biopsy_recommendation, manoma_classification):
        self.patient_id = patient_id
        self.biopsy_recommendation = biopsy_recommendation
        self.manoma_classification = manoma_classification
