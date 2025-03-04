# scan.py
import customtkinter as tk
import shutil
from PIL import Image
import subprocess
from src.utils.images_path import *
from src.utils.colors import *
from datetime import datetime
class Scan:
    def __init__(self,root):
        # scan frame
        self.root=root
        self.scan_frame = tk.CTkFrame(root, corner_radius=0, fg_color="#ffffff")
        self.scan_frame.grid_rowconfigure(0, weight=1)
        self.scan_frame.grid_rowconfigure(1, weight=0) 
        self.scan_frame.grid_columnconfigure(0, weight=3)  
        self.scan_frame.grid_columnconfigure(1, weight=1)  

        # Left frame
        self.left_frame = tk.CTkFrame(self.scan_frame, corner_radius=0, fg_color="#290805",width=1045, height=636)
        self.left_frame.grid_rowconfigure(0, weight=1)
        self.left_frame.grid(row=0, column=0, padx=20, pady=10, sticky="nsew")

        # Right frame
        self.right_frame = tk.CTkFrame(self.scan_frame, corner_radius=0, fg_color="transparent")
        self.right_frame.grid_rowconfigure((0,1,2), weight=1)
        self.right_frame.grid(row=0, column=1, padx=20, pady=10, sticky="nsew")

        # Buttons in the right frame
        self.scan_frame_button_1 = tk.CTkButton(self.right_frame, text="scan", image=image_icon_image, compound="right",width=360.88,height=73.61,fg_color=btn_color,command=self.scanning)
        self.scan_frame_button_1.grid(row=0, column=0, padx=20, pady=10,sticky="ews",)
        self.scan_frame_button_2 = tk.CTkButton(self.right_frame, text="Re-scan", image=image_icon_image, compound="right",width=360.88,height=73.61,fg_color=btn_color)
        self.scan_frame_button_2.grid(row=1, column=0, padx=20, pady=10,sticky="ewn")
        self.scan_frame_button_3 = tk.CTkButton(self.right_frame, text="Save", image=image_icon_image, compound="top",width=360.88,height=73.61,command=self.open_popup,fg_color=btn_color)
        self.scan_frame_button_3.grid(row=2, column=0, padx=20, pady=10,sticky="n")
        
         # Bottom frame
        self.bottom_frame = tk.CTkFrame(self.scan_frame, corner_radius=0, fg_color="transparent")
        self.bottom_frame.grid_rowconfigure(0, weight=1)
        self.bottom_frame.grid_columnconfigure(0, weight=1)
        self.bottom_frame.grid(row=1, column=0, columnspan=2, sticky="ew", padx=20, pady=10)

        # Button in the bottom frame
        self.bottom_button = tk.CTkButton(self.bottom_frame, text="Scan", fg_color=btn_color)
        self.bottom_button.grid(row=0, column=0, padx=20, pady=10)

        # Add the scan frame to the root window
        self.scan_frame.grid(row=0, column=0, sticky="nsew")
        
        self.value_textbox = tk.CTkTextbox(self.left_frame,width=1045,height=636)
        self.value_textbox.grid(row=0,column =0,padx=5,pady=5,sticky='nswe')
        self.value_textbox.configure(state="disabled")
    def open_popup(self):
        popup = tk.CTkToplevel(self.root)
        popup.geometry("400x400")
        popup.title("Save Data")

        # Alphanumeric input field
        label = tk.CTkLabel(popup, text="Patient ID:")
        label.pack(pady=10)
        entry = tk.CTkLabel(popup, text=self.root.active_patient_name)
        entry.pack(pady=10)

        # Manoma Classification switch
        manoma_label = tk.CTkLabel(popup, text="Manoma Classification")
        manoma_label.pack(pady=10)
        manoma_switch = tk.CTkSwitch(popup, text="No/Yes")
        manoma_switch.pack(pady=10)

        # Biopsy Recommendation switch
        biopsy_label = tk.CTkLabel(popup, text="Biopsy Recommendation")
        biopsy_label.pack(pady=10)
        biopsy_switch = tk.CTkSwitch(popup, text="No/Yes")
        biopsy_switch.pack(pady=10)

        # Save Button
        save_button = tk.CTkButton(popup, text="Save", command=self.save_data,fg_color=btn_color)
        save_button.pack(pady=20)

        # Close Button
        close_button = tk.CTkButton(popup, text="Close", command=popup.destroy,fg_color=btn_color)
        close_button.pack(pady=10)


    def save_data(self):
        # Logic to save data goes here
        
        print("Data saved")

    def scanning(self):
        current_time=''+datetime.today().strftime('%Y-%m-%d-%H:%M:%S')
#        subprocess.run(["echo" ,"53215404","|","sudo", "-S","ls"])
 #       subprocess.run(["bash","/home/ubuntu/Desktop/molevision/gui_ms_mdvoves3/gui/#tiny.sh",self.root.active_patient.patient_id])
        
        self.run_script()
        src_path = os.path.join('/home/ubuntu/Desktop/mmwave/',f'{self.root.active_patient.patient_id}.zip')
        path_to_store=''+captured_path+'/'+self.root.active_patient.patient_id
        if not os.path.exists(path_to_store):
    	    os.makedirs(path_to_store)
        dest_path = os.path.join(path_to_store,f'{self.root.active_patient.patient_id}_{current_time}.zip')
        shutil.move(src_path,dest_path)
       # print("Returned value: ",returned_value)
    def display_message(self):
        print(f"hi hello  {self.message}")
    def run_script(self):
        process=subprocess.Popen(["python3","/home/ubuntu/Desktop/molevision/gui_ms_mdvoves3/gui/tinyv2.py",self.root.active_patient.patient_id],stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
        for line in process.stdout:
            value = line.strip()
            #print(f"In parent:  {value}")
            self.update_value(value)
            
            
    def update_value(self,value):
        self.value_textbox.configure(state="normal")
        self.value_textbox.insert(tk.END, value+"\n")
        self.value_textbox.configure(state="disabled")
        
        
