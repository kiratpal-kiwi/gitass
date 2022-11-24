from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image, ImageTk
import mysql.connector

class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1550x800+0+0")

        #TEXT VAriable
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_SecurityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        self.var_check=IntVar()




        # bg image
        self.bg1 = ImageTk.PhotoImage(file=r"G:\Web Development\Project_TkInter_Project\images\bg1.jpg")
        lbl_bg1 = Label(self.root, image=self.bg1)
        lbl_bg1.place(x=0, y=0, relwidth=1, relheight=1)

        #frame for register
        frame=Frame(self.root,bg="white")
        frame.place(x=375,y=100,width=800,height=550)

        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="darkgreen",bg="white")
        register_lbl.place(x=20,y=20)

        #first name last name

        fname = Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white",fg="black")
        fname.place(x=30,y=80)

        fname_entry = ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15))
        fname_entry.place(x=30,y=115,width=250)

        l_name = Label(frame, text="Last Name", font=("times new roman", 15, "bold"), bg="white", fg="black")
        l_name.place(x=350, y=80)

        self.txt_lname = ttk.Entry(frame,textvariable=self.var_lname, font=("times new roman", 15))
        self.txt_lname.place(x=350, y=115, width=250)


        #contact and email

        contact=Label(frame,text="Contact No.",font=("times new roman", 15, "bold"),bg="white",fg="black")
        contact.place(x=30,y=160)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman", 15))
        self.txt_contact.place(x=30,y=195,width=250)

        email=Label(frame,text="Email",font=("times new roman", 15, "bold"),bg="white",fg="black")
        email.place(x=350,y=160)

        self.txt_email= ttk.Entry(frame,textvariable=self.var_email,font=("times new roman", 15))
        self.txt_email.place(x=350,y=195,width=250)

        #Security Question and security answer

        security_Q=Label(frame,text="Select Security Question",font=("times new roman", 15, "bold"),bg="white",fg="black")
        security_Q.place(x=30,y=240)

        self.combo_security_Q = ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","Your Birthday Place","Your Girlfriend name","Your Pet Name")
        self.combo_security_Q.place(x=30,y=275,width=250)
        self.combo_security_Q.current(0)

        Security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
        Security_A.place(x=350,y=240)

        self.txt_security = ttk.Entry(frame,textvariable=self.var_SecurityA, font=("times new roman", 15))
        self.txt_security.place(x=350, y=275, width=250)

        #Password and confirm password

        pswd = Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="white",
                           fg="black")
        pswd.place(x=30, y=320)

        self.txt_pswd = ttk.Entry(frame,textvariable=self.var_pass, font=("times new roman", 15))
        self.txt_pswd.place(x=30, y=355, width=250)



        confirm_pswd = Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white",
                           fg="black")
        confirm_pswd.place(x=350, y=320)

        self.txt_confirm_pswd = ttk.Entry(frame,textvariable=self.var_confpass, font=("times new roman", 15))
        self.txt_confirm_pswd.place(x=350, y=355, width=250)


        #Terms and condition

        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree The Terms & Conditions",font=("times new roman", 12,"bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=30,y=400)

        #register now button and login button

        b1 = Button(frame,text="Register Now",command=self.register_data,cursor="hand2",font=("times new roman", 15,"bold"),bg="red",fg="white",activebackground="red",activeforeground="white")
        b1.place(x=30,y=450,width=150)

        b2 = Button(frame, text="Login", cursor="hand2", font=("times new roman", 15, "bold"), bg="red",
                    fg="white", activebackground="red", activeforeground="white")
        b2.place(x=350, y=450,width=150)

    #velidation
    def register_data(self):
        if self.var_fname.get()=="" or self.var_lname.get()=="" or self.var_securityQ.get()=="Select" or self.var_SecurityA.get()=="":
            messagebox.showerror("Error","All fields are required")
        elif self.var_pass.get()!=self.var_confpass.get() :
            messagebox.showerror("Error","Password not matching or filled")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our Terms and Conditions")
        else:
            con = mysql.connector.connect(host="localhost",user="root",password="root",database = "managementdb")
            my_cursor = con.cursor()
            query = ("select * from register where email = %s")
            value = (self.var_email.get(),)
            my_cursor.execute(query,value)
            row = my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist,please try with different email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_securityQ.get(),
                                                                                        self.var_SecurityA.get(),
                                                                                        self.var_pass.get()
                ))
                con.commit()
                con.close()
                messagebox.showinfo("Success","Registeration Successful")





if __name__ == "__main__":
    root = Tk()
    app = Register(root)
    root.mainloop()