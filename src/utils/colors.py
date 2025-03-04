from tkinter import messagebox
#Buttons dark
bt_dark= "#290805"
bt_light= "#FFFFFF"

#Buttons dark
text_dark= "#42454A"
text_light= "#FFFFFF"

#nav frame
nav_dark ="#261104"
nav_light="#EAE8F3"

btn_color=bt_dark
nav_color=nav_light
txt_clr=text_dark
def color_change(root,color_mode):
    # print(f"hi tthis {color_mode}")
    if(color_mode=="Dark"):
        btn_color=bt_light
        nav_color=nav_dark
        txt_clr=text_light
    elif(color_mode=="Light"):
        print("Light mode under construction ")
        messagebox.showerror("Construction", "Light Mode under construction")
        return
        # txt_clr=text_dark
        # btn_color=bt_dark
        # nav_color=nav_light
    else:
        print("System mode under construction ")
        messagebox.showerror("Construction", "Sytem Mode under construction")
        return
    root.navigation_frame.configure(fg_color=nav_color)
    root.home_button.configure(text_color=txt_clr)
    root.capture_button.configure(text_color=txt_clr)
    root.patients_button.configure(text_color=txt_clr)
    root.scan_button.configure(text_color=txt_clr)
    root.appearance_mode_menu.configure(text_color=nav_color,fg_color=txt_clr)