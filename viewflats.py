from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
a=Tk()
a.iconbitmap("a.ico")
a.title("GHARBETI - viewflats")
a.geometry("1600x950")
a.resizable(0,0)
c = Canvas(a, height=1100, width = 700)
bgimage = PhotoImage(file='img/homepic.png')
background_label = Label(a, image=bgimage)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
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
home=Button(a,text="Home",
               font=("Calibri",26),
               bg = '#F0F4F7',
               fg='#007EA3',
               cursor='hand2',
               border=0,
               command=home)
home.place(x=50,y=50)
Frame(a, width=88,height=2, bg = '#007EA3').place(x = 60, y = 103)

tenant_button=Button(a, text="Add new tenants",
                   font=("Calibri",26),
                   fg='#007EA3',
                   bg='#F0F4F7',
                   border=0,
                   cursor='hand2',command=ant)
tenant_button.place(x=180,y=50)
Frame(a, width=245,height=2, bg = '#007EA3').place(x = 187, y = 103)

# problem_buuton=Button(a, text="Add a problem",
#                    font=("Calibri",26),
#                    fg='#007EA3',
#                    bg='#F0F4F7',
#                    border=0,
#                    cursor='hand2',
#                    command=aap)
# problem_buuton.place(x=650,y=50)
# Frame(a, width=215,height=2, bg = '#007EA3').place(x = 657, y = 103)

# l=Label(a,text="this is view flats",font=("Calibri",16))
# l.place(x=400,y=400)



a.mainloop()