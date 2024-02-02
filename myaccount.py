from tkinter import *
from PIL import ImageTk, Image
a=Tk()
a.geometry('700x700')
def home():
    a.destroy()
    import gbhome
def viewflats():
    a.destroy
    import gbviewflats
def addaprob():
    a.destroy
    import gbaddaprob
def myacc():
    a.destory()
    import myaccount
Home=Button(a,text="Home",command=home).place(x=67,y=25)
ViewFlats=Button(a,text="View Flats",command=viewflats).place(x=138,y=25)
Addaprob=Button(a,text="Add a problem").place(x=220,y=25)
Myaccount=Button(a,text="My Account").place(x=330,y=25)
my=ImageTk.PhotoImage(Image.open("C:/Users/Dell/Desktop/files/gharbeti/download.png"))
image_label = Label( image=my,height=200,width=100)
image_label.place(x=330,y=216)
Label(text="ID no").place(x=330,y=420)
Label(text="name of staff").place(x=330,y=440)
Label(text="email").place(x=330,y=460)
Label(text="contact").place(x=330,y=480)
logout=Button(a,text="LOGOUT").place(x=330,y=500)


a.mainloop()