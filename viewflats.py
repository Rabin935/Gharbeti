from tkinter import *

root=Tk()
root.title("Records of tenants")
root.geometry("1550x800+0+0")


#function in commands onclikcing navigation buttons
def func():
    root.destroy
    import data 
def home():
    root.destroy()
    import home
def vflat():
    root.destroy()
    import viewflats

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
                command=func,
                fg='#007EA3',
                bg='#F0F4F7',
                border=0,
                cursor='hand2')
flat_button.place(x=50,y=150)
Frame(root, width=153,height=2, bg = '#007EA3').place(x = 180, y = 103)

flat_button=Button(root, text="Tenants",
                font=("Calibri",20),
                command=func,
                fg='#007EA3',
                bg='#F0F4F7',
                border=0,
                cursor='hand2')
flat_button.place(x=50,y=200)
Frame(root, width=153,height=2, bg = '#007EA3').place(x = 180, y = 103)


        
root.mainloop()
