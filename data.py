from tkinter import *

class dbtable:
    def __init__(self,root):
        self.root=root
        self.root.title("Records of tenants")
        self.root.geometry("1295x550+230+0")

if __name__=="__main__":
    root=Tk()
    obj=dbtable(root)
    root.mainloop()
