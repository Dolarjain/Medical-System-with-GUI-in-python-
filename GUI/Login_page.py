from tkinter import *
from tkinter import ttk,messagebox
import mysql.connector as mysql
import os

def login():
    
    if username.get()=="" or password.get()=="":
       messagebox.showerror("field error","enter all fields",parent=window) 
    if username.get()=="Dev@123" and password.get()=="Dev@123":
       window.destroy()
       os.system("devloper_page.py")
    else:
       db1=mysql.connect(host='localhost',user='root',password='Dj2000@jain',database='hospital')
       mycursor1=db1.cursor()
       print("database connected...")
       
       mycursor1.execute("select username,password from resister_user where BINARY username=%s and BINARY password=%s",(username_var.get(),password_var.get()))
       row=mycursor1.fetchone()
       print(row)
       if row==None:
           messagebox.showerror("Value error",'enter correct value',parent=window)
           db1.close() 
           print("database closed.....") 
           
       else:
           window.destroy()
           os.system("register_page.py")

def Button1():
    messagebox.showerror("Value error",'enter correct value',parent=window)
    print("hello world")

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

background_img = PhotoImage(file = f"Login_page/background.png")
background = canvas.create_image(
    500.0, 300.0,
    image=background_img)

img0 = PhotoImage(file = f"Login_page/img0.png")
login_Button = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command =login,
    relief = "flat")

login_Button.place(
    x = 621, y = 488,
    width = 145,
    height = 38)

# img1 = PhotoImage(file = f"Login_page/img1.png")
# Send_otp = Button(
#     image = img1,
#     borderwidth = 0,
#     highlightthickness = 0,
#     command = Button1,
#     relief = "flat")

# Send_otp.place(
#     x = 771, y = 389,
#     width = 80,
#     height = 38)



username_img = PhotoImage(file = f"Login_page/img_textBox1.png")
username_bg = canvas.create_image(
    693.5, 230.0,
    image = username_img)

username_var = StringVar()
username = Entry(
    bd = 0,
    bg = "#e1cece",
    highlightthickness = 0,
    textvariable=username_var)

username.place(
    x = 555.0, y = 211,
    width = 277.0,
    height = 36)

password_img = PhotoImage(file = f"Login_page/img_textBox2.png")
password_bg = canvas.create_image(
    693.5, 319.0,
    image = password_img)

password_var = StringVar()
password = Entry(
    bd = 0,
    bg = "#e1cece",
    highlightthickness = 0,
    textvariable=password_var)

password.place(
    x = 555.0, y = 300,
    width = 277.0,
    height = 36)

# otp_img = PhotoImage(file = f"Login_page/img_textBox0.png")
# otp_bg = canvas.create_image(
#     651.0, 408.0,
#     image = otp_img)

# otp_var=StringVar()
# otp = Entry(
#     bd = 0,
#     bg = "#e1cece",
#     highlightthickness = 0,
#     textvariable=otp_var)

# otp.place(
#     x = 555.0, y = 389,
#     width = 192.0,
#     height = 36)

window.resizable(False, False)
window.mainloop()
