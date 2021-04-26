from tkinter import*
import math,random
from tkinter import messagebox
import os
class Bill_App:
    def __init__(self,root):
        self.root=root
        width= root.winfo_screenwidth() 
        height= root.winfo_screenheight()
        self.root.geometry("%dx%d" % (width, height))
        self.root.title("Billing Software")
        bg_color="#081832"
        title = Label(self.root, text="Billing Software",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill=X)

        # variables###

        #cosmetics
        self.soap = IntVar()
        self.face_cream = IntVar()
        self.face_wash=IntVar()
        self.spray=IntVar()
        self.lotion=IntVar()
        self.gell=IntVar()

        #grocery
        self.rice=IntVar()
        self.food_oil=IntVar()
        self.daal=IntVar()
        self.wheat = IntVar()
        self.sugar = IntVar()
        self.tea=IntVar()

        #cold Drinks
        self.maza=IntVar()
        self.cock=IntVar()
        self.frooti=IntVar()
        self.Red_Bull=IntVar()
        self.limca=IntVar()
        self.sprite=IntVar()

        # Total Product Price & Tax Variables
        self.cosmetics_price=StringVar()
        self.grocery_price=StringVar()
        self.cold_drinks=StringVar()

        self.cosmetics_tax=StringVar()
        self.grocery_tax=StringVar()
        self.cold_drinks_tax=StringVar()
        
        # Customer
        self.C_name=StringVar()
        self.c_phone=StringVar()
        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill=StringVar()



        # Customer Details frame
        F1 = LabelFrame(self.root,bd=10,relief=GROOVE,text="Customer Details",font=("Times new roman",15,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=88,relwidth=1)
        
        cname_lbl = Label(F1,text="Customer Name",bg=bg_color,fg="white",font=("Times new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_text = Entry(F1,width=15,textvariable=self.C_name, font="aerial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=5)

        cphn_lbl = Label(F1,text="Phone No.",bg=bg_color,fg="white",font=("Times new roman",18,"bold")).grid(row=0,column=2,padx=20,pady=5)
        cphn_text = Entry(F1,width=15,textvariable=self.c_phone, font="aerial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=5)

        c_bill_lbl = Label(F1,text="Bill No.",bg=bg_color,fg="white",font=("Times new roman",18,"bold")).grid(row=0,column=4,padx=20,pady=5)
        c_bill_text = Entry(F1,width=15,textvariable=self.search_bill, font="aerial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,padx=10,pady=5)

        bill_btn = Button(F1, text="Search",command=self.find_bill,width=10,bd=7, font ="aerial 12 bold").grid(row=0, column=6,pady=10,padx=50)

        #cosmetics Frame
        F2 = LabelFrame(self.root,bd=10,relief=GROOVE,text="Cosmatics",font=("Times new roman",15,"bold"),fg="gold",bg=bg_color)
        F2.place(x=5,y=200,width=325,height=380)

        bath_lbl = Label(F2,text="Bath Soap",font=("times new roman",16,"bold"),bg=bg_color,fg="lightblue").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        bath_text = Entry(F2,width=10,textvariable=self.soap,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        face_cream = Label(F2,text="Face Cream",font=("times new roman",16,"bold"),bg=bg_color,fg="lightblue").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        face_cream = Entry(F2,width=10,textvariable=self.face_cream,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        hair_s = Label(F2,text="Hair Spray",font=("times new roman",16,"bold"),bg=bg_color,fg="lightblue").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        hair_s = Entry(F2,width=10,textvariable=self.spray,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        hair_g = Label(F2,text="Hair Gell",font=("times new roman",16,"bold"),bg=bg_color,fg="lightblue").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        hair_g = Entry(F2,width=10,textvariable=self.gell,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        body = Label(F2,text="Body Lotion",font=("times new roman",16,"bold"),bg=bg_color,fg="lightblue").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        body = Entry(F2,width=10,textvariable=self.lotion,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        Face_w = Label(F2,text="Face Wash",font=("times new roman",16,"bold"),bg=bg_color,fg="lightblue").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        Face_w = Entry(F2,width=10,textvariable=self.face_wash,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        #Grocery Frame
        F3 = LabelFrame(self.root,bd=10,relief=GROOVE,text="Grocery",font=("Times new roman",15,"bold"),fg="gold",bg=bg_color)
        F3.place(x=340,y=200,width=325,height=380)

        G1 = Label(F3,text="Rice",font=("times new roman",16,"bold"),bg=bg_color,fg="lightblue").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        G1 = Entry(F3,width=10,textvariable=self.rice,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        G2 = Label(F3,text="Food Oil",font=("times new roman",16,"bold"),bg=bg_color,fg="lightblue").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        G2 = Entry(F3,width=10,textvariable=self.food_oil,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        G3 = Label(F3,text="Daal",font=("times new roman",16,"bold"),bg=bg_color,fg="lightblue").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        G3 = Entry(F3,width=10,textvariable=self.daal,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        G4 = Label(F3,text="Wheat",font=("times new roman",16,"bold"),bg=bg_color,fg="lightblue").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        G4 = Entry(F3,width=10,textvariable=self.wheat,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        G5 = Label(F3,text="Sugar",font=("times new roman",16,"bold"),bg=bg_color,fg="lightblue").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        G5 = Entry(F3,width=10,textvariable=self.sugar,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        G6 = Label(F3,text="Tea",font=("times new roman",16,"bold"),bg=bg_color,fg="lightblue").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        G6 = Entry(F3,width=10,textvariable=self.tea,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        #Cold Drinks

        F4 = LabelFrame(self.root,bd=10,relief=GROOVE,text="Cold Drinks",font=("Times new roman",15,"bold"),fg="gold",bg=bg_color)
        F4.place(x=680,y=200,width=325,height=380)

        C1 = Label(F4,text="Sprite",font=("times new roman",16,"bold"),bg=bg_color,fg="lightblue").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        C1 = Entry(F4,width=10,textvariable=self.sprite,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        C2 = Label(F4,text="Maza",font=("times new roman",16,"bold"),bg=bg_color,fg="lightblue").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        C2 = Entry(F4,width=10,textvariable=self.maza,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        C3 = Label(F4,text="Cock",font=("times new roman",16,"bold"),bg=bg_color,fg="lightblue").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        C3 = Entry(F4,width=10,textvariable=self.cock,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        C4 = Label(F4,text="Limca",font=("times new roman",16,"bold"),bg=bg_color,fg="lightblue").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        C4 = Entry(F4,width=10,textvariable=self.limca,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        C5 = Label(F4,text="Frooti",font=("times new roman",16,"bold"),bg=bg_color,fg="lightblue").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        C5 = Entry(F4,width=10,textvariable=self.frooti,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        C6 = Label(F4,text="RedBull",font=("times new roman",16,"bold"),bg=bg_color,fg="lightblue").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        C6 = Entry(F4,width=10,textvariable=self.Red_Bull,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        # Bill Area

        F5 = Frame(self.root,bd=10,relief=GROOVE)
        F5.place(x=1050,y=205,width=340,height=380)
        bill_title = Label(F5,text="Bill area",font="aerial 15 bold", bd=7, relief=GROOVE).pack(fill=X)
        scrol_y = Scrollbar(F5, orient=VERTICAL)
        self.textarea = Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.textarea.yview)
        self.textarea.pack()

        #button frame

        F6 = LabelFrame(self.root,bd=10,relief=GROOVE,text="Bill Menu",font=("Times new roman",15,"bold"),fg="gold",bg=bg_color)
        F6.place(x=0,y=595,relwidth=1,height=240)
        
        m1_lbl = Label(F6, text="Total Cosmetics Price",bg=bg_color,fg="lightblue",font=("time new riman",14,"bold")).grid(row=0,column=0,padx=20,pady=20,sticky="w")
        m1_entry = Entry(F6,width=18,textvariable=self.cosmetics_price,font="aerial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

        m2_lbl = Label(F6, text="Total Grocery Price",bg=bg_color,fg="lightblue",font=("time new riman",14,"bold")).grid(row=1,column=0,padx=20,pady=20,sticky="w")
        m2_entry = Entry(F6,width=18,textvariable=self.grocery_price,font="aerial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)

        m3_lbl = Label(F6, text="Total Cold DRinks Price",bg=bg_color,fg="lightblue",font=("time new riman",14,"bold")).grid(row=2,column=0,padx=20,pady=10,sticky="w")
        m3_entry = Entry(F6,width=18,textvariable=self.cold_drinks,font="aerial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)

        c1_lbl = Label(F6, text="Cosmetics Tax",bg=bg_color,fg="lightblue",font=("time new riman",14,"bold")).grid(row=0,column=2,padx=20,pady=20,sticky="w")
        c1_entry = Entry(F6,width=18,textvariable=self.cosmetics_tax,font="aerial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)

        c2_lbl = Label(F6, text="Grocery Tax",bg=bg_color,fg="lightblue",font=("time new riman",14,"bold")).grid(row=1,column=2,padx=20,pady=20,sticky="w")
        c2_entry = Entry(F6,width=18,textvariable=self.grocery_tax,font="aerial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)

        c3_lbl = Label(F6, text="Cold Drinks Tax",bg=bg_color,fg="lightblue",font=("time new riman",14,"bold")).grid(row=2,column=2,padx=20,pady=20,sticky="w")
        c3_entry = Entry(F6,width=18,textvariable=self.cold_drinks_tax,font="aerial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)

        btn_f = Frame(F6, bd=7, relief=GROOVE)
        btn_f.place(x=840,y=40,width=580,height=105)

        total_btn = Button(btn_f,command=self.total,text="Total",bg="cadetblue",fg="white",pady=17,width=11,font="aerial 14").grid(row=0,column=0,padx=5,pady=7)
        gbill_btn = Button(btn_f,text="Generate Bill",command=self.bill_area,bg="cadetblue",fg="white",pady=17,width=11,font="aerial 14").grid(row=0,column=1,padx=5,pady=7)
        Clear_btn = Button(btn_f,text="Clear",command=self.clear,bg="cadetblue",fg="white",pady=17,width=11,font="aerial 14").grid(row=0,column=2,padx=5,pady=7)
        Exit_btn = Button(btn_f,text="Exit",command=self.exit,bg="cadetblue",fg="white",pady=17,width=11,font="aerial 14").grid(row=0,column=3,padx=5,pady=7)
        self.welcome_bill()

    def total(self):
        self.c_s_p=self.soap.get()*40
        self.c_fc_p=self.face_cream.get()*120
        self.c_fw_p=self.face_wash.get()*60
        self.c_hs_p=self.spray.get()*90
        self.c_hg_p=self.gell.get()*180
        self.c_bl_p=self.lotion.get()*99
        self.total_cosmetic_price=float(
                                        self.c_s_p+
                                        self.c_fc_p+
                                        self.c_fw_p+
                                        self.c_hs_p+
                                        self.c_hg_p+
                                        self.c_bl_p
                                        )
        self.cosmetics_price.set("Rs. "+str(self.total_cosmetic_price))
        self.c_tax=round((self.total_cosmetic_price*0.05),2)
        self.cosmetics_tax.set("Rs. "+str(self.c_tax))

        self.g_r_p=self.rice.get()*40
        self.g_f_p=self.food_oil.get()*180
        self.g_d_p=self.daal.get()*60
        self.g_w_p=self.wheat.get()*240
        self.g_s_p=self.sugar.get()*45
        self.g_t_p=self.tea.get()*150
        self.total_grocery_price=float(
                                        self.g_r_p+
                                        self.g_f_p+
                                        self.g_d_p+
                                        self.g_w_p+
                                        self.g_s_p+
                                        self.g_t_p
                                        )
        self.grocery_price.set("Rs. "+str(self.total_grocery_price))
        self.g_tax=round((self.total_grocery_price*0.1),2)
        self.grocery_tax.set("Rs. "+str(self.g_tax))

        self.d_f_p=self.frooti.get()*80
        self.d_m_p=self.maza.get()*80
        self.d_s_p=self.sprite.get()*70
        self.d_r_p=self.Red_Bull.get()*150
        self.d_l_p=self.limca.get()*70
        self.d_c_p=self.cock.get()*80
        self.total_drinks_price=float(
                                       self.d_f_p+
                                       self.d_m_p+
                                       self.d_s_p+
                                       self.d_r_p+
                                       self.d_l_p+
                                       self.d_c_p
                                        )
        self.cold_drinks.set("Rs. "+str(self.total_drinks_price))
        self.cd_tax=round((self.total_drinks_price*0.05),2)
        self.cold_drinks_tax.set("Rs. "+str(self.cd_tax))

        #total bill
        self.total_p = self.total_cosmetic_price+self.total_grocery_price+self.total_drinks_price
        self.total_t = self.c_tax+self.g_tax+self.cd_tax
        self.total_bill = self.total_p+self.total_t


    def welcome_bill(self):
        self.textarea.delete('1.0',END)
        self.textarea.insert(END,"\t\tWelcome ")
        self.textarea.insert(END,f"\nBill No: {self.bill_no.get()}")
        self.textarea.insert(END,f"\nCusotmer Name: {self.C_name.get()}")
        self.textarea.insert(END,f"\nPhone No: {self.c_phone.get()}")
        self.textarea.insert(END,f"\n=====================================")
        self.textarea.insert(END,f"\n Products\t\tQTY\t\tPrice")
        self.textarea.insert(END,f"\n=====================================")

    def bill_area(self):
        if self.C_name.get()=="" or self.c_phone.get()=="":
            messagebox.showerror("Error","Customer details are must")
        elif self.cosmetics_price.get()=="Rs. 0.0" and self.grocery_price.get()=="Rs. 0.0" and self.cold_drinks.get()=="Rs. 0.0":
            messagebox.showerror("Error","No product purchased")
        
        else:
            self.welcome_bill()
            #cosmetics
            if self.soap.get()!=0:
                self.textarea.insert(END,f"\n Bath Soap\t\t{self.soap.get()}\t\t{self.c_s_p}")

            if self.face_cream.get()!=0:
                self.textarea.insert(END,f"\n Face Cream\t\t{self.face_cream.get()}\t\t{self.c_fc_p}")
        
            if self.spray.get()!=0:
                self.textarea.insert(END,f"\n Hair Spray\t\t{self.spray.get()}\t\t{self.c_hs_p}")
            
            if self.gell.get()!=0:
                self.textarea.insert(END,f"\n Hair Gell\t\t{self.gell.get()}\t\t{self.c_hg_p}")

            if self.lotion.get()!=0:
                self.textarea.insert(END,f"\n Body Lotion\t\t{self.lotion.get()}\t\t{self.c_bl_p}")

            if self.face_wash.get()!=0:
                self.textarea.insert(END,f"\n Face Wash\t\t{self.face_wash.get()}\t\t{self.c_fw_p}")

            #grocery
            if self.rice.get()!=0:
                self.textarea.insert(END,f"\n Rice\t\t{self.rice.get()}\t\t{self.g_r_p}")

            if self.food_oil.get()!=0:
                self.textarea.insert(END,f"\n Food Oil\t\t{self.food_oil.get()}\t\t{self.g_f_p}")
        
            if self.daal.get()!=0:
                self.textarea.insert(END,f"\n Daal\t\t{self.daal.get()}\t\t{self.g_d_p}")
            
            if self.wheat.get()!=0:
                self.textarea.insert(END,f"\n Wheat\t\t{self.wheat.get()}\t\t{self.g_w_p}")

            if self.sugar.get()!=0:
                self.textarea.insert(END,f"\n Sugar\t\t{self.sugar.get()}\t\t{self.g_s_p}")

            if self.tea.get()!=0:
                self.textarea.insert(END,f"\n Tea \t\t{self.tea.get()}\t\t{self.g_t_p}")

            #cold_drinks
            if self.sprite.get()!=0:
                self.textarea.insert(END,f"\n Sprite\t\t{self.sprite.get()}\t\t{self.d_s_p}")

            if self.maza.get()!=0:
                self.textarea.insert(END,f"\n Maza\t\t{self.maza.get()}\t\t{self.d_m_p}")
        
            if self.cock.get()!=0:
                self.textarea.insert(END,f"\n Cock\t\t{self.cock.get()}\t\t{self.d_c_p}")
            
            if self.limca.get()!=0:
                self.textarea.insert(END,f"\n Limca\t\t{self.limca.get()}\t\t{self.d_l_p}")

            if self.frooti.get()!=0:
                self.textarea.insert(END,f"\n Frooti\t\t{self.frooti.get()}\t\t{self.d_f_p}")

            if self.Red_Bull.get()!=0:
                self.textarea.insert(END,f"\n Red Bull\t\t{self.Red_Bull.get()}\t\t{self.d_r_p}")

            self.textarea.insert(END,f"\n=====================================")
            if self.cosmetics_tax.get()!="Rs. 0.0":
                self.textarea.insert(END,f"\n Cosmetics Tax\t\t\t{self.cosmetics_tax.get()}")

            if self.grocery_tax.get()!="Rs. 0.0":
                self.textarea.insert(END,f"\n Grocery Tax\t\t\t{self.grocery_tax.get()}")
            
            if self.cold_drinks_tax.get()!="Rs. 0.0":
                self.textarea.insert(END,f"\n Cold Drink Tax\t\t\t{self.cold_drinks_tax.get()}")
            self.textarea.insert(END,f"\n=====================================")
            self.textarea.insert(END,f"\n Total Bill:\t\t\tRs. {self.total_bill}")
            self.textarea.insert(END,f"\n=====================================")
            self.save_bill()

    def save_bill(self):
        op = messagebox.askyesno("Save","Save Bill ?")
        if op>0:
            self.bill_data = self.textarea.get("1.0",END)
            f1 = open("bills/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved","Saved Successfully")
        else: 
            return
        
    def find_bill(self):
        present="no"
        for i in os.listdir("bills/"):
            if i.split(".")[0]==self.search_bill.get():
                f1 = open(f"bills/{i}","r")
                self.textarea.delete('1.0',END)
                for t in f1:
                    self.textarea.insert(END,t)
                f1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("Error","Invalid Bill No.")
    
    def clear(self):
        op=messagebox.askyesno("Clear","Do you want to clear?")
        if op>0:
            # variables###

            #cosmetics
            self.soap.set(0)
            self.face_cream.set(0)
            self.face_wash.set(0)
            self.spray.set(0)
            self.lotion.set(0)
            self.gell.set(0)

            #grocery
            self.rice.set(0)
            self.food_oil.set(0)
            self.daal.set(0)
            self.wheat.set(0)
            self.sugar.set(0)
            self.tea.set(0)

            #cold Drinks
            self.maza.set(0)
            self.cock.set(0)
            self.frooti.set(0)
            self.Red_Bull.set(0)
            self.limca.set(0)
            self.sprite.set(0)

            # Total Product Price & Tax Variables
            self.cosmetics_price.set("")
            self.grocery_price.set("")
            self.cold_drinks.set("")

            self.cosmetics_tax.set("")
            self.grocery_tax.set("")
            self.cold_drinks_tax.set("")
            
            # Customer
            self.C_name.set("")
            self.c_phone.set("")
            self.bill_no.set("")
            x=random.randint(1000,9999)
            self.bill_no.set(str(x))
            self.search_bill.set("")
            self.welcome_bill()

    def exit(self):
        op=messagebox.askyesno("Exit","Do you want to exit?")
        if op>0:
            self.root.destroy()
root = Tk()
obj = Bill_App(root)
root.mainloop()