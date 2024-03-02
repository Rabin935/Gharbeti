#To create tkinter module
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import sqlite3

#To create an application window
a=Tk()
a.title("GHARBETI") 
a.geometry('1000x600')
a.resizable(0,0)
c = Canvas(a, height=1100, width = 700)
bgimage = PhotoImage(file='logo1.png')
background_label = Label(a, image=bgimage)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
c.pack()
a.iconbitmap("a.ico")

conn=sqlite3.connect("staff.db")
cursor=conn.cursor()

def home():
    conn=sqlite3.connect("staff.db")
    cursor=conn.cursor()
    global k
    k = id_no.get()
    p = password.get()
    cursor.execute("SELECT * FROM st_records WHERE fname=? AND pw=?", (k, p))
    record = cursor.fetchone()
    if record:
        a.destroy()
        import home
    else:
        messagebox.showerror("error","invalid details")

#show or hide password option 
def add():
    if chk.get()==1:
        password.config(show="")
    else:
        password.config(show='*')

#on hitting signup button:connecting to signuppage
def signup():
    a.destroy()
    import Signuppage   

def forget():
    a.destroy()
    import pwreset


frame = Frame(a, width= '400', height='500',
              bg= '#F0F4F7') 
frame.place(x = 560, y = 50)

l=Label(a,text="Sign In",
        font=("Calibri", 28), 
        fg='#007EA3',
        bg = "#F0F4F7")
l.place(x=690,y=100)

def on_enter(e):
    id_no.delete(0, 'end')
    
def on_leave(e):
    name = id_no.get()
    if name == '':
        id_no.insert(0, 'Username')
    
id_no=Entry(a,width=32,
         font=("Calibri",11),
         fg = '#007EA3',
         bg = '#F0F4F7',
         border=0)
id_no.place(x=600,y=220, height=30)
id_no.insert(0, 'Username')
id_no.bind('<FocusIn>', on_enter)
id_no.bind('<FocusOut>', on_leave)

Frame(a, width=300,bg = '#007EA3').place(x = 600, y = 250)

def on_enter(e):
    password.delete(0, 'end')
    
def on_leave(e):
    name = password.get()
    if name == '':
        password.insert(0, 'Password')
    
password=Entry(a,width=32,
         font=("Calibri",11),
         fg = '#007EA3',
         bg = '#F0F4F7',
         border=0)
password.place(x=600,y=280, height=30)
password.insert(0, 'Password')
password.bind('<FocusIn>', on_enter)
password.bind('<FocusOut>', on_leave)

Frame(a, width=300,bg = '#007EA3').place(x = 600, y = 310)

#for checkbutton of show password 
chk=IntVar()
Checkbutton(a,variable=chk,
            bg = "#F0F4F7",command=add).place(x= 715,y=330)
Label(a,text="Show password",
      font=("Calibri",12),
      bg = "#F0F4F7",
      fg='#007EA3').place(x=735,y=330)

#for signin button
sign_in=Button(a, text='Sign in',
               width=20,
               font=("Arial Bold",16),
               bg= "#82A6B4",
               border=0,
               fg='#F0F4F7',
               command=home).place(x=640,y=380, height=40)
forget=Button(text="Forgot password?",
              font=("Calibri",11),
              fg= 'blue',
              cursor='hand2',
              border=0,
              bg= '#F0F4F7',
              command=forget).place(x=794,y=425)
Label(a,text="Don't have an account?",
      font=("Calibri",10),
      bg = "#F0F4F7").place(x=650,y=468)
sign_up=Button(a,text="SIGN UP",
               font=("Calibri",11),
               bg = '#F0F4F7',
               fg='blue',
               cursor='hand2',
               border=0,
               command=signup)
sign_up.place(x=780,y=465)
a.mainloop()