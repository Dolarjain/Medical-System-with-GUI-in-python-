from tkinter import *
from tkinter import messagebox
import mysql.connector as mysql 

def btn_clicked():
    print("Button Clicked")
def add_med():

    if medicine_id.get()=="" or madicine_name.get()=="" or madicine_price.get()=="" or description_field.get()=="":
       messagebox.showerror("ERROR","ALL FIELDS ARE REQUIRED",parent=window)
    else:   
        try:
    #dealing with the database table for entering the information of the user_hospital
            db=mysql.connect(host="localhost",user="root",password="Dj2000@jain",database="hospital")
            mycursor=db.cursor()
            mycursor.execute("insert into madicines (madicine_id,madicine_name,madicine_price,madicine_description) values (%s,%s,%s,%s)",
                               (
                                #tuple had been created for multiple value inseration 
                                medicine_id.get(),
                                madicine_name.get(),
                                madicine_price.get(),
                                description_field.get()
                               )
                            )
            db.commit()
            db.close()
            messagebox.showinfo("SUCCESS","MEDICINE ADDED SUCCESSFULLY",parent=window)
        except Exception:
            messagebox.showerror("Network","No network/Database Connected...",parent=window)
            
def reset_field():
    medicine_id.delete(0,END)
    madicine_name.delete(0,END)
    madicine_price.delete(0,END)
    description_field.delete(0,END)
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

background_img = PhotoImage(file = f"Devloper_Window/background.png")
background = canvas.create_image(
    86.0, 341.0,
    image=background_img)

img0 = PhotoImage(file = f"Devloper_Window\img0.png")
add_medicine = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = add_med,
    relief = "flat")

add_medicine.place(
    x = 796, y = 112,
    width = 159,
    height = 39)

img1 = PhotoImage(file = f"Devloper_Window\img1.png")
upload_image = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

upload_image.place(
    x = 616, y = 256,
    width = 159,
    height = 39)

img2 = PhotoImage(file = f"Devloper_Window\img2.png")
display_details = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

display_details.place(
    x = 796, y = 184,
    width = 159,
    height = 39)

img3 = PhotoImage(file = f"Devloper_Window\img3.png")
update_madicine = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

update_madicine.place(
    x = 796, y = 256,
    width = 159,
    height = 39)

img4 = PhotoImage(file = f"Devloper_Window\img4.png")
delete_medicine = Button(
    image = img4,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

delete_medicine.place(
    x = 796, y = 328,
    width = 159,
    height = 39)

img5 = PhotoImage(file = f"Devloper_Window\img5.png")
search_medicine = Button(
    image = img5,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

search_medicine.place(
    x = 796, y = 400,
    width = 159,
    height = 39)

img6 = PhotoImage(file = f"Devloper_Window\img6.png")
reset_fields = Button(
    image = img6,
    borderwidth = 0,
    highlightthickness = 0,
    command = reset_field,
    relief = "flat")

reset_fields.place(
    x = 796, y = 472,
    width = 159,
    height = 39)

medicine_id_img = PhotoImage(file = f"Devloper_Window\img_textBox0.png")
medicine_id_bg = canvas.create_image(
    182.0, 212.0,
    image = medicine_id_img)

medicine_id = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

medicine_id.place(
    x = 73.0, y = 193,
    width = 218.0,
    height = 36)

madicine_name_img = PhotoImage(file = f"Devloper_Window\img_textBox1.png")
madicine_name_bg = canvas.create_image(
    477.0, 212.0,
    image = madicine_name_img)

madicine_name = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

madicine_name.place(
    x = 368.0, y = 193,
    width = 218.0,
    height = 36)

description_img = PhotoImage(file = f"Devloper_Window\img_textBox2.png")
description_bg = canvas.create_image(
    477.0, 319.0,
    image = description_img)

description_field = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

description_field.place(
    x = 368.0, y = 300,
    width = 218.0,
    height = 36)

madicine_price_img = PhotoImage(file = f"Devloper_Window\img_textBox3.png")
madicine_price_bg = canvas.create_image(
    182.0, 319.0,
    image = madicine_price_img)

madicine_price = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

madicine_price.place(
    x = 73.0, y = 300,
    width = 218.0,
    height = 36)

madicine_detail_tab_img = PhotoImage(file = f"Devloper_Window\img_textBox4.png")
madicine_detail_tab_bg = canvas.create_image(
    414.5, 476.0,
    image = madicine_detail_tab_img)

madicine_detail_tab = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

madicine_detail_tab.place(
    x = 54, y = 381,
    width = 721,
    height = 188)

window.resizable(False, False)
window.mainloop()
