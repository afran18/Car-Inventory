from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3


class supplierClass:
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

        self.var_sup_invoice = StringVar()
        self.var_desc = StringVar()
        self.var_contact = StringVar()
        self.var_name = StringVar()


        # ==============================================
        SearchFrame = LabelFrame(self.root, text="Search Supplier", font=("times new roman", 12))

        SearchFrame.place(x=250, y=20, width=600, height=70)

        # =============Options===============
        lbl_search = Label(SearchFrame, text="Search By Invoice ",bg="white",font=("times new roman", 15))
        lbl_search.place(x=10, y=10, height=30)


        txt_search = Entry(SearchFrame, textvariable=self.var_searchtxt, font=("times new roman", 15),
                           bg="lightgreen").place(x=200, y=10, height=30)
        btn_search = Button(SearchFrame, command=self.search, text="Search", font=("times new roman", 15), bg="#4caf50", fg="#fff",
                            cursor="hand2").place(x=410, y=9, width=150, height=30)

        # ============TITLE====================
        title = Label(self.root, text="Supplier Details", font=("times new roman", 15), bg="#1C0C5B", fg="#fff").place(
            x=50, y=100, width="1000")

        # =========row1=============
        lbl_supplier_invoice = Label(self.root, text="Invoice No", font=("times new roman", 15), bg="white", ).place(x=50, y=150)

        txt_supplier_invoice = Entry(self.root, textvariable=self.var_sup_invoice, font=("times new roman", 15),
                           bg="lightgreen", )
        txt_supplier_invoice.place(x=150, y=150, width=180)


        # ==========row2======

        lbl_name = Label(self.root, text="Name", font=("times new roman", 15), bg="white", ).place(x=50, y=190)


        txt_name = Entry(self.root, textvariable=self.var_name, font=("times new roman", 15), bg="lightgreen", )
        txt_name.place(x=150, y=190, width=180)

        # =======row3======

        lbl_contact = Label(self.root, text="Contact", font=("times new roman", 15), bg="white", ).place(x=50, y=230)

        txt_contact = Entry(self.root, textvariable=self.var_contact, font=("times new roman", 15),bg="lightgreen", )
        txt_contact.place(x=150, y=230, width=180)

        # =======row4========

        lbl_desc = Label(self.root, text="Description", font=("times new roman", 15), bg="white", ).place(x=50, y=270)

        self.txt_desc = Text(self.root, font=("times new roman", 15), bg="lightgreen", )
        self.txt_desc.place(x=150, y=270,width=240, height=60)

        # ======buttons ====
        btn_add = Button(self.root, text="Save", command=self.add, font=("times new roman", 15), bg="#2196f3",
                         fg="#fff",
                         cursor="hand2").place(x=450, y=150, width=110, height=28)
        btn_update = Button(self.root, text="Update", command=self.update, font=("times new roman", 15), bg="#4caf50", fg="#fff",
                         cursor="hand2").place(x=450, y=190, width=110, height=28)
        btn_delete= Button(self.root, command=self.delete, text="Delete", font=("times new roman", 15), bg="#f44336", fg="#fff",
                         cursor="hand2").place(x=450, y=230, width=110, height=28)
        btn_clear = Button(self.root, command=self.clear, text="Clear", font=("times new roman", 15), bg="#607d8b", fg="#fff",
                         cursor="hand2").place(x=450, y=270, width=110, height=28)


        #==============emp frame=========================

        emp_frame = Frame(self.root, bd=3, relief=RIDGE)
        emp_frame.place(x=0, y=350, relwidth=1, height=300)

        scrolly = Scrollbar(emp_frame, orient=VERTICAL)
        scrollx = Scrollbar(emp_frame, orient=HORIZONTAL)

        self.supplierTable= ttk.Treeview(emp_frame, columns=(
            "invoice","name","contact","desc"),yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)

        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.supplierTable.xview)
        scrolly.config(command=self.supplierTable.yview)

        self.supplierTable["show"] = "headings"
        self.supplierTable.heading("invoice", text="INVOICE")
        self.supplierTable.heading("name", text="NAME")
        self.supplierTable.heading("contact", text="CONTACT")
        self.supplierTable.heading("desc", text="DESCRIPTION")

        self.supplierTable["show"] = "headings"
        self.supplierTable.column("invoice", width=90)
        self.supplierTable.column("name", width=90)
        self.supplierTable.column("contact", width=90)
        self.supplierTable.column("desc", width=90)
        self.supplierTable.column("contact", width=90)

        self.supplierTable.pack(fill=BOTH, expand=1)
        self.supplierTable.bind("<ButtonRelease-1>", self.get_data)
        self.show()

        self.img1 = Image.open("images/cat.jpg")
        self.img1 = self.img1.resize((320, 170), Image.ANTIALIAS)
        self.img1 = ImageTk.PhotoImage(self.img1)

        self.lbl_img1 = Label(self.root, image=self.img1)
        self.lbl_img1.place(x=700, y=150)

        # =======employee details======

    # ========================================================================================================================

    def add(self):
        con = sqlite3.connect(database=r'car2.db')
        cur = con.cursor()
        try:
            if self.var_sup_invoice.get() == "":
                messagebox.showerror("Error", "Invoice must be required", parent=self.root)
            else:
                cur.execute("Select * from Supplier WHERE invoice=?", (self.var_sup_invoice.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "This Invoice No is already assigned, try different",
                                         parent=self.root)
                else:
                    cur.execute(
                        "INSERT INTO Supplier (invoice,name,contact,desc) "
                        "VALUES(?,?,?,?)",
                        (
                            self.var_sup_invoice.get(),
                            self.var_name.get(),
                            self.var_contact.get(),
                           # self.var_desc.get(),

                            self.txt_desc.get('1.0', END),

                        ))
                    con.commit()
                    messagebox.showinfo("SUCCESS", "Supplier added successfully", parent=self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def show(self):
        con = sqlite3.connect(database=r'car2.db')
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM Supplier")
            rows=cur.fetchall()
            self.supplierTable.delete(*self.supplierTable.get_children())
            for row in rows:
                self.supplierTable.insert('', END, values=row)


        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def get_data(self,ev):
        f=self.supplierTable.focus()
        content=(self.supplierTable.item(f))
        row=content['values']
        #print(row)
        self.var_sup_invoice.set(row[0])
        self.var_name.set(row[1])
        self.var_contact.set(row[2])
        self.txt_desc.delete('1.0', END)
        self.txt_desc.insert(END, row[3])


    def update(self):
        con = sqlite3.connect(database=r'car2.db')
        cur = con.cursor()
        try:
            if self.var_sup_invoice.get() == "":
                messagebox.showerror("Error", "Invoice must be required", parent=self.root)
            else:
                cur.execute("Select * from supplier WHERE invoice=?", (self.var_sup_invoice.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid invoice no",
                                         parent=self.root)
                else:
                    cur.execute(
                        "UPDATE Supplier SET name=?,contact=?,desc=? WHERE invoice= ?",

                        (
                            self.var_name.get(),

                            self.var_contact.get(),

                            self.txt_desc.get('1.0', END),

                            self.var_sup_invoice.get(),
                        ))
                    con.commit()
                    messagebox.showinfo("SUCCESS", "Supplier Updated Successfully", parent=self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def delete(self):
        con = sqlite3.connect(database=r'car2.db')
        cur = con.cursor()
        try:
            if self.var_sup_invoice.get() == "":
                messagebox.showerror("Error", "invoice no must be required", parent=self.root)
            else:
                cur.execute("Select * from Supplier WHERE invoice=?", (self.var_sup_invoice.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid invoice no",
                                         parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do you really wish to delete?", parent=self.root)
                    if op == True:
                        cur.execute("DELETE FROM  Supplier WHERE  invoice=?",(self.var_sup_invoice.get(),))
                        con.commit()
                        messagebox.showinfo("DELETE", "Supplier Deleted Successfully", parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def clear(self):
        self.var_sup_invoice.set("")
        self.var_name.set("")
        self.var_contact.set("")
        self.txt_desc.delete('1.0', END)


        self.var_searchtxt.set("")

        self.show()

    def search(self):
        con = sqlite3.connect(database=r'car2.db')
        cur = con.cursor()
        try:

            if self.var_searchtxt.get() == "":
                messagebox.showerror("Error", "Invioce no should be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM supplier WHERE invoice=?",(self.var_searchtxt.get(),))
                row = cur.fetchall()
                if  row!=None:
                    self.supplierTable.delete(*self.supplierTable.get_children())
                    for row in row:
                        self.supplierTable.insert('', END, values=row)
                else:
                    messagebox.showerror("Error","No record found", parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)





if __name__ == "__main__":
    root = Tk()
    obj = supplierClass(root)
    root.mainloop()
