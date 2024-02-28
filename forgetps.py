from tkinter import *

a = Tk()
a.title("GHARBETI") 
a.geometry('450x600')
a.resizable(0,0)


def confirm():
    a.destroy()
    import home
    




#frame for reset security question
Frame(a, width=600,height=100, bg = '#007EA3').place(x = 0, y = 0)

headline = Label(a, text='Reset Security Question',
                 font=('Ariel', 20),
                 fg="#F0F4F7",
                 bg = '#007EA3')
headline.place(x = 80, y = 25)

security = Label(a, text='Fill up the details below for the security purpose.',
                 font=('Calibri', 15))
security.place(x = 10, y = 110)

#question and answer no 1
question1 = Label(a, text='1.   What is your favourite food?',
                  font=('Calibri', 15))
question1.place(x = 10, y =160)

def on_enter(e):
    ans1.delete(0, 'end')
    
def on_leave(e):
    name = ans1.get()
    if name == '':
        ans1.insert(0, 'Enter your answer')
        
ans1=Entry(a,width=32,
         font=("Calibri",15),
         bg = '#F0F4F7',
         border=0)
ans1.place(x=40,y=190, height=30)
ans1.insert(0, 'Enter your answer')
ans1.bind('<FocusIn>', on_enter)
ans1.bind('<FocusOut>', on_leave)

Frame(a, width=270,bg = 'black').place(x = 40, y = 220)


#question and answer no 2
question2 = Label(a, text='2.   Which is the middle school you graduate from?',
                  font=('Calibri', 15))
question2.place(x = 10, y =260)

def on_enter(e):
    ans2.delete(0, 'end')
    
def on_leave(e):
    name = ans2.get()
    if name == '':
        ans2.insert(0, 'Enter your answer')
        
ans2=Entry(a,width=32,
         font=("Calibri",15),
         bg = '#F0F4F7',
         border=0)
ans2.place(x=40,y=290, height=30)
ans2.insert(0, 'Enter your answer')
ans2.bind('<FocusIn>', on_enter)
ans2.bind('<FocusOut>', on_leave)

Frame(a, width=270, bg= 'black').place(x = 40, y = 320)


#question and answer no 3
question3 = Label(a, text='3.   Write a name of the city you grew up.',
                  font=('Calibri', 15))
question3.place(x = 10, y =360)


def on_enter(e):
    ans3.delete(0, 'end')
    
def on_leave(e):
    name = ans3.get()
    if name == '':
        ans3.insert(0, 'Enter your answer')
        
ans3=Entry(a,width=32,
         font=("Calibri",15),
         bg = '#F0F4F7',
         border=0)
ans3.place(x=40,y=390, height=30)
ans3.insert(0, 'Enter your answer')
ans3.bind('<FocusIn>', on_enter)
ans3.bind('<FocusOut>', on_leave)

Frame(a, width=270,bg = 'black').place(x = 40, y = 420)

#confirm button
confirm = Button(a, text='Confirm',
                 font=('Calibri', 20),
                 bg='#007EA3',
                 fg='#F0F4F7',
                 command=confirm)
confirm.place(x = 150, y = 470)



a.mainloop()