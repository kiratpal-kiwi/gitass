from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector


def main():
    win = Tk()
    app = Login_Window(win)
    win.mainloop()


class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        self.bg1 = ImageTk.PhotoImage(file=r"G:\Web Development\Project_TkInter_Project\images\bg1.jpg")
        lbl_bg1 = Label(self.root, image=self.bg1)
        lbl_bg1.place(x=0, y=0, relwidth=1, relheight=1)

        frame = Frame(self.root, bg="black")
        frame.place(x=615, y=170, width=340, height=450)

        # login logo image
        self.login_head = ImageTk.PhotoImage(
            file=r"G:\Web Development\Project_TkInter_Project\images\login_head1 (1).jpg")
        lblimg1 = Label(image=self.login_head, bg="black", borderwidth=0)
        lblimg1.place(x=730, y=180)

        # Username lable and entry
        lblUsername = Label(frame, text="Username", fg="white", bg="black", font=("times new roman", 15, "bold"))
        lblUsername.place(x=120, y=150)

        self.txtuser = ttk.Entry(frame, font=("times new roman", 13, "bold"))
        self.txtuser.place(x=40, y=180, width=270)

        # Password lable and entry
        lblPassword = Label(frame, text="Password", fg="white", bg="black", font=("times new roman", 15, "bold"))
        lblPassword.place(x=120, y=230)

        self.txtpass = ttk.Entry(frame, font=("times new roman", 13, "bold"))
        self.txtpass.place(x=40, y=260, width=270)

        # Login button
        loginbtn = Button(frame, command=self.login, text="Login", cursor="hand2", font=("times new roman", 13, "bold"),
                          bd=3, relief=RIDGE, fg="white", bg="red", activeforeground="blue", activebackground="red")
        loginbtn.place(x=115, y=300, width=120, height=35)
        # register button
        registerbtn = Button(frame, command=self.register_window, text="Register Here", cursor="hand2",
                             font=("times new roman", 10, "bold"), borderwidth=0, fg="white", bg="black",
                             activeforeground="white", activebackground="black")
        registerbtn.place(x=40, y=350)
        # forget password button
        forgetbtn = Button(frame, command=self.forget_password_window, text="Forget Password", cursor="hand2",
                           font=("times new roman", 10, "bold"), borderwidth=0,
                           fg="white", bg="black", activeforeground="white", activebackground="black")
        forgetbtn.place(x=40, y=380)

    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)

    # Login validation
    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "All fields required")
        elif self.txtuser.get() == "kirat" and self.txtpass.get() == "1234":
            messagebox.showinfo("Success", "Welcome to the Library management system application.")
        else:
            con = mysql.connector.connect(host="localhost", user="root", password="root", database="managementdb")
            my_cursor = con.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s", (
                self.txtuser.get(),
                self.txtpass.get()
            ))
            row = my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error", "Invalid Username and Password")
            else:
                open_main = messagebox.askyesno("Success", "Do You Want To Proceed")
                if open_main > 0:
                    self.new_window = Toplevel(self.root)
                else:
                    if not open_main:
                        return

            con.commit()
            con.close()

    # reset password function
    def reset_pass(self):
        if self.combo_security_Q.get() == "Select":
            messagebox.showerror("Error", "Select security Questions", parent=self.root2)
        elif self.txt_security.get() == "":
            messagebox.showerror("Error", "Please enter security answer", parent=self.root2)
        elif self.txt_newpass.get() == "":
            messagebox.showerror("Error", "Please enter new password", parent=self.root2)
        else:
            con = mysql.connector.connect(host="localhost", user="root", password="root", database="managementdb")
            my_cursor = con.cursor()
            query = ("select * from register where email = %s and securityQ = %s and securityA= %s")
            value = (self.txtuser.get(), self.combo_security_Q.get(), self.txt_security.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error", "Please enter correct answer", parent=self.root2)
            else:
                query = ("update register set password= %s where email = %s")
                value = (self.txt_newpass.get(), self.txtuser.get(),)
                my_cursor.execute(query, value)

                con.commit()
                con.close()
                messagebox.showinfo("Success", "Password reset successfully", parent=self.root2)
                self.root2.destroy()

    # Forget password window
    def forget_password_window(self):
        if self.txtuser.get() == "":
            messagebox.showerror("Error", "Please enter the email address to reset password")
        else:
            con = mysql.connector.connect(host="localhost", user="root", password="root", database="managementdb")
            my_cursor = con.cursor()
            query = ("select * from register where email=%s")
            value = (self.txtuser.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error", "Please enter valid username")
            else:
                con.close()

                self.root2 = Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+170")

                # froget password lable
                l = Label(self.root2, text="Forget Password", fg="red", bg="white",
                          font=("times new roman", 20, "bold"))
                l.place(x=0, y=10, relwidth=1)

                # security question and answer
                security_Q = Label(self.root2, text="Select Security Question", font=("times new roman", 15, "bold"),
                                   bg="white", fg="black")
                security_Q.place(x=50, y=80)

                self.combo_security_Q = ttk.Combobox(self.root2,
                                                     font=("times new roman", 15, "bold"), state="readonly")
                self.combo_security_Q["values"] = (
                    "Select", "Your Birthday Place", "Your Girlfriend name", "Your Pet Name")
                self.combo_security_Q.place(x=50, y=120, width=250)
                self.combo_security_Q.current(0)

                Security_A = Label(self.root2, text="Security Answer", font=("times new roman", 15, "bold"), bg="white",
                                   fg="black")
                Security_A.place(x=50, y=160)

                self.txt_security = ttk.Entry(self.root2, font=("times new roman", 15))
                self.txt_security.place(x=50, y=200, width=250)

                # new password lable and entry
                new_password = Label(self.root2, text="New Password", font=("times new roman", 15, "bold"), bg="white",
                                     fg="black")
                new_password.place(x=50, y=240)

                self.txt_newpass = ttk.Entry(self.root2, font=("times new roman", 15))
                self.txt_newpass.place(x=50, y=280, width=250)

                # reset password button
                resetbtn = Button(self.root2, command=self.reset_pass, text="Reset", cursor="hand2",
                                  font=("times new roman", 15, "bold"), borderwidth=0,
                                  fg="white", bg="green", activeforeground="white", activebackground="black")
                resetbtn.place(x=130, y=320)


class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1550x800+0+0")

        # TEXT VAriable
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_SecurityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()
        self.var_check = IntVar()

        # bg image
        self.bg1 = ImageTk.PhotoImage(file=r"G:\Web Development\Project_TkInter_Project\images\bg1.jpg")
        lbl_bg1 = Label(self.root, image=self.bg1)
        lbl_bg1.place(x=0, y=0, relwidth=1, relheight=1)

        # frame for register
        frame = Frame(self.root, bg="white")
        frame.place(x=375, y=100, width=800, height=550)

        register_lbl = Label(frame, text="REGISTER HERE", font=("times new roman", 20, "bold"), fg="darkgreen",
                             bg="white")
        register_lbl.place(x=20, y=20)

        # first name last name

        fname = Label(frame, text="First Name", font=("times new roman", 15, "bold"), bg="white", fg="black")
        fname.place(x=30, y=80)

        fname_entry = ttk.Entry(frame, textvariable=self.var_fname, font=("times new roman", 15))
        fname_entry.place(x=30, y=115, width=250)

        l_name = Label(frame, text="Last Name", font=("times new roman", 15, "bold"), bg="white", fg="black")
        l_name.place(x=350, y=80)

        self.txt_lname = ttk.Entry(frame, textvariable=self.var_lname, font=("times new roman", 15))
        self.txt_lname.place(x=350, y=115, width=250)

        # contact and email

        contact = Label(frame, text="Contact No.", font=("times new roman", 15, "bold"), bg="white", fg="black")
        contact.place(x=30, y=160)

        self.txt_contact = ttk.Entry(frame, textvariable=self.var_contact, font=("times new roman", 15))
        self.txt_contact.place(x=30, y=195, width=250)

        email = Label(frame, text="Email", font=("times new roman", 15, "bold"), bg="white", fg="black")
        email.place(x=350, y=160)

        self.txt_email = ttk.Entry(frame, textvariable=self.var_email, font=("times new roman", 15))
        self.txt_email.place(x=350, y=195, width=250)

        # Security Question and security answer

        security_Q = Label(frame, text="Select Security Question", font=("times new roman", 15, "bold"), bg="white",
                           fg="black")
        security_Q.place(x=30, y=240)

        self.combo_security_Q = ttk.Combobox(frame, textvariable=self.var_securityQ,
                                             font=("times new roman", 15, "bold"), state="readonly")
        self.combo_security_Q["values"] = ("Select", "Your Birthday Place", "Your Girlfriend name", "Your Pet Name")
        self.combo_security_Q.place(x=30, y=275, width=250)
        self.combo_security_Q.current(0)

        Security_A = Label(frame, text="Security Answer", font=("times new roman", 15, "bold"), bg="white", fg="black")
        Security_A.place(x=350, y=240)

        self.txt_security = ttk.Entry(frame, textvariable=self.var_SecurityA, font=("times new roman", 15))
        self.txt_security.place(x=350, y=275, width=250)

        # Password and confirm password

        pswd = Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="white",
                     fg="black")
        pswd.place(x=30, y=320)

        self.txt_pswd = ttk.Entry(frame, textvariable=self.var_pass, font=("times new roman", 15))
        self.txt_pswd.place(x=30, y=355, width=250)

        confirm_pswd = Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white",
                             fg="black")
        confirm_pswd.place(x=350, y=320)

        self.txt_confirm_pswd = ttk.Entry(frame, textvariable=self.var_confpass, font=("times new roman", 15))
        self.txt_confirm_pswd.place(x=350, y=355, width=250)

        # Terms and condition

        checkbtn = Checkbutton(frame, variable=self.var_check, text="I Agree The Terms & Conditions",
                               font=("times new roman", 12, "bold"), onvalue=1, offvalue=0)
        checkbtn.place(x=30, y=400)

        # register now button and login button

        b1 = Button(frame, text="Register Now", command=self.register_data, cursor="hand2",
                    font=("times new roman", 15, "bold"), bg="red", fg="white", activebackground="red",
                    activeforeground="white")
        b1.place(x=30, y=450, width=150)

        b2 = Button(frame, text="Login", command=self.return_login, cursor="hand2",
                    font=("times new roman", 15, "bold"), bg="red",
                    fg="white", activebackground="red", activeforeground="white")
        b2.place(x=350, y=450, width=150)

    # velidation
    def register_data(self):
        if self.var_fname.get() == "" or self.var_lname.get() == "" or self.var_securityQ.get() == "Select" or self.var_SecurityA.get() == "":
            messagebox.showerror("Error", "All fields are required")
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error", "Password not matching or filled")
        elif self.var_check.get() == 0:
            messagebox.showerror("Error", "Please agree our Terms and Conditions")
        else:
            con = mysql.connector.connect(host="localhost", user="root", password="root", database="managementdb")
            my_cursor = con.cursor()
            query = ("select * from register where email = %s")
            value = (self.var_email.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row != None:
                messagebox.showerror("Error", "User already exist,please try with different email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)", (
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
                messagebox.showinfo("Success", "Registeration Successful")
                self.root.destroy()

    def return_login(self):
        self.root.destroy()


if __name__ == "__main__":
    main()
