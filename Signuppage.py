from tkinter import *
from tkinter import PhotoImage
from PIL import Image, ImageTk
from tkinter import messagebox
a = Tk()
a.geometry('1100x700')
a.iconbitmap("a.ico")
c = Canvas(a, height=1100, width = 700)
bgimage = PhotoImage(file='logo1.png')
background_label = Label(a, image=bgimage)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
c.pack()
global flag
def check():
    flag=0
    if len((ps1.get()))<8:
        flag+=1
        messagebox.showwarning("error","Error in password")
        if bool((em1.get().endswith("@gmail.com")))==False:
            flag+=1
            messagebox.showwarning("error","Error in email")
            if bool((ph1.get()).isdigit)==False or len((ph1.get()))<10:
                flag+=1
                messagebox.showwarning("error","Error in phone number")
    if flag>=1:
        messagebox.showerror("error","error in details")
    else:
        messagebox.showinfo("SUCCESS","Account created successfully.")
        a.destroy()
        import home              
def signup():
    a.destroy()
    import gblogin
sign_up = Label(a, text="Sign Up", font=("Arial Bold", 50),
                bg = "#86A4BF")
sign_up.place(x = 0, y = 5)
detail = Label(a, text="Enter Your Detail", font=("Arial Bold", 22),
               bg= "#C0C9D1")
detail.place(x = 725, y = 60)
fn = Label(a, text="Full name", font= ("Arial Bold", 20),
           bg = '#C0C9D1')
fn.place(x = 650, y = 130)
ps = Label(a, text="Password", font= ("Arial Bold", 20),
           bg = '#C0C9D1')
ps.place(x = 650, y = 210)
em = Label(a, text="Email", font= ("Arial Bold", 20),
           bg = '#C0C9D1')
em.place(x = 650, y = 290)
pno = Label(a, text="Phone no. ", font= ("Arial Bold", 20),
            bg = '#C0C9D1')
pno.place(x = 650, y = 380)
gn = Label(a, text="Gender ", font= ("Arial Bold", 20),
           bg = '#C0C9D1')
gn.place(x = 650, y = 465)
name1 = Entry(a, width=35)
name1.place(x = 805, y = 130, height=30)
ps1 = Entry(a, width=35)
ps1.place(x = 805, y = 210, height=30)
em1 = Entry(a, width=35)
em1.place(x = 805, y = 290, height=30)
ph1 = Entry(a, width=35)
ph1.place(x = 805, y = 380, height=30)
c1=IntVar()
c2=IntVar()
c3=IntVar()
gn1 = Checkbutton(a, text = 'Female',variable=c1,
                  bg= '#C0C9D1')
gn1 = Radiobutton(a, text = 'Female',variable=c1,
                  bg= '#C0C9D1',value=1)
gn1.place(x = 805, y = 470)
gn2 = Checkbutton(a, text = 'Male',variable=c2,
                  bg="#C0C9D1")
gn2 = Radiobutton(a, text = 'Male',variable=c1,
                  bg="#C0C9D1",value=2)
gn2.place(x = 885, y = 470)
gn3 = Checkbutton(a, text = 'Others',variable=c3,
                  bg="#C0C9D1")
gn3 = Radiobutton(a, text = 'Others',variable=c1,
                  bg="#C0C9D1",value=3)
gn3.place(x = 945, y = 470)
sign = Button(a, text="Sign up", font=("Arial Bold", 20))
sign = Button(a, text="Sign up", font=("Arial Bold", 20),command=check)
sign.place(x = 820, y = 525)
acc = Label(a, text="Already have an account?",
            font = ("Arial Bold", 8),
            bg = "#C0C9D1")
acc.place(x = 760, y = 585)
log = Button(a, text="Log in",
             font = ("Arial Bold", 8),
             bg = "white",
             command=signup)
log.place(x = 910, y = 585)
a.mainloop()