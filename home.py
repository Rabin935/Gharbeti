from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
a=Tk()
a.title("GHARBETI")
a.geometry("1100x700")
a.resizable(0,0)
c = Canvas(a, height=1100, width = 700)
bgimage = PhotoImage(file='D:/python/project/Gharbeti/logo1.png')
background_label = Label(a, image=bgimage)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
c.pack()
e1=Label(a,text="Gharbeti")
e1.place(x=100,y=100)
e2=Label(a,text="aagya")
e2.place(x=150,y=200)
e3=Label(a,text="dipen lama added")
e3.place(x=200,y=200)
# a.iconbitmap("a.ico")


a.mainloop()