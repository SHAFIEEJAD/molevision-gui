import os
from PIL import Image
import customtkinter as tk
#--load images  i would be using
from config import *

logo_image = tk.CTkImage(Image.open(os.path.join(image_path, "mole_logo_w.png")), size=(50, 50))
large_test_image = tk.CTkImage(Image.open(os.path.join(image_path, "large_test_image.png")), size=(500, 150))
image_icon_image = tk.CTkImage(Image.open(os.path.join(image_path, "image_icon_light.png")), size=(20, 20))
home_image = tk.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")),
                                            dark_image=Image.open(os.path.join(image_path, "home_light.png")), size=(20, 20))
chat_image = tk.CTkImage(light_image=Image.open(os.path.join(image_path, "chat_dark.png")),
                                            dark_image=Image.open(os.path.join(image_path, "chat_light.png")), size=(20, 20))
add_user_image = tk.CTkImage(light_image=Image.open(os.path.join(image_path, "add_user_dark.png")),
                                                dark_image=Image.open(os.path.join(image_path, "add_user_light.png")), size=(20, 20))



##home
# Load background image
wallpaper = Image.open(os.path.join(image_path, "wallpaper_white.png"))


