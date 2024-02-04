from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
a=Tk()
a.title("GHARBETI")
a.geometry("1100x700")
a.resizable(0,0)
c = Canvas(a, height=1100, width = 700)
bgimage = PhotoImage(file='logo1.png')
background_label = Label(a, image=bgimage)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
c.pack()
# a.iconbitmap("a.ico")


a.mainloop()