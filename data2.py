from tkinter import *
import sqlite3
from tkinter import messagebox
from tkinter import ttk
root=Tk()
root.title("Gharbeti - Records of rooms")
root.geometry("1090x480+180+150")
root.config(bg='#007EA3')
root.resizable(0,0)
#connecting to database
conn=sqlite3.connect("staff.db")
cursor=conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS rooms(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        fo      INT,
        ro      INT,
        ra      INT,
        sta      VARCHAR(10)     
)""")
conn.commit()


font1=("Arial Italic",14)
font2=("Arial",10)
#setting function variables as global 
global add
global update
global delete


def add():
    conn=sqlite3.connect("staff.db")
    c=conn.cursor()
    c.execute("INSERT INTO rooms(fo,ro,ra,sta) VALUES(?,?,?,?)",
    (floorno.get(),roomno.get(),rate.get(),status.get()))
    conn.commit()
    conn.close()
    floorno.delete(0,END)
    roomno.delete(0,END)
    rate.delete(0,END)
    status.delete(0,END)
    display_data()
    messagebox.showinfo("inserted","data added successfully.")


def delete():
    conn =sqlite3.connect("staff.db")
    c=conn.cursor()
    c.execute(f"""
                DELETE FROM rooms
                WHERE ID={update_box.get()}""",)
    conn.commit()
    conn.close()
    update_box.delete(0,END)
    display_data()
    messagebox.showinfo("Deleted","Record deleted successfully.")




#for adding more tenants into database: update button
def insert():
    if(floorno.get()=="" or roomno.get()=="" or  rate.get()=="" or status.get()=="" ):
        messagebox.showerror("error","Please Enter All The Data.") 
    else:
        conn=sqlite3.connect("staff.db")
        c=conn.cursor()
        c.execute(f"""
                UPDATE rooms SET 
                fo='{floorno.get()}',
                ro='{roomno.get()}',
                ra='{rate.get()}',
                sta='{status.get()}'
                WHERE ID={update_box.get()}""",)
        conn.commit()
        conn.close()
        floorno.delete(0,END)
        roomno.delete(0,END)
        rate.delete(0,END)
        status.delete(0,END)
        update_box.delete(0,END)
        display_data()
        messagebox.showinfo("Updated","rooms has been updated.")



#for clear button
def clear():
    floorno.delete(0,END)
    roomno.delete(0,END)
    rate.delete(0,END)
    status.delete(0,END)

#creating functions(2) for displaying records on  treeview:fetch and display
def fetch():
    cursor.execute("SELECT * FROM rooms")
    rows=cursor.fetchall()
    return rows


def display_data():
    tv.delete(*tv.get_children())
    for row in fetch():
        tv.insert("",END,values=row)

#to navigate to tenants portal from rooms
def new():
    import data

#creating a function for fetching the data back to entry box on selecting the treeview record
def get_data(event):
    clear()
    selected_row=tv.focus()
    data=tv.item(selected_row)
    row=data["values"]
    floorno.insert(0,row[1])
    roomno.insert(0,row[2])
    rate.insert(0,row[3])
    status.insert(0,row[4])

label_floorno=Label(root,text="Floor no",font=font1,
                    bg='#007EA3')
label_floorno.place(x=0,y=90)

label_roomno=Label(root,text="Room no",font=font1,
                   bg='#007EA3')
label_roomno.place(x=0,y=140)

label_rate=Label(root,text="Rate(per month)",font=font1,
                 bg='#007EA3')
label_rate.place(x=0,y=190)

label_stat=Label(root,text="Status",font=font1,
                 bg='#007EA3')
label_stat.place(x=0,y=240)

floorno=Entry(root,width=30)
floorno.place(x=170,y=100,height=30)

roomno=Entry(root,width=30)
roomno.place(x=170,y=150,height=30)

rate=Entry(root,width=30)
rate.place(x=170,y=200,height=30)

status=Entry(root,width=30)
status.place(x=170,y=250,height=30)
   

btn_add=Button(root,text="Add",font=font1,command=add)
btn_add.place(x=0,y=350)

btn_retrieve=Button(root,text="update",font=font1,command=insert)
btn_retrieve.place(x=100,y=350)

btn_delete=Button(root,text="Delete",font=font1,command=delete)
btn_delete.place(x=100,y=400,height=32)

btn_clear=Button(root,text="Clear",font=font1,command=clear)
btn_clear.place(x=0,y=400)

btn_new=Button(root,text="Buy a room?",
               font=font1,
               command=new,
               bg = '#007EA3',
               fg='blue',
               cursor='hand2',
               border=0,)
btn_new.place(x=0,y=450)
frame = Frame(root, width= '110', height='2',
              bg= 'blue') 
frame.place(x = 5, y = 477)

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
tv.heading("2",text="Floor no")
tv.column("2",width=150)
tv.heading("3",text="Room no")
tv.column("3",width=200)
tv.heading("4",text="Rate(per month)")
tv.column("4",width=100)
tv.heading("5",text="Status")
tv.column("5",width=105)

#calling function for trigger event:get_data
tv.bind("<ButtonRelease-1>",get_data)

tv.place(x=380,y=100)
  
fetch()
display_data()


root.mainloop()