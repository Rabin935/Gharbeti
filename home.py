from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
a=Tk()
a.title("GHARBETI")
a.geometry("1100x700")
a.resizable(0,0)
c = Canvas(a, height=1100, width = 700)
bgimage = PhotoImage(file='C:/Users/Dell/Desktop/files/gharbeti/logo1.png')
background_label = Label(a, image=bgimage)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
c.pack()



# a.iconbitmap("a.ico")
def home():
    k=e1.get()
    p=e2.get()
    if k.isdigit() and len(p)>8:
        # a.destroy()
        # import home
        messagebox.showinfo("success","logged in successfully.")
    else:
        messagebox.showerror("error","invalid details")
def signup():
    a.destroy()
    import Signuppage    
l=Label(a,text="Enter your details",font=("Arial Bold", 28), 
        bg = "#86A4BF")
l.place(x=700,y=150)

l1=Label(a,text="Id no :",font=("Arial Bold",20),
         bg = "#86A4BF")
l1.place(x=650,y=220)

e1=Entry(a,width=20,font=("Arial Bold",14))
e1.place(x=805,y=220, height=30)

l2=Label(a,text="Password :",font=("Arial Bold",20),
         bg = "#86A4BF")
l2.place(x=650,y=290)

e2=Entry(a,width=20,font=("Arial Bold",14))
e2.place(x=805,y=290, height=30)

chk=IntVar()
Checkbutton(a,variable=chk,
            bg = "#86A4BF").place(x=830,y=400)
Label(a,text="Remember me",font=("Arial Bold",12), bg = "#86A4BF").place(x=850,y=400)

b1=Button(text='Login',font=("Arial Bold",16),command=home).place(x=860,y=450)

b2=Button(text="Forgot password",font=("Arial Bold",8)).place(x=860,y=500)

Label(a,text="Don't have an account?",
      font=("Arial Bold",10),
      bg = "#86A4BF").place(x=800,y=600)
b3=Button(text="SIGN UP",font=("Arial Bold",8),command=signup)
b3.place(x=960,y=600)

a.mainloop()