from tkinter import *

class ManagementSystem:
    def __init__(self,root):
        self.root = root
        self.root.title("Management System")
        self.root.geometry("1550x800+0+0")

        #management lable
        lbltitle = Label(self.root,text = "Management System",bg="light green",fg="green",bd=10,relief=RIDGE,padx=2,pady=6,font=("times new roman",50,"bold"))
        lbltitle.pack(side=TOP,fill=X)


        #frame outer

        frame = Frame(self.root,bd=12,padx=20,relief=RIDGE,bg="light green")
        frame.place(x=0,y=130,width=1530,height=400)


        #inner left frame
        leftdataframe= LabelFrame(frame,text="Information",bg="light green",fg="green",bd=12,relief=RIDGE,font=("times new roman",12,"bold"))
        leftdataframe.place(x=0,y=5,width=900,height=360)

        #inner right frame

        rightdataframe = LabelFrame(frame,text="Details",bg="light green",fg="green",bd=12,relief=RIDGE,font=("times new roman",12,"bold"))
        rightdataframe.place(x=910,y=5,width=540,height=360)









if __name__ == "__main__":
    root = Tk()
    obj = ManagementSystem(root)
    root.mainloop()