#To create tkinter module
from tkinter import *
import sqlite3
from tkinter import messagebox
from tkinter import ttk

#To create an application window
root=Tk()
root.title("Gharbeti - Records of tenants")
root.geometry("1090x480+180+150")
root.config(bg='#007EA3')
root.resizable(0,0)
root.iconbitmap("a.ico")
#connecting to database
conn=sqlite3.connect("staff.db")
cursor=conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS tenant(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        uname   VARCHAR(40),
        em      VARCHAR(40),
        co      INT,
        ps      VARCHAR(10),
        rn     INT       
)""")
conn.commit()


font1=("Arial Italic",14)
font2=("Arial",10)


#setting function variables as global 
global add
global update
global delete

#database for rooms
def add():
    conn=sqlite3.connect("staff.db")
    c=conn.cursor()
    c.execute("INSERT INTO tenant(uname,em,co,ps,rn) VALUES(?,?,?,?,?)",
    (username.get(),email.get(),contact.get(),pms.get(),rn.get()))
    conn.commit()
    conn.close()
    username.delete(0,END)
    email.delete(0,END)
    contact.delete(0,END)
    pms.delete(0,END)
    rn.delete(0,END)
    display_data()
    messagebox.showinfo("inserted","data added successfully.")


def delete():
    conn =sqlite3.connect("staff.db")
    c=conn.cursor()
    c.execute(f"""
                DELETE FROM tenant 
                WHERE ID={update_box.get()}""",)
    conn.commit()
    conn.close()
    update_box.delete(0,END)
    display_data()
    messagebox.showinfo("Deleted","Record deleted successfully.")




#for adding more tenants into database: update button
def insert():
    if(username.get()=="" or email.get()=="" or  contact.get()=="" or pms.get()=="" or rn.get()=="" ):
        messagebox.showerror("error","Please Enter All The Data.") 
    else:
        conn=sqlite3.connect("staff.db")
        c=conn.cursor()
        c.execute(f"""
                UPDATE tenant SET 
                uname='{username.get()}',
                em='{email.get()}',
                co='{contact.get()}',
                ps='{pms.get()}',
                rn='{rn.get()}'
                WHERE ID={update_box.get()}""",)
        conn.commit()
        conn.close()
        username.delete(0,END)
        email.delete(0,END)
        contact.delete(0,END)
        pms.delete(0,END)
        rn.delete(0,END)
        update_box.delete(0,END)
        display_data()
        messagebox.showinfo("Updated","Tenant has been updated.")



#for clear button
def clear():
    username.delete(0,END)
    email.delete(0,END)
    contact.delete(0,END)
    pms.delete(0,END)
    rn.delete(0,END)

#creating functions(2) for displaying records on  treeview:fetch and display
def fetch():
    cursor.execute("SELECT * FROM tenant")
    rows=cursor.fetchall()
    return rows


def display_data():
    tv.delete(*tv.get_children())
    for row in fetch():
        tv.insert("",END,values=row)


#creating a function for fetching the data back to entry box on selecting the treeview record
def get_data(event):
    clear()
    selected_row=tv.focus()
    data=tv.item(selected_row)
    row=data["values"]
    username.insert(0,row[1])
    email.insert(0,row[2])
    contact.insert(0,row[3])
    pms.insert(0,row[4])
    rn.insert(0,row[5])

#To create labels and entry in window
label_username=Label(root,text="Name",font=font1,
                     bg='#007EA3')
label_username.place(x=0,y=90)

label_email=Label(root,text="Email",font=font1,
                  bg='#007EA3')
label_email.place(x=0,y=140)

label_contact=Label(root,text="Contact No",font=font1,
                    bg='#007EA3')
label_contact.place(x=0,y=190)

label_ps=Label(root,text="Payment\nStatus",font=font1,
               bg='#007EA3')
label_ps.place(x=0,y=240)

label_rn=Label(root,text="Room no",font=font1,
               bg='#007EA3')
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
   

btn_add=Button(root,text="Add",font=font1,command=add)
btn_add.place(x=0,y=350)

btn_retrieve=Button(root,text="update",font=font1,command=insert)
btn_retrieve.place(x=100,y=350)

btn_delete=Button(root,text="Delete",font=font1,command=delete)
btn_delete.place(x=100,y=400,height=32)

btn_clear=Button(root,text="Clear",font=font1,command=clear)
btn_clear.place(x=0,y=400)

#entry box to enter id which is to be updated or deleted
update_box=Entry(root,width=25)
update_box.place(x=180,y=400,height=30)


#adding ttk style to insert treeview
style=ttk.Style()
style.configure("mystyle.Treeview",font=font2,rowheight=50)
style.configure("mystyle.Treeview.Heading",font=font2)
style.layout("mystyle.Treeview",[('mystyle.Treevie.treearea',{'sticky':'nswe'})])

#arranging columns and heading to be shown in treeview
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

#calling function for trigger event:get_data
tv.bind("<ButtonRelease-1>",get_data)

tv.place(x=380,y=100)
  
fetch()
display_data()


root.mainloop()