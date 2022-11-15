from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3


class productClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1300x500+220+130")
        self.root.title("Car Inventory Management System | Developed my Afran & Afnan")
        self.root.config(bg="#fff")
        self.root.focus_force()
        #==================================================
        
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()
        self.cat_list=StringVar()
        self.var_cat=StringVar()
        self.var_cat_id = StringVar()
        self.var_sup_invoice = StringVar()
        self.var_contact = StringVar()
        self.txt_desc = StringVar()
        self.txt_desc = StringVar()
        self.var_cat_name = StringVar()
        self.var_sup_name = StringVar()
        self.var_pid = StringVar()


        
        self.var_sup=StringVar()
        self.var_name=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.var_status=StringVar()
        self.var_name_product = StringVar()
        
        self.sup_list=[]
        
        
        
        
        
        product_Frame=Frame(self.root,bd=3,relief=RIDGE,bg="white")
        product_Frame.place(x=10,y=10,width=350,height=480)

        # =============column2==============
        lbl_category_enter = Label(product_Frame, text="Please select a category from table", font=("times new roman", 12), bg="white", fg="#1588ff").place(x=110, y=35)
        title = Label(product_Frame, text=" Manage Products Details", font=("times new roman", 18), bg="#1C0C5B", fg="#fff").pack(side=TOP,fill=X)
        lbl_category = Label(product_Frame, text="Category", font=("times new roman", 15), bg="white").place(x=20, y=60)
        lbl_supplier = Label(product_Frame, text="Supplier", font=("times new roman", 15), bg="white").place(x=20, y=110)
        lbl_product_name = Label(product_Frame, text="Name ", font=("times new roman", 15), bg="white").place(x=20, y=160)
        lbl_price = Label(product_Frame, text="Price", font=("times new roman", 15), bg="white").place(x=20, y=210)
        lbl_quantity = Label(product_Frame, text="Quantity", font=("times new roman", 15), bg="white").place(x=20, y=260)
        lbl_status = Label(product_Frame, text="Status", font=("times new roman", 15), bg="white").place(x=20, y=310)

        txt_category = Entry(product_Frame, textvariable=self.var_cat_name, font=("times new roman", 15),bg="lightgreen")
        txt_category.place(x=110, y=60, width=180)

        lbl_supplier_enter = Label(product_Frame, text="Please select a supplier from table", font=("times new roman", 12), bg="white", fg="#1588ff").place(x=110, y=85)

        txt_supplier = Entry(product_Frame, textvariable=self.var_sup_name, font=("times new roman", 15),bg="lightgreen")
        txt_supplier.place(x=110, y=110, width=180)
        txt_name = Entry(product_Frame, textvariable=self.var_name_product, font=("times new roman", 15),bg="lightgreen")
        txt_name.place(x=110, y=160, width=180)
        txt_price = Entry(product_Frame, textvariable=self.var_price, font=("times new roman", 15),bg="lightgreen")
        txt_price.place(x=110, y=210, width=180)
        txt_qty = Entry(product_Frame, textvariable=self.var_qty, font=("times new roman", 15),bg="lightgreen")
        txt_qty.place(x=110, y=260, width=180)

        cmb_status = ttk.Combobox(product_Frame, textvariable=self.var_status,
                                  values=("Active", "Inactive"), state='readonly', justify=CENTER,
                                  font=("times new roman", 15))
        cmb_status.place(x=110, y=310, width=180)
        cmb_status.current(0)

         # ======buttons ====
        btn_add = Button(product_Frame, text="Save", command=self.add, font=("times new roman", 15), bg="#2196f3",
                         fg="#fff",
                         cursor="hand2").place(x=60, y=350, width=100, height=40)
        btn_update = Button(product_Frame, text="Update", command=self.update, font=("times new roman", 15), bg="#4caf50", fg="#fff",
                         cursor="hand2").place(x=180, y=350, width=100, height=40)
        btn_delete = Button(product_Frame, command=self.delete, text="Delete", font=("times new roman", 15), bg="#ff4336", fg="#fff",
                         cursor="hand2").place(x=60, y=410, width=100, height=40)
        btn_clear = Button(product_Frame, command=self.clear, text="Clear", font=("times new roman", 15), bg="#607d8b", fg="#fff",
                         cursor="hand2").place(x=180, y=410, width=100, height=40)


         # ==============================================
        #SearchFrame = LabelFrame(self.root, text="Search Products", bg="white", font=("times new roman", 15), bd=2,
                                 #relief=RIDGE)
        #SearchFrame.place(x=480, y=0, width=600, height=80)

           # =============Options===============
        #cmb_search = ttk.Combobox(SearchFrame, textvariable=self.var_searchby,
                                  #values=("Select","category","spplier","name"), state='readonly', justify=CENTER,
                                  #font=("times new roman", 15))
        #cmb_search.place(x=10, y=10, width=180, height=30)
        #cmb_search.current(0)

        #txt_search = Entry(SearchFrame, textvariable=self.var_searchtxt, font=("times new roman", 15),
                           #bg="lightblue").place(x=200, y=10, height=30)
        #btn_search = Button(SearchFrame, command=self.search, text="Search", font=("times new roman", 15), bg="#4caf50", fg="#fff",
                            #cursor="hand2").place(x=410, y=9, width=150, height=30)


        #=============product details=========================

        p_Frame = Frame(self.root, bd=3, relief=RIDGE)
        p_Frame.place(x=680, y=190, width=640, height=300)

        scrolly = Scrollbar(p_Frame, orient=VERTICAL)
        scrollx = Scrollbar(p_Frame, orient=HORIZONTAL)

        self.productTable = ttk.Treeview(p_Frame, columns=( "pid","supplier","Category","name","price","qty","status"),yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)

        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.productTable.xview)
        scrolly.config(command=self.productTable.yview)

        self.productTable["show"] = "headings"
        self.productTable.heading("pid", text="P ID")
        self.productTable.heading("supplier", text="SUPPLIER")
        self.productTable.heading("Category", text="CATEGORY")
        self.productTable.heading("name", text="NAME")
        self.productTable.heading("price", text="PRICE")
        self.productTable.heading("qty", text="QUANTITY")
        self.productTable.heading("status", text="STATUS")


        self.productTable["show"] = "headings"

        self.productTable.column("pid", width=40)
        self.productTable.column("supplier", width=110)
        self.productTable.column("Category", width=90)
        self.productTable.column("name", width=90)
        self.productTable.column("price", width=90)

        self.productTable.column("qty", width=90)
        self.productTable.column("status", width=90)


        self.productTable.pack(fill=BOTH, expand=1)
        self.productTable.bind("<ButtonRelease-1>", self.get_data)
        self.show()

        # ==========Category Frame==========================
        cat_frame = Frame(self.root, bd=3, relief=RIDGE)
        cat_frame.place(x=360, y=10, width=320, height=480)

        scrolly = Scrollbar(cat_frame, orient=VERTICAL)
        scrollx = Scrollbar(cat_frame, orient=HORIZONTAL)

        self.CategoryTable = ttk.Treeview(cat_frame, columns=("cid", "name"), yscrollcommand=scrolly.set,
                                          xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.CategoryTable.xview)
        scrolly.config(command=self.CategoryTable.yview)

        self.CategoryTable["show"] = "headings"
        self.CategoryTable.heading("cid", text="Category ID")
        self.CategoryTable.heading("name", text="NAME")

        self.CategoryTable["show"] = "headings"
        self.CategoryTable.column("cid", width=60)
        self.CategoryTable.column("name", width=120)

        self.CategoryTable.pack(fill=BOTH, expand=1)
        self.CategoryTable.bind("<ButtonRelease-1>", self.get_cat_data)

        self.show_cat()


    #==========SUPPLIER FRAME==========================
        emp_frame = Frame(self.root, bd=3, relief=RIDGE)
        emp_frame.place(x=680, y=10, width=320, height=180)

        scrolly = Scrollbar(emp_frame, orient=VERTICAL)
        scrollx = Scrollbar(emp_frame, orient=HORIZONTAL)

        self.supplierTable = ttk.Treeview(emp_frame, columns=(
            "invoice", "name"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)

        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.supplierTable.xview)
        scrolly.config(command=self.supplierTable.yview)

        self.supplierTable["show"] = "headings"
        self.supplierTable.heading("invoice", text="INVOICE")
        self.supplierTable.heading("name", text="NAME")
        #self.supplierTable.heading("contact", text="CONTACT")
        #self.supplierTable.heading("desc", text="DESCRIPTION")

        self.supplierTable["show"] = "headings"
        self.supplierTable.column("invoice", width=90)
        self.supplierTable.column("name", width=90)
        #self.supplierTable.column("contact", width=90)
        #self.supplierTable.column("desc", width=90)

        self.supplierTable.pack(fill=BOTH, expand=1)
        self.supplierTable.bind("<ButtonRelease-1>", self.get_sup_data)
        self.show_sup()

        self.img1 = Image.open("images/product.jpg")
        self.img1 = self.img1.resize((260, 190), Image.ANTIALIAS)
        self.img1 = ImageTk.PhotoImage(self.img1)

        self.lbl_img1 = Label(self.root, image=self.img1, bd=0)
        self.lbl_img1.place(x=1010, y=0)


        
        
        # ========================================================================================================================


    def add(self):
        con = sqlite3.connect(database=r'car2.db')
        cur = con.cursor()
        try:
            if self.var_cat_name.get() == "Select"or self.var_sup_name.get()=="Select"or self.var_name_product.get()=="":
                messagebox.showerror("Error", "All fields are required", parent=self.root)
            else:
                cur.execute("Select * from product WHERE name=?", (self.var_name_product.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error","Product already exist!!", parent=self.root)
                else:
                    cur.execute(
                        "INSERT INTO product (Category,supplier,name,price,qty,status)"
                        "VALUES(?,?,?,?,?,?)",
                        (
                            self.var_cat_name.get(),
                            self.var_sup_name.get(),
                            self.var_name_product.get(),
                            self.var_price.get(),
                            self.var_qty.get(),
                            self.var_status.get(),
                           
                        ))
                    con.commit()
                    messagebox.showinfo("SUCCESS", "Product added successfully", parent=self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def show(self):
        con = sqlite3.connect(database=r'car2.db')
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM product")
            rows=cur.fetchall()
            self.productTable.delete(*self.productTable.get_children())
            for row in rows:
                self.productTable.insert('', END, values=row)


        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def get_data(self,ev):
        f=self.productTable.focus()
        content=(self.productTable.item(f))
        row=content['values']
        #print(row)
        self.var_pid.set(row[0])
        self.var_cat_name.set(row[2])
        self.var_sup_name.set(row[1])
        self.var_name_product.set(row[3])
        self.var_price.set(row[4])
        self.var_qty.set(row[5])
        self.var_status.set(row[6])

    def update(self):
        con = sqlite3.connect(database=r'car2.db')
        cur = con.cursor()
        try:
            if self.var_pid.get() == "":
                messagebox.showerror("Error", "Please select product from list", parent=self.root)
            else:
                cur.execute("Select * from product WHERE pid=?", (self.var_pid.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Product ID", parent=self.root)
                else:
                    cur.execute(
                        "UPDATE product SET Category=?,supplier=?,name=?,price=?,qty=?,status=? where pid=?",
                        (
                            self.var_cat_name.get(),
                            self.var_sup_name.get(),
                            self.var_name_product.get(),
                            self.var_price.get(),
                            self.var_qty.get(),
                            self.var_status.get(),
                            self.var_pid.get(),
                        ))
                    con.commit()
                    messagebox.showinfo("SUCCESS", "Product updated successfully", parent=self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def delete(self):
        con = sqlite3.connect(database=r'car2.db')
        cur = con.cursor()
        try:
            if self.var_pid.get() == "":
                messagebox.showerror("Error", "Select product from the list", parent=self.root)
            else:
                cur.execute("Select * from product WHERE pid=?", (self.var_pid.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Product", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do you really wish to delete this product?", parent=self.root)
                    if op == True:
                        cur.execute("DELETE FROM  product WHERE  pid=?", (self.var_pid.get(),))
                        con.commit()
                        messagebox.showinfo("DELETE", "Product deleted successfully", parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def clear(self):
        self.var_cat_name.set(""),
        self.var_sup_name.set(""),
        self.var_name_product.set(""),
        self.var_price.set(""),
        self.var_qty.set(""),
        self.var_status.set("Active"),
        self.var_pid.set(""),

        self.var_searchtxt.set("")
        self.var_searchby.set("Select")

        self.show()


    #======category calls===============
    def get_cat_data(self,ev):
        f = self.CategoryTable.focus()
        content = (self.CategoryTable.item(f))
        row = content['values']
        # print(row)
        self.var_cat_id.set(row[0])
        self.var_cat_name.set(row[1])



    def show_cat(self):
        con = sqlite3.connect(database=r'car2.db')
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM category")
            rows=cur.fetchall()
            self.CategoryTable.delete(*self.CategoryTable.get_children())
            for row in rows:
                self.CategoryTable.insert('', END, values=row)


        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

        
    #============supplier calls===================================
    def show_sup(self):
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

    def get_sup_data(self, ev):
        f=self.supplierTable.focus()
        content=(self.supplierTable.item(f))
        row=content['values']
        #print(row)
        self.var_sup_invoice.set(row[0])
        self.var_sup_name.set(row[1])
        self.var_contact.set(row[2])
        #self.txt_desc.delete('1.0', END)
        #self.txt_desc.insert(END, row[3])

        
if __name__ == "__main__":
    root = Tk()
    obj = productClass(root)
    root.mainloop()
