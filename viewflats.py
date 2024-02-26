from tkinter import *
from data import dbtable
#defining a class for apartment management system
class apms:
    def __init__(self,root):
        self.root=root
        self.root.title("Records of tenants")
        self.root.geometry("1550x800+0+0")

        #placing buttons to navigate through the 
        global home
        home=Button(root,text="Home",
               font=("Calibri",26),
               bg = '#F0F4F7',
               fg='#007EA3',
               cursor='hand2',
               border=0,
               command=home)
        home.place(x=50,y=50)
        Frame(root, width=88,height=2, bg = '#007EA3').place(x = 60, y = 103)

        flat_button=Button(root, text="View flats",
                        font=("Calibri",26),
                        command=self.db_details,
                        fg='#007EA3',
                        bg='#F0F4F7',
                        border=0,
                        cursor='hand2')
        flat_button.place(x=170,y=50)
        Frame(root, width=153,height=2, bg = '#007EA3').place(x = 180, y = 103)
        
    #overlapping on the main window 
    def db_details(self):
        self.newwindow=Toplevel(self.root)
        self.app=dbtable(self.newwindow)

#function in commands onclikcing navigation buttons
def home():
    root.destroy()
    import home
def vflat():
    root.destroy()
    import viewflats



        


        


#calling the function 
if __name__=="__main__":
    root=Tk()
    obj=apms(root)
    root.mainloop()
