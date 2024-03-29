#To create tkinter module
from tkinter import *

root=Tk()
root.title("Records of tenants")
root.geometry("1300x650+0+0")
root.config(bg="#F0F4F7")


#To create an application window
root.config(bg = '#F0F4F7')
c = Canvas(root, height=1100, width = 700)
bgimage = PhotoImage(file=r'C:\Users\ACER\OneDrive\Desktop\New folder\New folder\project\Gharbeti\img\background.png')
background_label = Label(root, image=bgimage)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
c.pack()
root.iconbitmap("C:/Users/ACER/OneDrive/Desktop/New folder/New folder/project/Gharbeti/a.ico")





#function in commands onclikcing navigation buttons
def func():
    import data 
def func2():
    import data2
def home():
    root.destroy()
    import home
def vflat():
    root.destroy()
    import viewflats
def myacc():
    # a.destroy()
    import myacc

#placing buttons to navigate through the program
home=Button(root,text="Home",
        font=("Calibri",26),
        bg = '#F0F4F7',
        fg='#007EA3',
        cursor='hand2',
        border=0,
        command=home)
home.place(x=50,y=50)
Frame(root, width=88,height=2, bg = '#007EA3').place(x = 60, y = 103)


flat_button=Button(root, text="View flats",
                font=("Calibri",26),
                command=vflat,
                fg='#007EA3',
                bg='#F0F4F7',
                border=0,
                cursor='hand2')
flat_button.place(x=170,y=50)
Frame(root, width=153,height=2, bg = '#007EA3').place(x = 180, y = 103)

flat_button=Button(root, text="Rooms",
                font=("Calibri",20),
                command=func2,
                fg='#007EA3',
                bg='#DDEEF7',
                border=0,
                cursor='hand2')
flat_button.place(x=50,y=180)
Frame(root, width=153,height=2, bg = '#007EA3').place(x = 180, y = 103)

flat_button=Button(root, text="Tenants",
                font=("Calibri",20),
                command=func,
                fg='#007EA3',
                bg='#DDEEF7',
                border=0,
                cursor='hand2')
flat_button.place(x=50,y=230)
Frame(root, width=153,height=2, bg = '#007EA3').place(x = 180, y = 103)

account_button=Button(root, text="My profile",
                   font=("Calibri",26),
                   fg='#007EA3',
                   bg='#F0F4F7',
                   border=0,
                   cursor='hand2',
                   command=myacc)
account_button.place(x=360,y=50)
Frame(root, width=150,height=2, bg = '#007EA3').place(x = 368, y = 103)

root.mainloop()
