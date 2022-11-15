from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3


class employeeClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.title("Car Inventory Management System | Developed my Afran & Afnan")
        self.root.config(bg="#fff")
        self.root.focus_force()

        # ======================================
        # ALL Variables =====================
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()

        self.var_emp_id = StringVar()
        self.var_gender = StringVar()
        self.var_contact = StringVar()
        self.var_name = StringVar()
        self.var_dob = StringVar()
        self.var_doj = StringVar()
        self.var_email = StringVar()
        self.var_pass = StringVar()
        self.var_utype = StringVar()
        self.var_salary = StringVar()

        # ==============================================
        SearchFrame = LabelFrame(self.root, text="Search Employee", bg="white", font=("times new roman", 15), bd=2,
                                 relief=RIDGE)
        SearchFrame.place(x=250, y=20, width=600, height=70)

        # =============Options===============
        cmb_search = ttk.Combobox(SearchFrame, textvariable=self.var_searchby,
                                  values=("Select", "Employee", "Name", "Contact"), state='readonly', justify=CENTER,
                                  font=("times new roman", 15))
        cmb_search.place(x=10, y=10, width=180, height=30)
        cmb_search.current(0)

        txt_search = Entry(SearchFrame, textvariable=self.var_searchtxt, font=("times new roman", 15),
                           bg="lightblue").place(x=200, y=10, height=30)
        btn_search = Button(SearchFrame, command=self.search, text="Search", font=("times new roman", 15), bg="#4caf50", fg="#fff",
                            cursor="hand2").place(x=410, y=9, width=150, height=30)

        # ============TITLE====================
        title = Label(self.root, text="Employee Details", font=("times new roman", 15), bg="#1C0C5B", fg="#fff").place(
            x=50, y=100, width="1000")

        # =========row1=============
        lbl_emp_id = Label(self.root, text="Emp ID", font=("times new roman", 15), bg="white", ).place(x=50, y=150)
        lbl_gender = Label(self.root, text="Gender", font=("times new roman", 15), bg="white", ).place(x=400, y=150)
        lbl_contact = Label(self.root, text="Contact", font=("times new roman", 15), bg="white", ).place(x=750, y=150)

        txt_emp_id = Entry(self.root, textvariable=self.var_emp_id, font=("times new roman", 15),
                           bg="lightblue", )
        txt_emp_id.place(x=150, y=150, width=180)

        cmb_gender = ttk.Combobox(self.root, textvariable=self.var_gender,
                                  values=("Select", "Male", "Female", "Others"), state='readonly', justify=CENTER,
                                  font=("times new roman", 15), )
        cmb_gender.place(x=500, y=147, width=180)
        cmb_gender.current(0)
        txt_contact = Entry(self.root, textvariable=self.var_contact, font=("times new roman", 15),
                            bg="lightblue", )
        txt_contact.place(x=850, y=150, width=180)
        # ==========row2======

        lbl_name = Label(self.root, text="Name", font=("times new roman", 15), bg="white", ).place(x=50, y=190)
        lbl_dob = Label(self.root, text="D.O.B", font=("times new roman", 15), bg="white", ).place(x=400, y=190)
        lbl_doj = Label(self.root, text="D.O.J", font=("times new roman", 15), bg="white", ).place(x=750, y=190)

        txt_name = Entry(self.root, textvariable=self.var_name, font=("times new roman", 15), bg="lightblue", )
        txt_name.place(x=150, y=190, width=180)
        txt_dob = Entry(self.root, textvariable=self.var_dob, font=("times new roman", 15), bg="lightblue", )
        txt_dob.place(x=500, y=190, width=180)
        txt_doj = Entry(self.root, textvariable=self.var_doj, font=("times new roman", 15), bg="lightblue", )
        txt_doj.place(x=850, y=190, width=180)

        # =======row3======

        lbl_email = Label(self.root, text="Email", font=("times new roman", 15), bg="white", ).place(x=50, y=230)
        lbl_pass = Label(self.root, text="Password", font=("times new roman", 15), bg="white", ).place(x=400, y=230)
        lbl_utype = Label(self.root, text="User Type", font=("times new roman", 15), bg="white", ).place(x=750, y=230)

        txt_email = Entry(self.root, textvariable=self.var_email, font=("times new roman", 15),bg="lightblue", )
        txt_email.place(x=150, y=230, width=180)
        txt_pass = Entry(self.root, textvariable=self.var_pass, font=("times new roman", 15), bg="lightblue")
        txt_pass.place(x=500, y=230, width=180)
        cmb_utype = ttk.Combobox(self.root, textvariable=self.var_utype,
                                 values=("Admin", "Employee",), state='readonly', justify=CENTER,
                                 font=("times new roman", 15), )
        cmb_utype.place(x=850, y=230, width=180)
        cmb_utype.current(0)

        # =======row4========

        lbl_address = Label(self.root, text="Address", font=("times new roman", 15), bg="white", ).place(x=50, y=270)
        lbl_salary = Label(self.root, text="Salary", font=("times new roman", 15), bg="white", ).place(x=400, y=270)

        self.txt_address = Text(self.root, font=("times new roman", 15), bg="lightblue", )
        self.txt_address.place(x=150, y=270,width=240, height=60)
        txt_salary = Entry(self.root, textvariable=self.var_salary, font=("times new roman", 15),bg="lightblue", )
        txt_salary.place(x=500, y=270, width=180)

        # ======buttons ====
        btn_add = Button(self.root, text="Save", command=self.add, font=("times new roman", 15), bg="#2196f3",
                         fg="#fff",
                         cursor="hand2").place(x=800, y=270, width=110, height=28)
        btn_update = Button(self.root, text="Update", command=self.update, font=("times new roman", 15), bg="#4caf50", fg="#fff",
                         cursor="hand2").place(x=920, y=270, width=110, height=28)
        btn_delete = Button(self.root, command=self.delete, text="Delete", font=("times new roman", 15), bg="#ff4336", fg="#fff",
                         cursor="hand2").place(x=800, y=305, width=110, height=28)
        btn_clear = Button(self.root, command=self.clear, text="Clear", font=("times new roman", 15), bg="#607d8b", fg="#fff",
                         cursor="hand2").place(x=920, y=305, width=110, height=28)

        #=============tree view=========================
        emp_frame = Frame(self.root, bd=3, relief=RIDGE)
        emp_frame.place(x=0, y=350, relwidth=1, height=150)

        scrolly = Scrollbar(emp_frame, orient=VERTICAL)
        scrollx = Scrollbar(emp_frame, orient=HORIZONTAL)

        self.EmployeeTable = ttk.Treeview(emp_frame, columns=(
            "eid", "name", "email", "gender", "contact", "dob", "doj", "pass", "utype", "address", "salary"),
                                          yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.EmployeeTable.xview)
        scrolly.config(command=self.EmployeeTable.yview)

        self.EmployeeTable["show"] = "headings"
        self.EmployeeTable.heading("eid", text="EMP ID")
        self.EmployeeTable.heading("name", text="NAME")
        self.EmployeeTable.heading("email", text="EMAIL")
        self.EmployeeTable.heading("gender", text="GENDER")
        self.EmployeeTable.heading("contact", text="CONTACT")
        self.EmployeeTable.heading("dob", text="D.O.B")
        self.EmployeeTable.heading("doj", text="D.O.J")
        self.EmployeeTable.heading("pass", text="PASSWORD")
        self.EmployeeTable.heading("utype", text="USER TYPE")
        self.EmployeeTable.heading("address", text="ADD")
        self.EmployeeTable.heading("salary", text="SALARY")

        self.EmployeeTable["show"] = "headings"
        self.EmployeeTable.column("eid", width=90)
        self.EmployeeTable.column("name", width=90)
        self.EmployeeTable.column("email", width=90)
        self.EmployeeTable.column("gender", width=90)
        self.EmployeeTable.column("contact", width=90)

        self.EmployeeTable.column("dob", width=90)
        self.EmployeeTable.column("doj", width=90)
        self.EmployeeTable.column("pass", width=90)
        self.EmployeeTable.column("utype", width=90)
        self.EmployeeTable.column("address", width=90)
        self.EmployeeTable.column("salary", width=90)

        self.EmployeeTable.pack(fill=BOTH, expand=1)
        self.EmployeeTable.bind("<ButtonRelease-1>", self.get_data)
        self.show()


    # ========================================================================================================================

    def add(self):
        con = sqlite3.connect(database=r'car2.db')
        cur = con.cursor()
        try:
            if self.var_emp_id.get() == "":
                messagebox.showerror("Error", "Employee ID must be required", parent=self.root)
            else:
                cur.execute("Select * from employee WHERE eid=?", (self.var_emp_id.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error","This Employee id is already assigned, try different",
                                         parent=self.root)
                else:
                    cur.execute(
                        "INSERT INTO employee (eid,name,email,gender,contact,dob,doj,pass,utype,address,salary) "
                        "VALUES(?,?,?,?,?,?,?,?,?,?,?)",
                        (
                            self.var_emp_id.get(),
                            self.var_name.get(),
                            self.var_email.get(),
                            self.var_gender.get(),
                            self.var_contact.get(),
                            self.var_dob.get(),
                            self.var_doj.get(),
                            self.var_pass.get(),
                            self.var_utype.get(),
                            self.txt_address.get('1.0', END),
                            self.var_salary.get(),
                        ))
                    con.commit()
                    messagebox.showinfo("SUCCESS", "Employee added successfully", parent=self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def show(self):
        con = sqlite3.connect(database=r'car2.db')
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM employee")
            rows=cur.fetchall()
            self.EmployeeTable.delete(*self.EmployeeTable.get_children())
            for row in rows:
                self.EmployeeTable.insert('', END, values=row)


        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def get_data(self,ev):
        f=self.EmployeeTable.focus()
        content=(self.EmployeeTable.item(f))
        row=content['values']
        # print(row)
        self.var_emp_id.set(row[0])
        self.var_name.set(row[1])
        self.var_email.set(row[2])
        self.var_gender.set(row[3])
        self.var_contact.set(row[4])
        self.var_dob.set(row[5])
        self.var_doj.set(row[6])
        self.var_pass.set(row[7])
        self.var_utype.set(row[8])
        self.txt_address.delete('1.0', END)
        self.txt_address.insert(END, row[9])
        self.var_salary.set(row[10])

    def update(self):
        con = sqlite3.connect(database=r'car2.db')
        cur = con.cursor()
        try:
            if self.var_emp_id.get() == "":
                messagebox.showerror("Error", "Employee ID must be required", parent=self.root)
            else:
                cur.execute("Select * from employee WHERE eid=?", (self.var_emp_id.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Employee ID",
                                         parent=self.root)
                else:
                    cur.execute(
                        "UPDATE employee SET name=?,email=?,gender=?,contact=?,dob=?,doj=?,pass=?,utype=?,address=?,"
                        "salary=? WHERE eid = ?",
                        (
                            self.var_name.get(),
                            self.var_email.get(),
                            self.var_gender.get(),
                            self.var_contact.get(),
                            self.var_dob.get(),
                            self.var_doj.get(),
                            self.var_pass.get(),
                            self.var_utype.get(),
                            self.txt_address.get('1.0', END),
                            self.var_salary.get(),
                            self.var_emp_id.get(),
                        ))
                    con.commit()
                    messagebox.showinfo("SUCCESS", "Employee updated successfully", parent=self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def delete(self):
        con = sqlite3.connect(database=r'car2.db')
        cur = con.cursor()
        try:
            if self.var_emp_id.get() == "":
                messagebox.showerror("Error", "Employee ID must be required", parent=self.root)
            else:
                cur.execute("Select * from employee WHERE eid=?", (self.var_emp_id.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Employee ID",
                                         parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do you really wish to delete this employee?", parent=self.root)
                    if op == True:
                        cur.execute("DELETE FROM  employee WHERE  eid=?",(self.var_emp_id.get(),))
                        con.commit()
                        messagebox.showinfo("DELETE","Employee deleted successfully", parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def clear(self):
        self.var_emp_id.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("Select")
        self.var_contact.set("")
        self.var_dob.set("")
        self.var_doj.set("")
        self.var_pass.set("")
        self.var_utype.set("Admin")
        self.txt_address.delete('1.0', END)
        self.var_salary.set("")

        self.var_searchtxt.set("")
        self.var_searchby.set("Select")

        self.show()

    def search(self):
        con = sqlite3.connect(database=r'car2.db')
        cur = con.cursor()
        try:
            if self.var_searchby.get() == "Select":
                messagebox.showerror("Error","Select a search option", parent=self.root)
            elif self.var_searchtxt.get() == "":
                messagebox.showerror("Error", "Search input should be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM employee WHERE "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                rows = cur.fetchall()
                if len(rows)!=0:
                    self.EmployeeTable.delete(*self.EmployeeTable.get_children())
                    for row in rows:
                        self.EmployeeTable.insert('', END, values=row)
                else:
                    messagebox.showerror("Error","No record found", parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)



if __name__ == "__main__":
    root = Tk()
    obj = employeeClass(root)
    root.mainloop()
