from tkinter import*
from PIL import Image,ImageTk
import sqlite3
from tkinter import messagebox
import time
import os


from employee import employeeClass
from category import categoryClass
from supplier import supplierClass
from products import productClass
from sales import salesClass


class car:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1580x800+0+0")
        self.root.title("Car Inventory Management System | Developed my Afran & Afnan")


        #===title====
        self.icon_title=PhotoImage(file="images/logo1.png")
        title=Label(self.root, text="Car Inventory Database System", image=self.icon_title, compound=LEFT, font=("poppins",30,"bold"), bg="#1C0C5B", fg="#fff", anchor="w", padx=20).place(x=0,y=0, relwidth=1,height=70)


        #===BUTTON===
        btn_logout = Button(self.root, command=self.logout, text="Logout",font=("poppins", 15, "bold"), bg="red", fg="white", cursor="hand2", relief="ridge").place(x=1200, y= 10, height=50, width=110)

        # ===clock====
        self.lbl_clock = Label(self.root, text="Developed by Afran & Afnan\t\t Date: DD-MM-YYYY\t\t  Time: HH:MM::SS", font=("times new roman", 15), bg="#FFC900", fg="#781C68")
        self.lbl_clock.place(x=0, y=70, relwidth=1, height=30)


        #===MENU====
        self.MenuLogo=Image.open("images/menu_im.png")
        self.MenuLogo=self.MenuLogo.resize((200,180),Image.ANTIALIAS)
        self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)



        LeftMenu=Frame(self.root, bd=2, relief=RIDGE, bg="#FFF")
        LeftMenu.place(x=0,y=102, width=200, height=620)

        lbl_menuLogo=Label(LeftMenu, image=self.MenuLogo)
        lbl_menuLogo.pack(side=TOP,fill=X)

        self.icon_side=PhotoImage(file="images/side.png")
        lbl_menu=Label(LeftMenu, text="MENU", font=("poppins", 20, "bold"),bg="#009688").pack(side=TOP, fill=X)
        btn_employee = Button(LeftMenu, command=self.employee, text="Employee", image=self.icon_side, compound=LEFT, padx=5, anchor="w", font=("poppins", 15, "bold"), bg="white", fg="black", bd=3, cursor="hand2").pack(side=TOP, fill=X)
        btn_supplier = Button(LeftMenu, command=self.supplier, text="Supplier", image=self.icon_side, compound=LEFT, padx=5, anchor="w",font=("poppins", 15, "bold"), bg="white", fg="black", bd=3, cursor="hand2").pack(side=TOP,fill=X)
        btn_category = Button(LeftMenu, command=self.category, text="Category", image=self.icon_side, compound=LEFT, padx=5, anchor="w",font=("poppins", 15, "bold"), bg="white", fg="black", bd=3, cursor="hand2").pack(side=TOP,fill=X)
        btn_product = Button(LeftMenu, command=self.product, text="Products", image=self.icon_side, compound=LEFT, padx=5, anchor="w",font=("poppins", 15, "bold"), bg="white", fg="black", bd=3, cursor="hand2").pack(side=TOP,fill=X)
        btn_sales = Button(LeftMenu, command=self.sales, text="Sales", image=self.icon_side, compound=LEFT, padx=5, anchor="w",font=("poppins", 15, "bold"), bg="white", fg="black", bd=3, cursor="hand2").pack(side=TOP,fill=X)
        btn_exit = Button(LeftMenu, command=self.exit, text="Exit", image=self.icon_side, compound=LEFT, padx=5, anchor="w",font=("poppins", 15, "bold"), bg="white", fg="black", bd=3, cursor="hand2").pack(side=TOP,fill=X)

        #====CONTENT=====

        self.lbl_employee=Label(self.root,text="Total Employees\n [ 0 ]",font=("times new roman", 20, "bold"),bg="#D83A56", fg="white", bd=5, relief="ridge", cursor="hand2")
        self.lbl_employee.place(x=300, y=120, height= 150, width=300)

        self.lbl_supplier = Label(self.root, text="Total Suppliers\n [ 0 ]", font=("times new roman", 20, "bold"),bg="#33bbf9", fg="white", bd=5, relief="ridge", cursor="hand2")
        self.lbl_supplier.place(x=650, y=120, height=150, width=300)

        self.lbl_category = Label(self.root, text="Total Categories\n [ 0 ]", font=("times new roman", 20, "bold"),bg="#FFD523", fg="white", bd=5, relief="ridge", cursor="hand2")
        self.lbl_category.place(x=1000, y=120, height=150, width=300)

        self.lbl_product = Label(self.root, text="Total Products\n [ 0 ]", font=("times new roman", 20, "bold"),bg="#F8A488", fg="white", bd=5, relief="ridge", cursor="hand2")
        self.lbl_product.place(x=300, y=320, height=150, width=300)

        self.lbl_sales= Label(self.root, text="Total Sales\n [ 0 ]", font=("times new roman", 20, "bold"),bg="#01937C", fg="white", bd=5, relief="ridge", cursor="hand2")
        self.lbl_sales.place(x=650, y=320, height=150, width=300)
        # ===animation images===============
        self.im1 = ImageTk.PhotoImage(file="images/bmw.png")
        self.im2 = ImageTk.PhotoImage(file="images/mclaren.png")
        self.im3 = ImageTk.PhotoImage(file="images/huracan.png")

        self.lbl_change_image = Label(self.root)
        self.lbl_change_image.place(x=800, y=500, width=680, height=270)
        self.animate_image()



        # ===footer====
        lbl_footer = Label(self.root, text="Car Inventory Management System | DBMS MINI PROJECT",font=("times new roman", 15), bg="#FFC900", fg="#781C68").pack(side=BOTTOM, fill=X)
        self.update_date_time()
        self.update_content()
#==========================================================================================================

    def employee(self):
         self.new_win=Toplevel(self.root)
         self.new_obj=employeeClass(self.new_win)

    def supplier(self):
         self.new_win=Toplevel(self.root)
         self.new_obj=supplierClass(self.new_win)

    def category(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = categoryClass(self.new_win)

    def product(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = productClass(self.new_win)

    def sales(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = salesClass(self.new_win)

    def update_date_time(self):
        time_ = time.strftime("%I:%M:%S")
        date_ = time.strftime("%d-%m-%Y")
        self.lbl_clock.config(text=f"Developed by Afran & Afnan\t\t Date: {str(date_)}\t\t  Time: {str(time_)}", font=("times new roman", 15), bg="#FFC900", fg="#781C68")
        self.lbl_clock.after(200,self.update_date_time)

    def update_content(self):
        con = sqlite3.connect(database=r'car2.db')
        cur = con.cursor()
        try:
            cur.execute("select * from product")
            product = cur.fetchall()
            self.lbl_product.config(text = f'Total Products\n[{str(len(product))}]')

            cur.execute("select * from supplier")
            supplier = cur.fetchall()
            self.lbl_supplier.config(text=f'Total Suppliers\n[{str(len(supplier))}]')

            cur.execute("select * from category")
            category = cur.fetchall()
            self.lbl_category.config(text=f'Total Categories\n[{str(len(category))}]')

            cur.execute("select * from employee")
            employee = cur.fetchall()
            self.lbl_employee.config(text=f'Total Employees\n[{str(len(employee))}]')
            bill = len(os.listdir('bill'))
            self.lbl_sales.config(text=f"Total Sales\n[{str(bill)}]")
            self.lbl_clock.after(200, self.update_content)
        except Exception as ex:
            pass


    def animate_image(self):
        self.im = self.im1
        self.im1 = self.im2
        self.im2 = self.im3
        self.im3 = self.im
        self.lbl_change_image.config(image=self.im)
        self.lbl_change_image.after(2000, self.animate_image)

    def logout(self):
        self.root.destroy()
        os.system("python login.py")

    def exit(self):
        self.root.destroy()

if __name__=="__main__":
    root = Tk()
    obj = car(root)
    root.mainloop()

