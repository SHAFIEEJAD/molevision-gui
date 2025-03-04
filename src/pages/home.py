import customtkinter as tk
import os
from PIL import Image
from src.utils.colors import *
from src.utils.images_path import wallpaper,large_test_image
class Home:
    def __init__(self, root):
        self.root = root

        self.home_frame=tk.CTkFrame(self.root, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_rowconfigure(0, weight=1)
        self.home_frame.grid_columnconfigure(0, weight=1)

        # Load background image
        self.bg_image = tk.CTkImage(wallpaper, size=(self.home_frame.winfo_screenwidth(), self.home_frame.winfo_screenheight()))


    
        # Create label to hold the background image
        self.bg_label = tk.CTkLabel(self.home_frame, text="", image=self.bg_image)
        self.bg_label.grid(row=0, column=1, sticky="nsew")


        # Create buttons
        self.capture_button = tk.CTkButton(self.home_frame, text="Capture", command=self.capture, width=200, height=50,fg_color=btn_color)
        self.scan_button = tk.CTkButton(self.home_frame, text="Scan", command=self.scan, width=200, height=50,fg_color=btn_color)
        self.patients_button = tk.CTkButton(self.home_frame, text="Patients", command=self.patients, width=200, height=50,fg_color=btn_color)

        # Position buttons on the canvas
        self.capture_button.place(relx=0.4, rely=0.5, anchor="center")
        self.scan_button.place(relx=0.6, rely=0.5, anchor="center")
        self.patients_button.place(relx=0.5, rely=0.6, anchor="center")

    def scan(self):
        # Define what happens when the Scan button is clicked
        print("Scan button clicked")
        self.root.select_frame("scan")
    def capture(self):
        # Define what happens when the Scan button is clicked
        print("Scan button clicked")
        self.root.select_frame("capture")

    def patients(self):
        # Define what happens when the Patients button is clicked
        print("Patients button clicked")
        self.root.select_frame("patients")