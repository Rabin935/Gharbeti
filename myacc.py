from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
from tkinter import PhotoImage
a=Tk()
# a.iconbitmap("a.ico")
a.title("GHARBETI - My profile")
a.geometry("450x650")
a.resizable(0,0)
a.config(bg='#F0F4F7')



Frame(a, width=700, height=180, bg='#007EA3').place(x = 0, y = 0)


staff_id = Label(a, text='Staff Account',
                 font=('Ariel', 40),
                 fg= '#F0F4F7',
                 bg='#007EA3')
staff_id.place(x = 60, y = 60)


id_no = Label(a, text="Id no",
              font=("Calibri",20),
              bg='#F0F4F7')
id_no.place(x = 40, y = 210)
name_of_staff = Label(a, text="Name of Staff ",
              font=("Calibri",20),
              bg='#F0F4F7')
name_of_staff.place(x = 40, y = 260)
email = Label(a, text="Email",
              font=("Calibri",20),
              bg='#F0F4F7')
email.place(x = 40, y = 310)
contact = Label(a, text="Contact",
              font=("Calibri",20),
              bg='#F0F4F7')
contact.place(x = 40, y = 360)


logout = Button(a, text='Log out',
                bg="#007EA3",
                font=('Calibri', 20))
logout.place(x = 150, y = 460)


a.mainloop()