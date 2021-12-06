from tkinter import *
import os

def Login_Button():
    print("Button Clicked")
    window.destroy()
    os.system("Login_page.py")
   

def register_button():
    print("button clicked")
    window.destroy()
    os.system("register_page.py")

window = Tk()

window.geometry("1000x600")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 600,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"E:\GUI\welcome page/background.png")
background = canvas.create_image(
    500.5, 300.0,
    image=background_img)

img0 = PhotoImage(file = f"E:\GUI\welcome page/img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = Login_Button,
    relief = "flat")

b0.place(
    x = 750, y = 169,
    width = 161,
    height = 161)

img1 = PhotoImage(file = f"E:\GUI\welcome page/img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = register_button,
    relief = "flat")

b1.place(
    x = 750, y = 353,
    width = 161,
    height = 179)

window.resizable(False, False)
window.mainloop()
