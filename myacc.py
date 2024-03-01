from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
from tkinter import PhotoImage
import sqlite3

a=Tk()
# a.iconbitmap("a.ico")
a.title("GHARBETI - My profile")
a.geometry("450x650")
a.resizable(0,0)
a.config(bg='#F0F4F7')

conn = sqlite3.connect("staff.db")
cursor = conn.cursor()

def login():
    a.destroy()
    import gblogin

def fetch_staff_details():
    staf_id = cid.get()
    # Query to retrieve staff details
    cursor.execute("SELECT * FROM st_records WHERE  ID = ?", (staf_id))
    staff_details = cursor.fetchone()
    if staff_details:
        # Display the fetched details
        staff_id.config(text=f"Staff ID: {staff_details[0]}")
        name_of_staff.config(text=f"Name of Staff: {staff_details[1]}")
        email.config(text=f"Email: {staff_details[3]}")
        contact.config(text=f"Contact: {staff_details[4]}")
    else:
        messagebox.showerror("Error", "Staff details not found!")


cid=Entry(a,text="enter id")
cid.place(x=40,y=400)
fetch_button = Button(a, text="Fetch Staff Details", command=fetch_staff_details)
fetch_button.place(x=200, y=400)

Frame(a, width=700, height=180, bg='#007EA3').place(x = 0, y = 0)
# Frame(a, width=700, height=900, bg='#FFA800').place(x = 0, y = 290)
# Frame(a, width=150,height=150, bg='blue').place(x = 280, y = 170)

staff_id = Label(a, text='Staff Account',
                 font=('Ariel', 40),
                 fg= '#F0F4F7',
                 bg='#007EA3')
staff_id.place(x = 100, y = 70)

name_of_staff = Label(a, text="Name of Staff ",
              font=("Calibri",20),
              bg='#F0F4F7')
name_of_staff.place(x = 40, y = 260)
email = Label(a, text="Email",
              font=("Calibri",20),
              bg='#F0F4F7')
email.place(x = 40, y = 310)
contact = Label(a, text="Contact",
              font=("Calibri",20),
              bg='#F0F4F7')
contact.place(x = 40, y = 360)


logout = Button(a, text='Log out',
                bg="#007EA3",
                font=('Calibri', 20),command=login)
logout.place(x = 150, y = 460)



a.mainloop()