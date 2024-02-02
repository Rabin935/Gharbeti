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
Addaprob=Button(a,text="Add a problem",command=addaprob).place(x=220,y=25)
Myaccount=Button(a,text="My Account",command=myacc).place(x=330,y=25)
Label(text="this is viewflats page")
a.mainloop()