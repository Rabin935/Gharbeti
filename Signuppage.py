#To create tkinter module
from tkinter import *
from tkinter import PhotoImage
from PIL import Image, ImageTk
from tkinter import messagebox
import sqlite3

#To create an application window
a = Tk()
a.title("GHARBETI - Signup")
a.geometry('1000x600')
a.resizable(0,0)
a.iconbitmap("a.ico")

#connecting to the database
conn=sqlite3.connect("staff.db")
cursor=conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS st_records(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        fname   VARCHAR(40),
        pw     VARCHAR(40),
        em     VARCHAR(40),
        co     INT,
        a1     VARCHAR(40),
        a2     VARCHAR(40),
        a3     VARCHAR(40) 
)""")
conn.commit()



#To add background image 
c = Canvas(a, height=1100, width = 700)
bgimage = PhotoImage(file='logo1.png')
background_label = Label(a, image=bgimage)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
c.pack()

def check():
    flag=0
    if len((password1.get()))<8:
        flag+=1
        messagebox.showwarning("error","Error in password")
        if bool((email.get().endswith("@gmail.com")))==False:
            flag+=1
            messagebox.showwarning("error","Error in email")
            if bool((phone_no.get()).isdigit())==False or len((phone_no.get()))<10:
                flag+=1
                messagebox.showwarning("error","Error in phone number")
    if flag>=1:
        messagebox.showerror("error","error in details")
    else:
        messagebox.showinfo("SUCCESS","Account created successfully.")
        v1=fullname.get()
        v2=password1.get()
        v3=email.get()
        v4=phone_no.get()
        a.destroy()
        import forgetps
        cursor.execute("INSERT INTO st_records(fname,pw,em,co,a1,a2,a3) VALUES(?,?,?,?,?,?,?)",
        (v1,v2,v3,v4,forgetps.v5,forgetps.v6,forgetps.v7))
        conn.commit()
        conn.close()
        import home
        
        
      
#function in commands onclikcing navigation buttons
def signup():
    a.destroy()
    import gblogin
    
#setting function variables as global 
global fullname
global password1
global email
global phone_no


frame = Frame(a, width= '400', height='500', bg= '#F0F4F7') 
frame.place(x = 560, y = 50)



sign_up = Label(a, text="Sign Up", font=("Calibri", 40),
                bg = "#F0F4F7")
sign_up.place(x = 170, y = 100)
detail = Label(a, text="Enter Your Detail",
               font=("Calibri", 22),
               fg='#007EA3',
               bg= "#F0F4F7")
detail.place(x = 690, y = 60)

def on_enter(e):
    fullname.delete(0, 'end')
    
def on_leave(e):
    name = fullname.get()
    if name == '':
        fullname.insert(0, 'Enter your Full name')




fullname=Entry(a,width=32,
         font=("Calibri",11),
         fg = '#007EA3',
         bg = '#F0F4F7',
         border=0)
fullname.place(x=650,y=130, height=30)
fullname.insert(0, 'Enter your Full name')
fullname.bind('<FocusIn>', on_enter)
fullname.bind('<FocusOut>', on_leave)

Frame(a, width=270,bg = '#007EA3').place(x = 650, y = 155)


def on_enter(e):
    password1.delete(0, 'end')
    
def on_leave(e):
    name = password1.get()
    if name == '':
        password1.insert(0, 'Enter your password')

password1=Entry(a,width=32,
         font=("Calibri",11),
         fg = '#007EA3',
         bg = '#F0F4F7',
         border=0)
password1.place(x=650,y=180, height=30)
password1.insert(0, 'Pasword')
password1.bind('<FocusIn>', on_enter)
password1.bind('<FocusOut>', on_leave)

Frame(a, width=270,bg = '#007EA3').place(x = 650, y = 205)

def on_enter(e):
    email.delete(0, 'end')
    
def on_leave(e):
    name = email.get()
    if name == '':
        email.insert(0, 'Enter your Email')
        
email=Entry(a,width=32,
         font=("Calibri",11),
         fg = '#007EA3',
         bg = '#F0F4F7',
         border=0)
email.place(x=650,y=230, height=30)
email.insert(0, 'Enter your Email')
email.bind('<FocusIn>', on_enter)
email.bind('<FocusOut>', on_leave)

Frame(a, width=270,bg = '#007EA3').place(x = 650, y = 255)

def on_enter(e):
    if phone_no.get() == 'Enter your phone no':
        phone_no.delete(0, 'end')
    
def on_leave(e):
    if phone_no.get() == '':
        phone_no.insert(0, 'Enter your phone no')

phone_no=Entry(a,width=32, 
         font=("Calibri",11),
         fg = '#007EA3',
         bg = '#F0F4F7',
         border=0)
phone_no.place(x=650,y=280, height=30)
phone_no.insert(0, 'Enter your phone no')

phone_no.bind('<FocusIn>', on_enter)
phone_no.bind('<FocusOut>', on_leave)

Frame(a, width=270,bg = '#007EA3').place(x = 650, y = 305)


c1=IntVar()
c2=IntVar()
c3=IntVar()
gn1 = Radiobutton(a, text = 'Female',
                  variable=c1,
                  fg="#007EA3",
                  bg= '#F0F4F7',value=1)
gn1.place(x = 650, y = 335)

gn2 = Radiobutton(a, text = 'Male',
                  variable=c1,
                  fg="#007EA3",
                  bg="#F0F4F7",value=2)
gn2.place(x = 720, y = 335)

gn3 = Radiobutton(a, text = 'Others',
                  variable=c1,
                  fg="#007EA3",
                  bg="#F0F4F7",value=3)
gn3.place(x = 790, y = 335)


sign = Button(a, text="Sign up",
              font=("Arial Bold", 20),
              bg='#82A6B4',
              fg='#F0F4F7',
              command=check)
sign.place(x = 680, y = 370)
acc = Label(a, text="Already have an account?",
            font = ("Arial Bold", 8),
            bg = "#F0F4F7")
acc.place(x = 650, y = 435)
log_in=Button(a,text="LOG IN",
               font=("Calibri",11),
               bg = '#F0F4F7',
               fg='blue',
               cursor='hand2',
               border=0,
               command=signup)
log_in.place(x=800,y=430)


a.mainloop()