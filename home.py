#To create tkinter module
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk,Image

#To create an application window
a=Tk()
a.iconbitmap("a.ico")
a.title("GHARBETI - Home")
screen_width = a.winfo_screenwidth()
screen_height = a.winfo_screenheight()
a.geometry('1300x650')
a.resizable(0,0)
a.config(bg = '#F0F4F7')
c = Canvas(a, height=1100, width = 700)
bgimage = PhotoImage(file='img/homepageimg.png')
background_label = Label(a, image=bgimage)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
c.pack()



def home():
    a.destroy()
    import home
def vflat():
    a.destroy()
    import viewflats
def myacc():
    a.destroy()
    import myacc


slogan = Label(a, text='Better finds for you',
               font=('Calibri bold', 25),
               fg='#007EA3',
               bg='#F0F4F7')
slogan.place(x = 195, y = 245)
home=Button(a,text="Home",
               font=("Calibri",26),
               bg = '#F0F4F7',
               fg='#007EA3',
               cursor='hand2',
               border=0,
               command=home)
home.place(x=50,y=50)
Frame(a, width=88,height=2, bg = '#007EA3').place(x = 60, y = 103)

flat_button=Button(a, text="View flats",
                   font=("Calibri",26),
                   command=vflat,
                   fg='#007EA3',
                   bg='#F0F4F7',
                   border=0,
                   cursor='hand2')
flat_button.place(x=170,y=50)
Frame(a, width=153,height=2, bg = '#007EA3').place(x = 180, y = 103)




account_button=Button(a, text="My profile",
                   font=("Calibri",26),
                   fg='#007EA3',
                   bg='#F0F4F7',
                   border=0,
                   cursor='hand2',
                   command=myacc)
account_button.place(x=360,y=50)
Frame(a, width=150,height=2, bg = '#007EA3').place(x = 368, y = 103)

welcome = Label(a, text= 'Welcome to our Apartment',
                font=('arial bold', 30),
                fg='#007EA3')
welcome.place(x = 700, y = 240)

description = Label(a, text='''Gharbeti is a user-friendly application designed to help staff members 
        become more familiar with tenant information. To ensure security, 
        staff can only access the application with a password and username. 
        Each staff member is assigned a unique ID number, which is required 
        to log into the app. Gharbeti is designed to be simple and intuitive, 
        allowing for seamless staff interaction.''',
                    font=('Arial', 15))
description.place(x = 600, y = 300)




a.mainloop()