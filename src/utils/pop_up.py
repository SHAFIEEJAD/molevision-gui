import customtkinter as tk
from src.utils.colors import *

def open_popup(self,title):
        popup = tk.CTkToplevel(self.root)
        popup.geometry("400x400")
        popup.title(title)

        # Alphanumeric input field
        label = tk.CTkLabel(popup, text="Patient ID:")
        label.pack(pady=10)
        self.entry = tk.CTkEntry(popup)
        self.entry.pack(pady=10)

        # Manoma Classification switch
        manoma_label = tk.CTkLabel(popup, text="Manoma Classification")
        manoma_label.pack(pady=10)
        self.manoma_switch = tk.CTkSwitch(popup, text="No/Yes")
        self.manoma_switch.pack(pady=10)

        # Biopsy Recommendation switch
        biopsy_label = tk.CTkLabel(popup, text="Biopsy Recommendation")
        biopsy_label.pack(pady=10)
        self.biopsy_switch = tk.CTkSwitch(popup, text="No/Yes")
        self.biopsy_switch.pack(pady=10)

        # Save Button
        save_button = tk.CTkButton(popup, text="Save", command=self.save_data,fg_color=btn_color)
        save_button.pack(pady=20)

        # Close Button
        close_button = tk.CTkButton(popup, text="Close", command=popup.destroy,fg_color=btn_color)
        close_button.pack(pady=10)