from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
a=Tk()
a.title("GHARBETI")
a.geometry("1100x700")
a.config(bg="#86A4BF")
a.iconbitmap("a.ico")
def mess():
    # k=e1.get()
    # p=e2.get()
    # m=e3.get()
    # if k.isdigit() and p.endswith("@gmai.com") and len(m)>8:
    #     messagebox.showinfo("success","logged in successfully.")
    # else:
    #     messagebox.showerror("error","invalid details")
    if e1.get() and e2.get() and e3.get():
        messagebox.showinfo("Success","Logged in successfully.")
    else:
        messagebox.showerror("Error","Please input valid details.")
l=Label(a,text="Enter your details",font=("Arial Bold",28)).place(x=830,y=150)
l1=Label(a,text="Id no :",font=("Arial Bold",16)).place(x=825,y=220)
e1=Entry(a,width=20,font=("Arial Bold",14)).place(x=950,y=220)
l2=Label(a,text="Email :",font=("Arial Bold",16)).place(x=825,y=290)
e2=Entry(a,width=20,font=("Arial Bold",14)).place(x=950,y=290)
l3=Label(a,text="Password :",font=("Arial Bold",16)).place(x=825,y=350)
e3=Entry(a,width=20,font=("Arial Bold",14)).place(x=950,y=350)
chk=IntVar()
Checkbutton(a,variable=chk).place(x=960,y=400)
Label(a,text="Remember me",font=("Arial Bold",12)).place(x=990,y=400)
b1=Button(text='Login',font=("Arial Bold",16),command=mess).place(x=1000,y=450)
Label(a,text="Forgot password",font=("Arial Bold",8)).place(x=1000,y=500)
Label(a,text="Don't have an account? SIGN UP?",font=("Arial Bold",10)).place(x=950,y=600)
my=ImageTk.PhotoImage(Image.open("C:/Users/Dell/Desktop/files/gharbeti/gb.jpg"))
image_label = Label( image=my,height=200,width=100)
image_label.place(x=150,y=150)
Label(a,text="How to use?",font=("Arial Bold",10)).place(x=150,y=590)
a.mainloop()