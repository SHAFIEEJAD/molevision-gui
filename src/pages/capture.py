# capture.py
import customtkinter as tk
from PIL import Image,ImageTk
import cv2
import numpy as np
from matplotlib import pyplot as plt
import os
from src.utils.images_path import *
from src.utils.colors import *
from datetime import datetime
import torch
import torch.nn as nn
from torchvision.models import mobilenet_v3_large
from torchvision import transforms

class Capture:
    def __init__(self,root):
        # capture frame
        self.root=root

        # Load model
        self.model = mobilenet_v3_large()
        self.model.classifier[3] = nn.Linear(self.model.classifier[3].in_features, 2)
        self.model.load_state_dict(torch.load("latest_model_epoch20.pth", map_location=torch.device("cpu")))
        self.model.eval()

        # Transformation to match training
        self.transform = transforms.Compose([
            transforms.ToPILImage(),
            transforms.Resize((512, 512)),
            transforms.ToTensor(),
            transforms.Normalize([0.5]*3, [0.5]*3)
        ])

        self.is_capture=0
        self.is_save=0
        ###connecting to the camera
        self.cap =cv2.VideoCapture(0)
        self.capture_frame = tk.CTkFrame(root, corner_radius=0, fg_color="#ffffff")
        self.capture_frame.grid_rowconfigure(0, weight=1)
        self.capture_frame.grid_rowconfigure(1, weight=0) 
        self.capture_frame.grid_columnconfigure(0, weight=99)  # Left frame gets 3 parts
        self.capture_frame.grid_columnconfigure(1, weight=1)  # Right frame gets 1 part
        
        # Left frame
        self.left_frame = tk.CTkFrame(self.capture_frame, corner_radius=0, fg_color="#290805", width=1045, height=636)
        self.left_frame.grid_rowconfigure(0, weight=1)
        self.left_frame.grid_columnconfigure(0, weight=1)
        self.left_frame.grid(row=0, column=0, padx=20, pady=10, sticky="nsew")

        # Label to display the video feed
        self.video_label = tk.CTkLabel(self.left_frame,text="")
        self.video_label.grid(row=0, column=0, sticky="nsew")

        # Right frame
        self.right_frame = tk.CTkFrame(self.capture_frame, corner_radius=0, fg_color="transparent")
        self.right_frame.grid_rowconfigure((0,1,2), weight=1)
        self.right_frame.grid(row=0, column=1, padx=20, pady=10, sticky="nsew")

        # Buttons in the right frame
        self.capture_frame_button_1 = tk.CTkButton(self.right_frame, text="Capture", image=image_icon_image, compound="right",width=360.88,height=73.61,fg_color=btn_color,command=self.capturing)
        self.capture_frame_button_1.grid(row=0, column=0, padx=20, pady=10,sticky="ews",)
        self.capture_frame_button_2 = tk.CTkButton(self.right_frame, text="Re-Capture", image=image_icon_image, compound="right",width=360.88,height=73.61,fg_color=btn_color,command=self.recapturing)
        self.capture_frame_button_2.grid(row=1, column=0, padx=20, pady=10,sticky="ewn")
        self.capture_frame_button_3 = tk.CTkButton(self.right_frame, text="Save", image=image_icon_image, compound="top",width=360.88,height=73.61,command=self.open_popup,fg_color=btn_color)
        self.capture_frame_button_3.grid(row=2, column=0, padx=20, pady=10,sticky="n")
        
         # Bottom frame
        self.bottom_frame = tk.CTkFrame(self.capture_frame, corner_radius=0, fg_color="transparent")
        self.bottom_frame.grid_rowconfigure(0, weight=1)
        self.bottom_frame.grid_columnconfigure(0, weight=1)
        self.bottom_frame.grid(row=1, column=0, columnspan=2, sticky="ew", padx=20, pady=10)

        # Button in the bottom frame
        self.bottom_button = tk.CTkButton(self.bottom_frame, text="Scan",fg_color=btn_color)
        self.bottom_button.grid(row=0, column=0, padx=20, pady=10)

        # Add the capture frame to the root window
        self.capture_frame.grid(row=0, column=0, sticky="nsew")

        #start vidoe
        if self.cap.isOpened():
            self.update_video_stream()
    def open_popup(self):
        self.popup = tk.CTkToplevel(self.root)
        self.popup.geometry("400x400")
        self.popup.title("Save Data")

        # patients input field
        label = tk.CTkLabel(self.popup, text="Patient ID:")
        label.pack(pady=10)
        entry = tk.CTkLabel(self.popup, text=self.root.active_patient.patient_id)
        entry.pack(pady=10)

        # Manoma Classification switch
        manoma_label = tk.CTkLabel(self.popup, text="Manoma Classification")
        manoma_label.pack(pady=10)
        manoma_switch = tk.CTkSwitch(self.popup, text="No/Yes")
        manoma_switch.pack(pady=10)

        # Biopsy Recommendation switch
        biopsy_label = tk.CTkLabel(self.popup, text="Biopsy Recommendation")
        biopsy_label.pack(pady=10)
        biopsy_switch = tk.CTkSwitch(self.popup, text="No/Yes")
        biopsy_switch.pack(pady=10)

        # Save Button
        save_button = tk.CTkButton(self.popup, text="Save", command=self.save_data,fg_color=btn_color)
        save_button.pack(pady=20)

        # Close Button
        close_button = tk.CTkButton(self.popup, text="Close", command=self.popup.destroy,fg_color=btn_color)
        close_button.pack(pady=10)

    def save_data(self):
        # Logic to save data goes here
        self.is_save=1
        self.popup.destroy()
        print("Data saved")
    def recapturing(self):
        self.is_capture=0

    def apply_preprocessing(self, image):

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        denoised = cv2.bilateralFilter(gray, 9, 75, 75)
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        enhanced = clahe.apply(denoised)
        # Check Blurriness (Variance of Laplacian)
        blur_metric = cv2.Laplacian(enhanced, cv2.CV_64F).var()
        if blur_metric < 100:
            print("⚠ Warning: Captured image may be blurry!")

        gaussian_blur = cv2.GaussianBlur(enhanced, (5, 5), 1.5)
        sharpened = cv2.addWeighted(enhanced, 1.5, gaussian_blur, -0.5, 0)
        sharpened_rgb = cv2.cvtColor(sharpened, cv2.COLOR_GRAY2BGR)
        return sharpened_rgb


    def update_video_stream(self):
        current_time = datetime.today().strftime('%Y-%m-%d-%H:%M:%S')
        patient_id = self.root.active_patient.patient_id
        path_to_store = os.path.join(captured_path, patient_id)

        ret, frame = self.cap.read()

        if ret and self.is_capture != 1:
            # Display video feed
            display_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            display_frame = cv2.resize(display_frame, (1045, 636))
            img = Image.fromarray(display_frame)
            imgtk = ImageTk.PhotoImage(image=img)
            self.video_label.imgtk = imgtk
            self.video_label.configure(image=imgtk)

        elif ret and self.is_capture == 1:
            if self.is_save:
                if not os.path.exists(path_to_store):
                    os.makedirs(path_to_store)

                # Save original image
                original_filename = f"{patient_id}_{current_time}.jpg"
                original_filepath = os.path.join(path_to_store, original_filename)
                cv2.imwrite(original_filepath, frame)
                print(f"✅ Original image saved at: {original_filepath}")

                # Preprocess the image
                processed_image = self.apply_preprocessing(frame)

                # Save preprocessed (filtered) image
                filtered_filename = f"{patient_id}_{current_time}_filtered.jpg"
                filtered_filepath = os.path.join(path_to_store, filtered_filename)
                cv2.imwrite(filtered_filepath, processed_image)
                print(f"✅ Filtered image saved at: {filtered_filepath}")

                self.is_save = 0
                self.recapturing()

        # Continuously update video stream
        self.root.after(10, self.update_video_stream)

    # def update_video_stream(self):
    #     current_time=''+datetime.today().strftime('%Y-%m-%d-%H:%M:%S')
    #     path_to_store=''+captured_path+'/'+self.root.active_patient.patient_id
    #     ret, frame = self.cap.read()
        
    #     if ret & self.is_capture!=1:
    #         frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    #         frame=cv2.resize(frame,(1045,636))
    #         img = Image.fromarray(frame)
    #         imgtk = ImageTk.PhotoImage(image=img)
    #         self.video_label.imgtk = imgtk
    #         self.video_label.configure(image=imgtk)
           
    #     elif ret & self.is_capture ==1:
    #         ret, frame = self.cap.read()
    #         if ret & self.is_save:
    #             if not os.path.exists(path_to_store):
    #                 os.makedirs(path_to_store)
    #             cv2.imwrite(os.path.join(path_to_store,f'{self.root.active_patient.patient_id+current_time}.jpg'), frame)
    #             self.is_save=0
    #             print(path_to_store)
    #             self.recapturing()
    #             # plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    #             # plt.show()
    #             # self.is_capture=0
    #     # Call the function again after 10 ms
    #     self.root.after(10, self.update_video_stream) 

    def capturing(self):
        self.is_capture=1
        # Get frame
        ret, frame = self.cap.read()
        if not ret:
            print("❌ Failed to read from camera")
            return

        # Preprocess
        processed = self.apply_preprocessing(frame)
        transformed = self.transform(processed).unsqueeze(0)

        # Predict
        with torch.no_grad():
            output = self.model(transformed)
            pred = torch.argmax(output, dim=1).item()

        result_text = "Malignant" if pred == 1 else "Benign"
        print(f"✅ Prediction: {result_text}")

        # Optional: show result on GUI
        result_label = tk.CTkLabel(self.right_frame, text=f"Prediction: {result_text}", text_color="#00FF00" if pred == 0 else "#FF0000", font=("Arial", 16))
        result_label.grid(row=3, column=0, pady=10)

    def display_message(self):
        print(f"hi hello  {self.message}")
