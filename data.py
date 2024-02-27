from tkinter import *
import sqlite3

class dbtable:
    def __init__(self,root):
        self.root=root
        self.root.title("Records of tenants")
        self.root.geometry("700x480+280+150")

        #connecting to database
        conn=sqlite3.connect("tenant.db")
        cursor=conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS tenant(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                uname   TEXT,
                em     TEXT,
                ps      TEXT,
                co     INT,
                rn     INT
        )""")
        conn.commit()
        conn.close()

        #setting function variables as global 
        global add
        global update
        global delete


        def add():
            conn=sqlite3.connect("tenant.db")
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

        def delete():
            conn=sqlite3.connect("tenant.db")
            c=conn.cursor()
            c.execute("DELETE from ")
            username.delete(0,END)
            email.delete(0,END)
            contact.delete(0,END)
            pms.delete(0,END)
            rn.delete(0,END)

       

        def edit():
            global editor
            editor=Tk()
            editor.title("Update Data")
            editor.geometry("300x480")
            conn=sqlite3.connect("gender_database.db")
            c=conn.cursor()
            record_id=update_box.get()
            c.execute("SELECT * FROM employee WHERE ID=?",(record_id,))
            records=c.fetchall()

            global username_editor
            global address_editor
            global role_editor
            global salary_editor

            username_editor=Entry(editor,width=30)
            username_editor.grid(row=0, column=1,padx=20,pady=(10,0))

            address_editor=Entry(editor,width=30) 
            address_editor.grid(row=1,column=1)

            role_editor=Entry(editor,width=30)
            role_editor.grid(row=2,column=1)

            salary_editor=Entry(editor,width=30)
            salary_editor.grid(row=3,column=1)

            username_label=Label(editor,text="username")
            username_label.grid(row=0,column=0,pady=(10,0))

            address_label=Label(editor,text="address")
            address_label.grid(row=1,column=0)

            role_label=Label(editor,text="role")
            role_label.grid(row=2,column=0)

            salary_label=Label(editor,text="salary")
            salary_label.grid(row=3,column=0)
            for record in records:
                username_editor.insert(0,record[1])
                address_editor.insert(0,record[2])
                role_editor.insert(0,record[3])
                salary_editor.insert(0,record[4])
            update_box.delete(0,END)
            edit_btn=Button(editor,text="SAVE",command=lambda:update(record_id))
            edit_btn.grid(row=6,column=0,columnspan=2,pady=10,ipadx=125)


        def update(record_id):
            conn=sqlite3.connect("gender_database.db")
            c=conn.cursor()
            c.execute("""
                    UPDATE employee SET 
                    uname=:u,
                    adr=:a,
                    rl=:r,
                    slr=:s
                    WHERE ID=:id""",
                    {
                        'u': username_editor.get(),
                        "a":address_editor.get(),
                        'r':role_editor.get(),
                        's':salary_editor.get(),
                        'id':record_id
                    }
            )
            conn.commit()
            conn.close()
            editor.destroy()

        label_username=Label(self.root,text="Name",font=("Arial Bold",18))
        label_username.place(x=0,y=90)

        label_email=Label(self.root,text="Email",font=("Arial Bold",18))
        label_email.place(x=0,y=140)

        label_contact=Label(self.root,text="Contact No",font=("Arial Bold",18))
        label_contact.place(x=0,y=190)

        label_ps=Label(self.root,text="Payment\nStatus",font=("Arial Bold",18))
        label_ps.place(x=0,y=240)

        label_rn=Label(self.root,text="Room no",font=("Arial Bold",18))
        label_rn.place(x=0,y=310)

        username=Entry(self.root,width=30)
        username.place(x=170,y=100,height=30)

        email=Entry(self.root,width=30)
        email.place(x=170,y=150,height=30)

        contact=Entry(self.root,width=30)
        contact.place(x=170,y=200,height=30)

        pms=Entry(self.root,width=30)
        pms.place(x=170,y=250,height=30)
            
        rn=Entry(self.root,width=30)
        rn.place(x=170,y=310,height=30)
        
        btn_add=Button(self.root,text="Add",font=("Arial Bold",18),command=add)
        btn_add.place(x=0,y=350)

        btn_retrieve=Button(self.root,text="update",font=("Arial Bold",18),command=update)
        btn_retrieve.place(x=100,y=350)

        btn_delete=Button(self.root,text="Delete",font=("Arial Bold",18),command=delete)
        btn_delete.place(x=380,y=370,height=32)

        update_box=Entry(self.root,width=25)
        update_box.place(x=220,y=450,height=30)

        edit_btn=Button(self.root,text="edit",font=("Arial Bold",18),width=5,command=edit)
        edit_btn.place(x=380,y=420)
        root.mainloop()


    

if __name__=="__main__":
    root=Tk()
    obj=dbtable(root)
    root.mainloop()
