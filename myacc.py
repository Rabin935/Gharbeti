from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
a=Tk()
# a.iconbitmap("a.ico")
a.title("GHARBETI")
a.geometry("1100x700")
a.resizable(0,0)
c = Canvas(a, height=1100, width = 700)
bgimage = PhotoImage(file='C:/Users/Dell/Desktop/files/G/Gharbeti/logo1.png')
background_label = Label(a, image=bgimage)
background_label.place(x=0, y=30, relwidth=1, relheight=1)
c.pack()
def home():
    a.destroy()
    import home
def vflat():
    a.destroy()
    import viewflats
def ant():
    a.destroy()
    import ant
def aap():
    a.destroy()
    import aap
def myacc():
    a.destroy()
    import myacc
b1=Button(text="HOME",font=("Calibri",14),command=home)
b1.place(x=50,y=50)
b2=Button(text="VIEW FLATS",font=("Calibri",14),command=vflat)
b2.place(x=150,y=50)
b2=Button(text="ADD NEW TENANT",font=("Calibri",14),command=ant)
b2.place(x=280,y=50)
b2=Button(text="ADD A PROBLEM",font=("Calibri",14),command=aap)
b2.place(x=470,y=50)
b2=Button(text="MY ACCOUNT",font=("Calibri",14),command=myacc)
b2.place(x=650,y=50)
l=Label(a,text="this is my account",font=("Calibri",16))
l.place(x=400,y=400)



a.mainloop()