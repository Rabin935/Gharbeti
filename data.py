from tkinter import *
import sqlite3
from tkinter import messagebox
from tkinter import ttk
root=Tk()
root.title("Records of tenants")
root.geometry("1090x480+180+150")
#connecting to database
conn=sqlite3.connect("rooms.db")
cursor=conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS tenant(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        uname   TEXT,
        em      TEXT,
        ps      TEXT,
        co     INT,
        rn     INT       
)""")
conn.commit()


font1=("Arial Italic",14)
font2=("Arial",10)
#setting function variables as global 
global add
global update
global delete

frame = Frame(root, width= '400', height='500',
        bg= '#F0F4F7') 
frame.place(x = 560, y = 50)

def add():
    conn=sqlite3.connect("rooms.db")
    c=conn.cursor()
    c.execute("INSERT INTO tenant(uname,em,ps,co,rn) VALUES(?,?,?,?,?)",
    (username.get(),email.get(),contact.get(),pms.get(),rn.get()))
    conn.commit()
    conn.close()
    username.delete(0,END)
    email.delete(0,END)
    contact.delete(0,END)
    pms.delete(0,END)
    rn.delete(0,END)


def delete():
    conn =sqlite3.connect("rooms.db")
    c=conn.cursor()
    c.execute("DELETE from ")
    username.delete(0,END)
    email.delete(0,END)
    contact.delete(0,END)
    pms.delete(0,END)
    rn.delete(0,END)


def update():
    conn=sqlite3.connect("rooms.db")
    c=conn.cursor()
    c.execute("""
            UPDATE tenant SET 
            uname=:u,
            em=:a,
            co=:r,
            ps=:p,
            rn=:s
            WHERE ID=:id""",
            {
                'u':username.get(),
                "a":email.get(),
                'r':contact.get(),
                'p':pms.get(),
                's':rn.get()
            }
    )
    conn.commit()

#for inserting into database:add btn
def insert():
    if(username.get()=="" or email.get()=="" or  contact.get()=="" or pms.get()=="" or rn.get()=="" ):
        messagebox.showerror("error","Please Enter All The Data.") 
    # elif(not(username.get()).isalpha and (email.get()).endswith("@gmail.com") and (len(str(contact.get())))>10 and ((pms.get()).upper=="PAID" or (pms.get()).upper=="UNPAID") and (type(rn.get())==int) ):
    #     messagebox.showerror("Error","Invalid Details") 
    else:
        c=conn.cursor()
        cursor.execute('SELECT max(id) FROM tenant')
        max_id =int(c.lastrowid)
        details=[max_id+1,(username.get()),email.get(),contact.get(),pms.get(),rn.get()]
        cursor.execute("INSERT INTO tenant values(?,?,?,?,?,?)",+details)
        conn.commit()
        messagebox.showinfo("Inserted","Tenant has been inserted.")



#for clear button
def clear():
    username.delete(0,END)
    email.delete(0,END)
    contact.delete(0,END)
    pms.delete(0,END)
    rn.delete(0,END)

#creating functions for treeview
def fetch():
    cursor.execute("SELECT * FROM tenant")
    rows=cursor.fetchall()
    return rows

def display_data():
    tv.delete(*tv.get_children())
    for row in fetch():
        tv.insert("",END,values=row)

label_username=Label(root,text="Name",font=font1)
label_username.place(x=0,y=90)

label_email=Label(root,text="Email",font=font1)
label_email.place(x=0,y=140)

label_contact=Label(root,text="Contact No",font=font1)
label_contact.place(x=0,y=190)

label_ps=Label(root,text="Payment\nStatus",font=font1)
label_ps.place(x=0,y=240)

label_rn=Label(root,text="Room no",font=font1)
label_rn.place(x=0,y=310)

username=Entry(root,width=30)
username.place(x=170,y=100,height=30)

email=Entry(root,width=30)
email.place(x=170,y=150,height=30)

contact=Entry(root,width=30)
contact.place(x=170,y=200,height=30)

pms=Entry(root,width=30)
pms.place(x=170,y=250,height=30)
    
rn=Entry(root,width=30)
rn.place(x=170,y=310,height=30)
   

btn_add=Button(root,text="Add",font=font1,command=insert)
btn_add.place(x=0,y=350)

btn_retrieve=Button(root,text="update",font=font1,command=update)
btn_retrieve.place(x=100,y=350)

btn_delete=Button(root,text="Delete",font=font1,command=delete)
btn_delete.place(x=100,y=400,height=32)

btn_clear=Button(root,text="Clear",font=font1,command=clear)
btn_clear.place(x=0,y=400)
update_box=Entry(root,width=25)
update_box.place(x=180,y=400,height=30)

style=ttk.Style()
style.configure("mystyle.Treeview",font=font2,rowheight=50)
style.configure("mystyle.Treeview.Heading",font=font2)
style.layout("mystyle.Treeview",[('mystyle.Treevie.treearea',{'sticky':'nswe'})])

tv=ttk.Treeview(root,columns=(1,2,3,4,5,6),show="headings",style="mystyle.Treeview")
tv.heading("1",text="ID")
tv.column("1",width=50)
tv.heading("2",text="Name")
tv.column("2",width=150)
tv.heading("3",text="Email")
tv.column("3",width=200)
tv.heading("4",text="Contact")
tv.column("4",width=100)
tv.heading("5",text="Status")
tv.column("5",width=105)
tv.heading("6",text="Room no")
tv.column("6",width=105)
tv.place(x=380,y=100)
  
fetch()
display_data()


root.mainloop()