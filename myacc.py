from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
from tkinter import PhotoImage
a=Tk()
# a.iconbitmap("a.ico")
a.title("GHARBETI - My profile")
a.geometry("700x900")
a.resizable(0,0)
a.config(bg='#F0F4F7')

# image = Image.open("img/myaccbgimg.png")

# img = ImageTk.PhotoImage(image)
# background_label = Label(a, image=img)

# label = Label(a, image=img)
# label.pack()

# c = Canvas(a, height=1100, width = 700)
# bgimage = PhotoImage(file='img/myaccbgimg.jpg')
# background_label = Label(a, image=bgimage)
# background_label.place(x=0, y=0, relwidth=1, relheight=1)
# c.pack()

# def home():
#     a.destroy()
#     import home
# def vflat():
#     a.destroy()
#     import viewflats
# def tenant():
#     a.destroy()
#     import ant
# def aap():
#     a.destroy()
#     import aap
# def myacc():
#     a.destroy()
#     import myacc

Frame(a, width=700, height=900, bg='#B53CFF').place(x = 0, y = 0)
Frame(a, width=700, height=900, bg='#FFA800').place(x = 0, y = 290)
Frame(a, width=150,height=150, bg='blue').place(x = 280, y = 170)


id_no = Label(a, text="Id no",
              font=("Calibri",25),
              bg='#FFA800')
id_no.place(x = 250, y = 340)
name_of_staff = Label(a, text="Name of Staff ",
              font=("Calibri",25),
              bg='#FFA800')
name_of_staff.place(x = 250, y = 400)
email = Label(a, text="Email",
              font=("Calibri",25),
              bg='#FFA800')
email.place(x = 250, y = 460)
contact = Label(a, text="Contact",
              font=("Calibri",25),
              bg='#FFA800')
contact.place(x = 250, y = 520)


logout = Button(a, text='Log out',
                bg="#007EA3",
                font=('Calibri', 25))
logout.place(x = 250, y = 800)


a.mainloop()