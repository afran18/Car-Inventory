from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3


class categoryClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.title("Car Inventory Management System | Developed my Afran & Afnan")
        self.root.config(bg="#fff")
        self.root.focus_force()
        #===========Variables============
        self.var_cat_id=StringVar()
        self.var_name=StringVar()

        #=======title==============
        lbl_title=Label(self.root, text="Product Category", font=("Times new roman", 25), bg="#184a45", fg="#fff", bd=3, relief=RIDGE)
        lbl_title.pack(side=TOP, fill=X, padx=10, pady=20)
        
        #=========categories=============================
        
        lbl_name=Label(self.root, text="Oils & Fuels", font=("Poppins", 15), bg="#8E05C2", fg="#fff")
        lbl_name.place(x=10,y=100, width=250, height=60)
        
        lbl_name=Label(self.root, text="Brake System", font=("Poppins", 15), bg="#8E05C2", fg="#fff")
        lbl_name.place(x=10,y=180, width=250, height=60)
        
        lbl_name=Label(self.root, text="Filters", font=("Poppins", 15), bg="#8E05C2", fg="#fff")
        lbl_name.place(x=10,y=260, width=250, height=60)
        
        lbl_name=Label(self.root, text="Head Lamp", font=("Poppins", 15), bg="#8E05C2", fg="#fff")
        lbl_name.place(x=10,y=340, width=250, height=60)
        
        lbl_name=Label(self.root, text="Rear Lamps", font=("Poppins", 15), bg="#8E05C2", fg="#fff")
        lbl_name.place(x=10,y=420, width=250, height=60)
        
        
        lbl_name=Label(self.root, text="Clutch System", font=("Poppins", 15), bg="#FF008E", fg="#fff")
        lbl_name.place(x=280,y=100, width=250, height=60)
        
        lbl_name=Label(self.root, text="Suspension", font=("Poppins", 15), bg="#FF008E", fg="#fff")
        lbl_name.place(x=280,y=180, width=250, height=60)
        
        lbl_name=Label(self.root, text="Body Parts", font=("Poppins", 15), bg="#FF008E", fg="#fff")
        lbl_name.place(x=280,y=260, width=250, height=60)
        
        lbl_name=Label(self.root, text="Engine Parts", font=("Poppins", 15), bg="#FF008E", fg="#fff")
        lbl_name.place(x=280,y=340, width=250, height=60)
        
        lbl_name=Label(self.root, text="Exhaust System", font=("Poppins", 15), bg="#FF008E", fg="#fff")
        lbl_name.place(x=280,y=420, width=250, height=60)
        
        
    
        
        
        lbl_name=Label(self.root, text="Transmission", font=("Poppins", 15), bg="#8E05C2", fg="#fff")
        lbl_name.place(x=550,y=100, width=250, height=60)
        
        lbl_name=Label(self.root, text="Fasteners", font=("Poppins", 15), bg="#8E05C2", fg="#fff")
        lbl_name.place(x=550,y=180, width=250, height=60)
        
        lbl_name=Label(self.root, text="Fuel System", font=("Poppins", 15), bg="#8E05C2", fg="#fff")
        lbl_name.place(x=550,y=260, width=250, height=60)
        
        lbl_name=Label(self.root, text="Gasket & Seals", font=("Poppins", 15), bg="#8E05C2", fg="#fff")
        lbl_name.place(x=550,y=340, width=250, height=60)
        
        lbl_name=Label(self.root, text="Interior & Safety", font=("Poppins", 15), bg="#8E05C2", fg="#fff")
        lbl_name.place(x=550,y=420, width=250, height=60)
        
        
        
        lbl_name=Label(self.root, text="Steering", font=("Poppins", 15), bg="#FF008E", fg="#fff")
        lbl_name.place(x=820,y=100, width=250, height=60)
        
        lbl_name=Label(self.root, text="Wheels & Tyres", font=("Poppins", 15), bg="#FF008E", fg="#fff")
        lbl_name.place(x=820,y=180, width=250, height=60)
        
        lbl_name=Label(self.root, text="Belts & Chains", font=("Poppins", 15), bg="#FF008E", fg="#fff")
        lbl_name.place(x=820,y=260, width=250, height=60)
        
        lbl_name=Label(self.root, text="Windscreen & Cleaning", font=("Poppins", 15), bg="#FF008E", fg="#fff")
        lbl_name.place(x=820,y=340, width=250, height=60)
        
        lbl_name=Label(self.root, text="Cooling System", font=("Poppins", 15), bg="#FF008E", fg="#fff")
        lbl_name.place(x=820,y=420, width=250, height=60)
        
        
        

        


    #==========FUNCTION=======================

    

if __name__ == "__main__":
    root = Tk()
    obj = categoryClass(root)
    root.mainloop()

