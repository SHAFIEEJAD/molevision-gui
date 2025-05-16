# from home import Home
# from capture import Capture
# import customtkinter as tk


# root=tk.CTk()
# home_frame= Home(root)
# capture_frame=Capture(root)
import os
image_path = "/home/shafieej/Molevision-GUI/images"

captured_path= "/home/shafieej/Molevision-GUI/captured"

captured_images_path= "/home/shafieej/Molevision-GUI/images/captured_images"

if not os.path.exists(image_path):
    os.makedirs(image_path)
if not os.path.exists(captured_path):
    os.makedirs(captured_path)
if not os.path.exists(captured_images_path):
    os.makedirs(captured_images_path)
