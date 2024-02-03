from tkinter import *
from tkinter import PhotoImage
from PIL import ImageTk, Image
from tkinter import messagebox
a = Tk()
a.geometry('1100x700')
c = Canvas(a, height=1100, width = 700)
bgimage = PhotoImage(file='logo1.png')
background_label = Label(a, image=bgimage)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
c.pack()




sign_up = Label(a, text="Sign Up", font=("Arial Bold", 50),
                bg = "#86A4BF")
sign_up.place(x = 0, y = 5)




fn = Label(a, text="Full name", font= ("Arial Bold", 20),
           bg = '#86A4BF')
fn.place(x = 500, y = 100)
ps = Label(a, text="Password", font= ("Arial Bold", 20),
           bg = '#86A4BF')
ps.place(x = 500, y = 180)
em = Label(a, text="Email", font= ("Arial Bold", 20),
           bg = '#86A4BF')
em.place(x = 500, y = 260)
pno = Label(a, text="Phone no. ", font= ("Arial Bold", 20),
            bg = '#86A4BF')
pno.place(x = 500, y = 340)
gn = Label(a, text="Gender ", font= ("Arial Bold", 20),
           bg = '#86A4BF')
gn.place(x = 500, y = 420)


name1 = Entry(a, width=35)
name1.place(x = 700, y = 100, height=30)
ps1 = Entry(a, width=35)
ps1.place(x = 700, y = 180, height=30)
em1 = Entry(a, width=35)
em1.place(x = 700, y = 260, height=30)
ph1 = Entry(a, width=35)
ph1.place(x = 700, y = 340, height=30)

c1=IntVar()
c2=IntVar()
c3=IntVar()
gn1 = Checkbutton(a, text = 'Female',variable=c1,
                  bg= '#86A4BF')
gn1.place(x = 700, y = 425)
gn2 = Checkbutton(a, text = 'Male',variable=c2,
                  bg="#86A4BF")
gn2.place(x = 770, y = 425)
gn3 = Checkbutton(a, text = 'Others',variable=c3,
                  bg="#86A4BF")
gn3.place(x = 840, y = 425)

sign = Button(a, text="Sign up", font=("Arial Bold", 20))
sign.place(x = 700, y = 480)

acc = Label(a, text="Already have an account?",
            font = ("Arial Bold", 8),
            bg = "#86A4BF")
acc.place(x = 700, y = 530)
log = Button(a, text="Log in",
             font = ("Arial Bold", 8),
             bg = "#86A4BF")
log.place(x = 845, y = 530)

a.mainloop()