from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk, messagebox
import sqlite3
import time
import os
import tempfile

class BillClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1365x700+0+0")
        self.root.title("Car Inventory Management System | Developed my Afran & Afnan")
        self.root.config(bg="#fff")
        self.cart_list = []
        self.chk_print = 0



        #===title====
        self.icon_title=PhotoImage(file="images/logo1.png")
        title=Label(self.root, text="Car Inventory Database System", image=self.icon_title, compound=LEFT, font=("poppins",30,"bold"), bg="#1C0C5B", fg="#fff", anchor="w", padx=20).place(x=0,y=0, relwidth=1,height=70)


        #===BUTTON===
        btn_logout = Button(self.root, command=self.logout, text="Logout",font=("poppins", 15, "bold"), bg="red", fg="white", cursor="hand2", relief="ridge").place(x=1200, y= 10, height=50, width=110)

        # ===clock====
        self.lbl_clock = Label(self.root, text="Developed by Afran & Afnan\t\t Date: DD-MM-YYYY\t\t  Time: HH:MM::SS", font=("times new roman", 15), bg="#FFC900", fg="#781C68")
        self.lbl_clock.place(x=0, y=70, relwidth=1, height=30)

        #====Product Frame=====================
        self.var_search=StringVar()
        ProductFrame1=Frame(self.root,bg="#fff", bd=4, relief=RIDGE)
        ProductFrame1.place(x=6, y=110, width=410, height=550)

        pTitle=Label(ProductFrame1,text="All Products", font=("times new roman", 20, "bold"), bg="#FF2626", fg="#FFF")
        pTitle.pack(side=TOP, fill=X)

        ProductFrame2 = Frame(ProductFrame1, bg="#fff", bd=2, relief=RIDGE)
        ProductFrame2.place(x=2, y=42, width=398, height=90)

        lbl_search=Label(ProductFrame2, text="Search Product | By Name", font=("times new roman", 15, "bold"), bg="white", fg="green")
        lbl_search.place(x=2, y=5)

        lbl_name=Label(ProductFrame2, text="Product Name", font=("times new roman", 15, "bold"), bg="white")
        lbl_name.place(x=2, y=45)

        txt_search=Entry(ProductFrame2, textvariable=self.var_search, font=("times new roman", 15), bg="lightgreen")
        txt_search.place(x=130, y=49, width=150, height=22)

        btn_search=Button(ProductFrame2, command=self.search, text="Search", font=("times new roman", 14, "bold"), bg="#2196f3", fg="#FFF", cursor="hand2")
        btn_search.place(x=285, y=48, width=100, height=22)

        btn_show_all = Button(ProductFrame2, command=self.show, text="Show all", font=("times new roman", 14, "bold"), bg="#083531", fg="#FFF", cursor="hand2")
        btn_show_all.place(x=285, y=10, width=100, height=25)

        ProductFrame3 = Frame(ProductFrame1, bd=3, relief=RIDGE)
        ProductFrame3.place(x=2, y=140, width=398, height=375)

        scrolly = Scrollbar(ProductFrame3, orient=VERTICAL)
        scrollx = Scrollbar(ProductFrame3, orient=HORIZONTAL)

        self.product_Table = ttk.Treeview(ProductFrame3, columns=(
            "pid", "name", "price", "qty", "status"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)

        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.product_Table.xview)
        scrolly.config(command=self.product_Table.yview)

        self.product_Table["show"] = "headings"
        self.product_Table.heading("pid", text="P ID")
        self.product_Table.heading("name", text="NAME")
        self.product_Table.heading("price", text="Price")
        self.product_Table.heading("qty", text="Quantity")
        self.product_Table.heading("status", text="Status")

        self.product_Table["show"] = "headings"
        self.product_Table.column("pid", width=30)
        self.product_Table.column("name", width=90)
        self.product_Table.column("price", width=80)
        self.product_Table.column("qty", width=60)
        self.product_Table.column("status", width=90)

        self.product_Table.pack(fill=BOTH, expand=1)
        self.product_Table.bind("<ButtonRelease-1>", self.get_data)

        lbl_note=Label(ProductFrame1, text="Note: Enter 0 quantity to remove a product from the cart", anchor='w', font=("times new roman", 12), bg="#FFF", fg="#F00")
        lbl_note.pack(side=BOTTOM, fill=X)

        #===========CUSTOMER FRAME==============================
        self.var_cname=StringVar()
        self.var_contact=StringVar()

        CustomerFrame = Frame(self.root, bg="#fff", bd=4, relief=RIDGE)
        CustomerFrame.place(x=420, y=110, width=530, height=70)

        self.cTitle = Label(CustomerFrame, text="Customer Details", font=("times new roman", 15), bg="#e1e1e1",)
        self.cTitle.pack(side=TOP, fill=X)

        lbl_name = Label(CustomerFrame, text="Name", font=("times new roman", 15),bg="white", fg="green")
        lbl_name.place(x=5, y=35)
        txt_name = Entry(CustomerFrame, textvariable=self.var_cname, font=("times new roman", 15), bg="lightgreen")
        txt_name.place(x=80, y=35, width=180)

        lbl_contact = Label(CustomerFrame, text="Contact No", font=("times new roman", 15), bg="white", fg="green")
        lbl_contact.place(x=280, y=35)
        txt_contact = Entry(CustomerFrame, textvariable=self.var_contact, font=("times new roman", 15), bg="lightgreen")
        txt_contact.place(x=380, y=35, width=140)

        #============Calculator  & Cart Frame============================
        cal_cart_frame = Frame(self.root, bg="#fff", bd=4, relief=RIDGE)
        cal_cart_frame.place(x=420, y=190, width=530, height=360)

        #===============calculator frame================
        self.var_cal_input=StringVar()

        cal_frame = Frame(cal_cart_frame, bg="#fff", bd=4, relief=RIDGE)
        cal_frame.place(x=5, y=10, width=268, height=340)

        self.txt_cal_input=Entry(cal_frame, textvariable=self.var_cal_input, font=("Poppins", 15, "bold"), width=19, bd=9, relief=GROOVE, state='readonly', justify=RIGHT)
        self.txt_cal_input.grid(row=0, columnspan=4)

        btn_7=Button(cal_frame,text="7", command=lambda:self.get_input(7), font=("Poppins", 15, "bold"), width=4, bd=3,pady=4, cursor="hand2")
        btn_7.grid(row=1, column=0)
        btn_8 = Button(cal_frame, command=lambda:self.get_input(8), text="8", font=("Poppins", 15, "bold"), width=4, bd=3, pady=4, cursor="hand2")
        btn_8.grid(row=1, column=1)
        btn_9 = Button(cal_frame, command=lambda:self.get_input(9), text="9", font=("Poppins", 15, "bold"), width=4, bd=3, pady=4, cursor="hand2")
        btn_9.grid(row=1, column=2)
        btn_sum = Button(cal_frame, command=lambda:self.get_input('+'), text="+", font=("Poppins", 15, "bold"), width=4, bd=3, pady=4, cursor="hand2")
        btn_sum.grid(row=1, column=3)

        btn_4 = Button(cal_frame, command=lambda:self.get_input(4), text="4", font=("Poppins", 15, "bold"), width=4, bd=3, pady=4, cursor="hand2")
        btn_4.grid(row=2, column=0)
        btn_5 = Button(cal_frame, command=lambda:self.get_input(5), text="5", font=("Poppins", 15, "bold"), width=4, bd=3, pady=4, cursor="hand2")
        btn_5.grid(row=2, column=1)
        btn_6 = Button(cal_frame, command=lambda:self.get_input(6), text="6", font=("Poppins", 15, "bold"), width=4, bd=3, pady=4, cursor="hand2")
        btn_6.grid(row=2, column=2)
        btn_sub= Button(cal_frame, command=lambda:self.get_input('-'), text="-", font=("Poppins", 15, "bold"), width=4, bd=3, pady=4, cursor="hand2")
        btn_sub.grid(row=2, column=3)

        btn_1 = Button(cal_frame, command=lambda:self.get_input(1), text="1", font=("Poppins", 15, "bold"), width=4, bd=3, pady=4, cursor="hand2")
        btn_1.grid(row=3, column=0)
        btn_2 = Button(cal_frame, command=lambda:self.get_input(2), text="2", font=("Poppins", 15, "bold"), width=4, bd=3, pady=4, cursor="hand2")
        btn_2.grid(row=3, column=1)
        btn_3 = Button(cal_frame, command=lambda:self.get_input(3), text="3", font=("Poppins", 15, "bold"), width=4, bd=3, pady=4, cursor="hand2")
        btn_3.grid(row=3, column=2)
        btn_mul = Button(cal_frame, command=lambda:self.get_input('*'), text="*", font=("Poppins", 15, "bold"), width=4, bd=3, pady=4, cursor="hand2")
        btn_mul.grid(row=3, column=3)

        btn_0 = Button(cal_frame, command=lambda:self.get_input(0), text="0", font=("Poppins", 15, "bold"), width=4, bd=3, cursor="hand2")
        btn_0.grid(row=4, column=0)
        btn_c = Button(cal_frame, command=lambda:self.clear_cal(), text="C", font=("Poppins", 15, "bold"), width=4, bd=3,  cursor="hand2")
        btn_c.grid(row=4, column=1)
        btn_eq = Button(cal_frame, command=lambda:self.perform_cal(), text="=", font=("Poppins", 15, "bold"), width=4, bd=3, cursor="hand2")
        btn_eq.grid(row=4, column=2)
        btn_div = Button(cal_frame, command=lambda:self.get_input('/'), text="/", font=("Poppins", 15, "bold"), width=4, bd=3,cursor="hand2")
        btn_div.grid(row=4, column=3)

        #===============cart frame==========================
        cart_Frame = Frame(cal_cart_frame, bd=3, relief=RIDGE)
        cart_Frame.place(x=280, y=8, width=245, height=342)

        self.cTitle = Label(cart_Frame, text="Cart \tTotal Product : 0", font=("times new roman", 15), bg="lightgreen", )
        self.cTitle.pack(side=TOP, fill=X)

        scrolly = Scrollbar(cart_Frame, orient=VERTICAL)
        scrollx = Scrollbar(cart_Frame, orient=HORIZONTAL)

        self.CartTable = ttk.Treeview(cart_Frame, columns=(
            "pid", "name", "price", "qty"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)

        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.CartTable.xview)
        scrolly.config(command=self.CartTable.yview)

        self.CartTable["show"] = "headings"
        self.CartTable.heading("pid", text="P ID")
        self.CartTable.heading("name", text="NAME")
        self.CartTable.heading("price", text="Price")
        self.CartTable.heading("qty", text="QTY")

        self.CartTable["show"] = "headings"
        self.CartTable.column("pid", width=40)
        self.CartTable.column("name", width=100)
        self.CartTable.column("price", width=90)
        self.CartTable.column("qty", width=40)

        self.CartTable.pack(fill=BOTH, expand=1)
        self.CartTable.bind("<ButtonRelease-1>", self.get_data_cart)

        #===========Add Cart Widgets Frame===================
        self.var_pid = StringVar()
        self.var_pname = StringVar()
        self.var_qty = StringVar()
        self.var_price = StringVar()
        self.var_stock = StringVar()

        Add_CartWidgetsFrame = Frame(self.root, bg="#fff", bd=4, relief=RIDGE)
        Add_CartWidgetsFrame.place(x=420, y=550, width=530, height=110)

        lbl_p_name=Label(Add_CartWidgetsFrame, text="Product Name", font=("Times new roman", 15), bg="white")
        lbl_p_name.place(x=5,y=5)
        txt_p_name=Entry(Add_CartWidgetsFrame, textvariable=self.var_pname, font=("Times new roman", 15), state='readonly')
        txt_p_name.place(x=5,y=35, width=190, height=22)

        lbl_p_price = Label(Add_CartWidgetsFrame, text="Price per qty", font=("Times new roman", 15), bg="white")
        lbl_p_price.place(x=230, y=5)
        txt_p_price = Entry(Add_CartWidgetsFrame, textvariable=self.var_price, font=("Times new roman", 15), state='readonly')
        txt_p_price.place(x=230, y=35, width=120, height=22)

        lbl_p_qty = Label(Add_CartWidgetsFrame, text="Quantity", font=("Times new roman", 15), bg="white")
        lbl_p_qty.place(x=390, y=5)
        txt_p_qty = Entry(Add_CartWidgetsFrame, textvariable=self.var_qty, font=("Times new roman", 15), bg="#eee")
        txt_p_qty.place(x=390, y=35, width=120, height=22)

        self.lbl_inStock = Label(Add_CartWidgetsFrame, text="InStock", font=("Times new roman", 15), bg="white")
        self.lbl_inStock.place(x=5, y=70)

        btn_clear_cart=Button(Add_CartWidgetsFrame, command=self.clear_cart, text="Clear", font=("Times new roman", 15,"bold"), bg="#607d8b",fg="#fff", cursor="hand2")
        btn_clear_cart.place(x=180, y=70, width=150, height=30)
        btn_add_cart=Button(Add_CartWidgetsFrame, command=self.add_update_cart, text="Add / Update", font=("Times new roman", 15,"bold"), bg="#4caf50", fg="#fff", cursor="hand2")
        btn_add_cart.place(x=340, y=69, width=180, height=30)

        #============billing area======================
        billFrame=Frame(self.root, bd=2, relief=RIDGE, bg='white')
        billFrame.place(x=953, y=110, width=410, height=410)
        BTitle = Label(billFrame, text="Customer Bill Area", font=("times new roman", 20, "bold"), bg="#FF2626", fg="#FFF")
        BTitle.pack(side=TOP, fill=X)

        scrolly=Scrollbar(billFrame, orient=VERTICAL)
        scrolly.pack(side=RIGHT, fill=Y)

        self.txt_bill_area = Text(billFrame, yscrollcommand=scrolly.set)
        self.txt_bill_area.pack(fill=BOTH, expand=1)

        scrolly.config(command=self.txt_bill_area.yview)

    #========BILLING BUTTONS======================
        billMenuFrame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        billMenuFrame.place(x=953, y=520, width=410, height=140)

        self.lbl_amnt = Label(billMenuFrame, text="Bill Amount\n0", font=("times new roman", 14, "bold"), bg="#3151b5", fg="#FFF")
        self.lbl_amnt.place(x=2, y=5, width=120, height=70)
        self.lbl_discount = Label(billMenuFrame, text="Discount\n5%", font=("times new roman", 14, "bold"), bg="#8bc34a", fg="#FFF")
        self.lbl_discount.place(x=122, y=5, width=120, height=70)
        self.lbl_net_pay = Label(billMenuFrame, text="Net Pay\n0", font=("times new roman", 14, "bold"), bg="#607d8b", fg="#FFF")
        self.lbl_net_pay.place(x=242, y=5, width=160, height=70)

        btn_print = Button(billMenuFrame, command=self.print_bill, text="Print", font=("times new roman", 14, "bold",),bg="#4caf50", fg="#FFF", cursor="hand2")
        btn_print.place(x=2, y=80, width=120, height=50)
        btn_clear_all = Button(billMenuFrame, command=self.clear_all, text="Clear", font=("times new roman", 14, "bold",),bg="#607d8b", fg="#FFF", cursor="hand2")
        btn_clear_all.place(x=122, y=80, width=120, height=50)
        btn_generate = Button(billMenuFrame,command=self.generate_bill,  text="Generate/Save Bill", font=("times new roman", 14, "bold",), bg="#2196f3", fg="#FFF", cursor="hand2")
        btn_generate.place(x=242, y=80, width=160, height=50)

        # ===footer====

        lbl_footer2 = Label(self.root, text="USN: 2AG19CS001 | 2AG19CS002",font=("times new roman", 8), bg="#FFC900", fg="#781C68")
        lbl_footer2.pack(side=BOTTOM, fill=X)
        lbl_footer = Label(self.root, text="Car Inventory Management System | DBMS MINI PROJECT",
                           font=("times new roman", 12), bg="#FFC900", fg="#781C68")
        lbl_footer.pack(side=BOTTOM, fill=X)

        self.show()
        self.update_date_time()
        #self.bill_top()

    #=============ALL Functions=========================================
    def get_input(self,num):
        xnum=self.var_cal_input.get()+str(num)
        self.var_cal_input.set(xnum)

    def clear_cal(self):
        self.var_cal_input.set('')

    def perform_cal(self):
        result=self.var_cal_input.get()
        self.var_cal_input.set(eval(result))

    def show(self):
        con = sqlite3.connect(database=r'car2.db')
        cur = con.cursor()
        #self.productTable = ttk.Treeview(p_Frame, columns=( "pid","supplier","Category","name","price","qty","status"),yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)

        try:
            cur.execute("SELECT pid, name, price, qty, status FROM product where status = 'Active'")
            rows=cur.fetchall()
            self.product_Table.delete(*self.product_Table.get_children())
            for row in rows:
                self.product_Table.insert('', END, values=row)


        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def search(self):
        con = sqlite3.connect(database=r'car2.db')
        cur = con.cursor()
        try:
            if self.var_search.get() == "":
                messagebox.showerror("Error", "Search input should be required", parent=self.root)
            else:
                cur.execute("select pid, name, price, qty, status from product where name LIKE '%"+self.var_search.get() + "%' and status='Active'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.product_Table.delete(*self.product_Table.get_children())
                    for row in rows:
                        self.product_Table.insert('',END, values=row)
                else:
                    messagebox.showerror("Error", "No record found!", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def get_data(self,ev):
        f=self.product_Table.focus()
        content=(self.product_Table.item(f))
        row=content['values']
        self.var_pid.set(row[0])
        self.var_pname.set(row[1])
        self.var_price.set(row[2])
        self.var_qty.set('1')
        self.lbl_inStock.config(text=f"In Stock[{str(row[3])}]")
        self.var_stock.set(row[3])

    def get_data_cart(self,ev):
        f = self.CartTable.focus()
        content = (self.CartTable.item(f))
        row = content['values']
        self.var_pid.set(row[0])
        self.var_pname.set(row[1])
        self.var_price.set(row[2])
        self.var_qty.set(row[3])
        self.lbl_inStock.config(text=f"In Stock[{str(row[4])}]")
        self.var_stock.set(row[4])

    def add_update_cart(self):
        if self.var_pid.get() == "":
            messagebox.showerror("Error", "Please select the product" , parent=self.root)
        elif self.var_qty.get() == "":
            messagebox.showerror("Error", "Please enter the quantity", parent=self.root)
        elif int(self.var_qty.get()) > int(self.var_stock.get()):
            messagebox.showerror("Error", "Invalid Quantity", parent=self.root)

        else:
            #price_cal = (int(self.var_qty.get())*float(self.var_price.get()))
            #price_cal = float(price_cal)
            price_cal = self.var_price.get()
            #pid, name, price, qty, status
            cart_data=[self.var_pid.get(), self.var_pname.get(), price_cal, self.var_qty.get(),self.var_stock.get()]

            #print(self.cart_list)
            #=============UPDATE CART====================
            present = 'no'
            qty_no = 0
            for row in self.cart_list:
                if self.var_pid.get() == row[0]:
                    present = 'yes'
                    break

                qty_no = qty_no + 1


            if present == 'yes':
                op = messagebox.askyesno('Confirm', "Product already present\n Do you want to update or remove", parent=self.root)
                if op==True:
                    if self.var_qty.get()=="0":
                        self.cart_list.pop(qty_no)
                    else:
                        #self.cart_list[qty_no][2] = price_cal #price
                        self.cart_list[qty_no][3] = self.var_qty.get() #qty
            else:
                self.cart_list.append(cart_data)

            self.show_cart()
            self.bill_updates()

    def bill_updates(self):
        self.bill_amnt = 0
        self.net_pay = 0
        self.discount = 0
        for row in self.cart_list:
            self.bill_amnt = self.bill_amnt + (float(row[2])*int(row[3]))

        self.discount = (self.bill_amnt*5)/100
        self.net_pay = self.bill_amnt - self.discount
        self.lbl_amnt.config(text=f'Bill Amount\n{str(self.bill_amnt)}')
        self.lbl_net_pay.config(text=f'Net Pay\n[{str(self.net_pay)}]')
        self.cTitle.config(text=f"Cart \tTotal Product : {str(len(self.cart_list))}")


    def show_cart(self):
        con = sqlite3.connect(database=r'car2.db')
        cur = con.cursor()
        try:
            self.CartTable.delete(*self.CartTable.get_children())
            for row in self.cart_list:
                self.CartTable .insert('', END, values=row)


        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def generate_bill(self):
        if self.var_cname.get() == "" or self.var_contact.get() == "":
            messagebox.showerror("Error", "Customer details are required", parent=self.root)
        elif len(self.cart_list) == 0:
            messagebox.showerror("Error", "Please add products in the cart", parent=self.root)
        else:
            #====Bill Top==============
            self.bill_top()
            #====Bill Middle==============
            self.bill_middle()
            #====Bill Bottom==============
            self.bill_bottom()

            fp = open(f'bill/{str(self.invoice)}.txt','w')
            fp.write(self.txt_bill_area.get('1.0', END))
            fp.close()
            messagebox.showinfo("Saved","Bill has been generated/Saved in backend", parent=self.root)
            self.chk_print = 1


    def bill_top(self):
        self.invoice = int(time.strftime("%H%M%S")) + int(time.strftime("%d%m%Y"))

        bill_top_temp = f'''
\t CAR Inventory Management System
\t Afnan Hudli | Afran Davalbhai
\t   USN:2AG19CS001 | 2AG19CS002
 {str("="*47)}
 Customer Name : {self.var_cname.get()}
 Ph no. :{self.var_contact.get()}
 Bill no. : {str(self.invoice)}\t\tDate: {str(time.strftime("%d/%m/%Y"))}
 {str("="*47)}
 Product Name\t\t\tQTY\tPrice
 {str("="*47)}
        '''
        self.txt_bill_area.delete('1.0', END)
        self.txt_bill_area.insert('1.0', bill_top_temp)

    def bill_bottom(self):
        bill_bottom_temp = f'''
 {str("="*47)}
 Bill Amount\t\t\t\tRs.{self.bill_amnt}
 Discount\t\t\t\tRs.{self.discount}
 Net Pay\t\t\t\tRs.{self.net_pay}
 {str("="*47)}        
        '''
        self.txt_bill_area.insert(END, bill_bottom_temp)

    def bill_middle(self):
        con = sqlite3.connect(database=r'car2.db')
        cur = con.cursor()
        try:
            for row in self.cart_list:
                pid = row[0]
                name = row[1]
                qty = int(row[4]) - int(row[3])
                if int(int(row[3])) == int(row[4]):
                    status = "Inactive"
                if int(int(row[3])) != int(row[4]):
                    status = "Active"
                price = float(row[2])*int(row[3])
                price = str(price)
                self.txt_bill_area.insert(END, "\n "+name+"\t\t\t"+row[3]+"\tRs."+price)
            #============ update qty in product table ======================
                cur.execute("Update product set qty=?, status=? where pid=?", (
                    qty,
                    status,
                    pid
                ))
                con.commit()
            con.close()
            self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def clear_cart(self):
        f = self.CartTable.focus()
        content = (self.CartTable.item(f))
        row = content['values']
        self.var_pid.set('')
        self.var_pname.set('')
        self.var_price.set('')
        self.var_qty.set('')
        self.lbl_inStock.config(text=f"In Stock")
        self.var_stock.set('')
        self.cTitle.config(text=f"Cart \tTotal Product : 0")

    def clear_all(self):
        del self.cart_list[:]
        self.var_cname.set('')
        self.var_contact.set('')
        self.txt_bill_area.delete('1.0', END)
        self.var_search.set('')

        self.clear_cart()
        self.show()
        self.show_cart()

    def update_date_time(self):
        time_ = time.strftime("%I:%M:%S")
        date_ = time.strftime("%d-%m-%Y")
        self.lbl_clock.config(text=f"Developed by Afran & Afnan\t\t Date: {str(date_)}\t\t  Time: {str(time_)}", font=("times new roman", 15), bg="#FFC900", fg="#781C68")
        self.lbl_clock.after(200,self.update_date_time)

    def print_bill(self):
        if self.chk_print == 1:
            messagebox.showinfo("Print", "Please wait while printing", parent=self.root)
            new_file = tempfile.mktemp('.txt')
            open(new_file, 'w').write(self.txt_bill_area.get('1.0', END))
            os.startfile(new_file, 'print')
        else:
            messagebox.showerror("Print", "Please generate a bill to print the receipt", parent=self.root)

    def logout(self):
        self.root.destroy()
        os.system("python login.py")



if __name__ == "__main__":
    root = Tk()
    obj = BillClass(root)
    root.mainloop()
