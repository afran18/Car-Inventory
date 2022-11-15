from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import sqlite3
import os
import email_pass
import smtplib
import time



class Login_System:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System | Developed by Afran & Afnan")
        self.root.geometry("1580x800+0+0")

        self.otp=''


        car_title = Label(self.root, text="Car Inventory Database System",font=("poppins", 30, "bold"),fg="#2388ff", anchor="w", padx=70).place(x=0, y=10,height=70)
        name_title = Label(self.root, text="Developed by Afran & Afnan",font=("poppins", 20),anchor="w", padx=70).place(x=120, y=70,height=50)

        blue_bg = Label(self.root, bg="#ffc900")
        blue_bg.place(x=0, y=0, width=40, relheight=1)

        yellow_bg = Label(self.root,bg="#ffc900")
        yellow_bg.place(x=1130, y=0, width=450, relheight=1)

        # =========Login_Frame===============

        self.employee_name = StringVar()
        self.password = StringVar()

        login_frame = Frame(self.root, bd=0, relief=RIDGE, bg="#000B49")
        login_frame.place(x=950, y=90, width=350, height=460)

        title = Label(login_frame, text="Login System", font=("Poppins", 25, "bold"), bg="#000B49", fg="#fff")
        title.place(x=0, y=20, relwidth=1)

        lbl_user = Label(login_frame, text="Employee Name", font=("Times new roman", 15), bg="#000B49", fg="#fff")
        lbl_user.place(x=50, y=100)

        txt_username = Entry(login_frame, textvariable=self.employee_name, font=("Times new roman", 15), bg="#ececec",
                             fg="#000")
        txt_username.place(x=50, y=130, width=250)

        lbl_pass = Label(login_frame, text="Password", font=("Times new roman", 15), bg="#000B49", fg="#fff")
        lbl_pass.place(x=50, y=190)
        txt_pass = Entry(login_frame, textvariable=self.password, show="*", font=("Times new roman", 15), bg="#ececec",
                         fg="#000")
        txt_pass.place(x=50, y=220, width=250)

        btn_login = Button(login_frame, command=self.login, text="Login", font=("Poppins", 15, "bold"), bg="#00B0F0",
                           fg="#fff", activebackground="#00B0F0", activeforeground="#fff", cursor="hand2")
        btn_login.place(x=50, y=300, width=250, height=35)

        hr = Label(login_frame, bg="lightgrey").place(x=50, y=370, width=250, height=2)
        or_ = Label(login_frame, text="OR", font=("Times new roman", 15, "bold"), fg="#fff", bg="#000B49").place(x=150, y=355)

        btn_forget = Button(login_frame, command=self.forget_window, text="Forget Password?", font=("Times new roman", 15,), bd=0, bg="#000B49",
                            fg="#ffc900", activebackground="#000B49", activeforeground="#ffc900", cursor="hand2")
        btn_forget.place(x=100, y=400)

        # ====Frame 2=======================
        register_frame = Frame(self.root, bd=0, relief=RIDGE, bg="#000B49")
        register_frame.place(x=950, y=570, width=350, height=60)

        lbl_reg = Label(register_frame, text="DBMS MINI PROJECT", font=("poppins", 15, "bold"), bg="#000B49", fg="#fff").place(x=0, y=2, relwidth=1, relheight=1)
        #btn_signup = Button(register_frame, text="Sign up", font=("Times new roman", 13, "bold"), bd=0, bg="#000B49",
                            #fg="#ffc900", activebackground="#000B49", activeforeground="#ffc900", cursor="hand2")
        #btn_signup.place(x=200, y=17)

        # ===animation images===============
        self.im1 = ImageTk.PhotoImage(file="images/bmw.png")
        self.im2 = ImageTk.PhotoImage(file="images/mclaren.png")
        self.im3 = ImageTk.PhotoImage(file="images/huracan.png")

        self.lbl_change_image = Label(self.root)
        self.lbl_change_image.place(x=100, y=250, width=680, height=270)
        self.animate_image()


#===============ALL FUNCTIONS============================

    def animate_image(self):
        self.im = self.im1
        self.im1 = self.im2
        self.im2 = self.im3
        self.im3 = self.im
        self.lbl_change_image.config(image=self.im)
        self.lbl_change_image.after(2000, self.animate_image)

    def login(self):
        con = sqlite3.connect(database=r'car2.db')
        cur = con.cursor()
        try:
            if self.employee_name.get()=="" or self.password.get()=="":
                messagebox.showerror("Error", "All fields are required", parent=self.root)
            else:
                cur.execute("select utype from employee where name=? AND pass=?", (self.employee_name.get(), self.password.get()))
                user = cur.fetchone()
                if user==None:
                    messagebox.showerror("Error", "No such user found", parent=self.root)
                else:
                    if user[0]=="Admin":
                        self.root.destroy()
                        os.system("python dashboard.py")

                    else:
                        self.root.destroy()
                        os.system("python billing.py")

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def forget_window(self):
        con = sqlite3.connect(database=r'car2.db')
        cur = con.cursor()
        try:
            if self.employee_name.get()=="":
                messagebox.showerror("Error", "No such user found", parent=self.root)
            else:
                cur.execute("select email from employee where name=?",(self.employee_name.get(),))
                email = cur.fetchone()
                if email == None:
                    messagebox.showerror("Error", "No such user found", parent=self.root)
                else:
                    #=======forget window======
                    self.var_otp=StringVar()
                    self.var_new_pass=StringVar()
                    self.var_conf_pass=StringVar()

                    #======CALL SEND EMAIL FUNCTION=============
                    chk = self.send_email(email[0])
                    if chk == 'f':
                        messagebox.showerror("Error", "Connection error, try again", parent=self.root)
                    else:
                        self.forget_win = Toplevel(self.root)
                        self.forget_win.title("RESET PASSWORD")
                        self.forget_win.geometry("400x350+600+200")
                        self.forget_win.focus_force()

                        title = Label(self.forget_win, text="Reset Password", font=("Times new roman", 15, "bold"), bg="#3f51b5",fg="#fff").pack(side=TOP, fill=X)

                        lbl_reset = Label(self.forget_win, text="Enter OTP sent on Registered Email",font=("Times new roman", 15)).place(x=20, y=60)
                        txt_reset = Entry(self.forget_win, textvariable=self.var_otp, font=("Times new roman", 15), bg="lightgreen")
                        txt_reset.place(x=20, y=100, width=250, height=30)
                        self.btn_reset = Button(self.forget_win,command=self.validate_otp, text="Submit", font=("Times new roman", 15), bg="lightblue",cursor="hand2")
                        self.btn_reset.place(x=280, y=99, width=100, height=30)

                        lbl_new_pass = Label(self.forget_win, text="Enter New Password", font=("Times new roman", 15, "bold")).place(x=20, y=160)
                        txt_new_pass = Entry(self.forget_win, textvariable=self.var_new_pass, font=("Times new roman", 15), bg="lightgreen")
                        txt_new_pass.place(x=20, y=190, width=250, height=30)

                        lbl_c_pass = Label(self.forget_win, text="Confirm New Password", font=("Times new roman", 15, "bold")).place(x=20, y=225)
                        txt_c_pass = Entry(self.forget_win, textvariable=self.var_conf_pass, font=("Times new roman", 15),bg="lightgreen")
                        txt_c_pass.place(x=20, y=255, width=250, height=30)

                        self.btn_update = Button(self.forget_win, command=self.update_password, text="Update", state=DISABLED, font=("Times new roman", 15),bg="lightblue", cursor="hand2")
                        self.btn_update.place(x=150, y=299, width=100, height=30)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.forget_win)

    def send_email(self, to_):
        s=smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        email_=email_pass.email_
        pass_=email_pass.pass_

        s.login(email_,pass_)
        
        self.otp=int(time.strftime("%H%S%M"))+int(time.strftime("%S"))

        subj = 'CAR DBMS | Reset Password OTP'
        msg = f'Dear {str(self.employee_name.get())},\n\nYour OTP is: {str(self.otp)}.\n\nWith Regards,\nAfran & Afnan'
        msg = "Subject:{}\n\n{}".format(subj, msg)
        s.sendmail(email_, to_, msg)
        chk = s.ehlo()

        if chk[0]== 250:
            return 's'
        else:
            return'f'

    def validate_otp(self):
        if int(self.otp)==int(self.var_otp.get()):
            self.btn_update.config(state=NORMAL)
            self.btn_reset.config(state=DISABLED)
        else:
            messagebox.showerror(("Error", "Invalid OTP, Try Again"), parent=self.forget_win)

    def update_password(self):
        if self.var_new_pass.get() == "" or self.var_conf_pass.get() == "":
            messagebox.showerror(("Error", "Enter new password"), parent=self.forget_win)
        elif self.var_new_pass.get() != self.var_conf_pass.get():
            messagebox.showerror(("Error", "Passwords don't match"), parent=self.forget_win)
        else:
            con = sqlite3.connect(database=r'car2.db')
            cur = con.cursor()
            try:
                cur.execute("Update employee SET pass=? where name=?", (self.var_new_pass.get(), self.employee_name.get()))
                con.commit()
                messagebox.showinfo("Password Changed", "Your Password has been changed successfully", parent=self.forget_win)
                self.forget_win.destroy()

            except Exception as ex:
                messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.forget_win)





root = Tk()
obj = Login_System(root)
root.mainloop()
