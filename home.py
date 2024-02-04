from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
a=Tk()
a.title("GHARBETI")
a.geometry("1100x700")
a.resizable(0,0)
c = Canvas(a, height=1100, width = 700)
bgimage = PhotoImage(file='C:/Users/Dell/Desktop/files/G/Gharbeti/logo1.png')
background_label = Label(a, image=bgimage)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
c.pack()
e1=Label(a,text="Gharbeti")
e1.place(x=100,y=100)
# a.iconbitmap("a.ico")


a.mainloop()