import customtkinter as tk
import os
from PIL import Image
from src.utils.colors import *
from src.pages.home import Home
from src.pages.capture import Capture
from src.pages.scan import Scan
from src.utils.patient import Patient
from src.pages.patients import PatientsList
from src.utils.images_path import *
patients = [
    Patient("P001", "Yes", "No"),
]
root= tk.CTk()
root.title("Molevision")
root.width=1512
root.height=982
root.geometry("1512x982")
tk.DrawEngine.preferred_drawing_method = "circle_shapes"
# self.bt_dark= "#42454A"
# self.bt_light= "#FFFFFF"
root.active_patient=Patient("","","")
# root.active=root.active_patient if root.active_patient else "no patient selected"
root.active_patient_id=root.active_patient.patient_id if root.active_patient.patient_id != "" else "select patient"
def select_patient(patient):
    root.active_patient=patient
    root.patient_id.configure(text=root.active_patient.patient_id if root.active_patient.patient_id!="" else "patient not selected")
def select_frame_by_name(name):
    # set button color for selected button
    root.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
    root.capture_button.configure(fg_color=("gray75", "gray25") if name == "capture" else "transparent")
    root.scan_button.configure(fg_color=("gray75", "gray25") if name == "scan" else "transparent")
    root.patients_button.configure(fg_color=("gray75", "gray25") if name == "patients" else "transparent")
    root.active_nav=name
    # show selected frame
    if name == "home":
        home_frame.home_frame.grid(row=1, column=0, sticky="nsew")
    else:
        home_frame.home_frame.grid_forget()
    if name == "capture":
        capture_frame.capture_frame.grid(row=1, column=0, sticky="nsew")
    else:
        capture_frame.capture_frame.grid_forget()
    if name == "scan":
         scan_frame.scan_frame.grid(row=1, column=0, sticky="nsew")
    else:
         scan_frame.scan_frame.grid_forget()
    if name == "patients":
        patients_frame.frame.grid(row=1, column=0, sticky="nsew")
    else:
        patients_frame.frame.grid_forget()
    

def home_button_event():
    select_frame_by_name("home")

def capture_button_event():
    select_frame_by_name("capture")
def scan_button_event():
    select_frame_by_name("scan")
    
def patients_button_event():
    select_frame_by_name("patients")

def change_appearance_mode_event(new_appearance_mode):
    color_change(root,new_appearance_mode)
    tk.set_appearance_mode(new_appearance_mode)

root.activate_patient=select_patient
root.select_frame=select_frame_by_name
# set grid layout 2x1
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

# load images with light and dark mode image

# create navigation frame
root.navigation_frame = tk.CTkFrame(root,fg_color=nav_color , corner_radius=0)
root.navigation_frame.grid(row=0, column=0, sticky="ew")
root.navigation_frame.grid_columnconfigure((0,5), weight=1)

root.navigation_frame_label = tk.CTkLabel(root.navigation_frame, text="", image=logo_image,
                                                        compound="left", font=tk.CTkFont(size=15, weight="bold"))
root.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

root.home_button = tk.CTkButton(root.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Home",
                                            fg_color="transparent", text_color=txt_clr, hover_color=("gray70", "gray30"),
                                            image=home_image, anchor="w", command=home_button_event)
root.home_button.grid(row=0, column=1, padx=20, pady=10)

root.capture_button = tk.CTkButton(root.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Capture",
                                                fg_color="transparent", text_color=txt_clr, hover_color=("gray70", "gray30"),
                                                image=image_icon_image, anchor="w", command=capture_button_event)
root.capture_button.grid(row=0, column=2, padx=20, pady=10)
root.scan_button = tk.CTkButton(root.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Scan",
                                                fg_color="transparent", text_color=txt_clr, hover_color=("gray70", "gray30"),
                                                image=image_icon_image, anchor="w", command=scan_button_event)
root.scan_button.grid(row=0, column=3, padx=20, pady=10)
root.patients_button = tk.CTkButton(root.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Patients",
                                                fg_color="transparent", text_color=txt_clr, hover_color=("gray70", "gray30"),
                                                image=add_user_image, anchor="w", command=patients_button_event)
root.patients_button.grid(row=0, column=4, padx=20, pady=10)
root.patient_id=tk.CTkLabel(root.navigation_frame, text=root.active_patient.patient_id if root.active_patient.patient_id else "patient not selected",height=40,text_color="#ffffff")
root.patient_id.grid(row=0,column=5,padx=20,pady=20)
root.appearance_mode_menu = tk.CTkOptionMenu(root.navigation_frame,text_color=txt_clr,fg_color=txt_clr,button_hover_color=btn_color, values=["Dark", "Light", "System"],
                                                        command=change_appearance_mode_event)
root.appearance_mode_menu.grid(row=0, column=6, padx=20, pady=10, sticky="e")
change_appearance_mode_event("Dark")
# create home frame
home_frame= Home(root)

# create capture frame
capture_frame = Capture(root)

#create scan frame
scan_frame=Scan(root)

# create third frame
# patients_frame = tk.CTkFrame(root, corner_radius=0, fg_color="transparent")
patients_frame = PatientsList(root, patients)
# select default frame

select_frame_by_name("home")


       

root.mainloop()
