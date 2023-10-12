from tkinter import *
from math import ceil
from tkinter import messagebox as msg
import datetime
import os
import mysql.connector

def db_connect():
    return mysql.connector.connect(host = "localhost",user="root", password="",database="tkinter_db")

def dbstore():
    conn = db_connect()
    cursor = conn.cursor()
    query = "insert into customer(name,mobile,total) values(%s,%s,%s)"
    args = (e_cusname.get(),e_phno.get(),ceil(total))
    cursor.execute(query,args)
    conn.commit()

bill_num = 0
def updatebill():
    '''update bill number automatically'''
    global bill_num
    bill_num += 1
    e_bill.config(text=f'{bill_num}')

def savebill():
    '''save bill function saves bill in txt file'''
    result = msg.askyesno("Save Status", "Do You want to save the bill")
    if result:
        bill_data = textarea.get(1.0, 'end')
        date = datetime.datetime.now()
        folder_name = date.strftime('%d_%m_%Y')

        # Create the full path to the folder
        folder_path = os.path.join("Supermarket_bills", folder_name)

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)  # Creates the folder and any missing parent directories

        file_name = f'{folder_path}/{folder_name}_{bill_num}.txt'
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(bill_data)
        msg.showinfo("Save Status", "Bill Saved Successfully")

#clear button function
def clear():
    '''clear all inputs and text area'''
    e_cusname.delete(0,'end')
    e_phno.delete(0,'end')
    e_body_products.delete(0,'end')
    e_body_tax.delete(0,'end')
    e_bathsoap.delete(0,'end')
    e_bodylotion.delete(0,'end')
    e_hairoil.delete(0,'end')
    e_fashwash.delete(0,'end')
    e_hairshampoo.delete(0,'end')
    e_grocery_products.delete(0,'end')
    e_grocery_tax.delete(0,'end')
    e_Wheatflour.delete(0,'end')
    e_Rice.delete(0,'end')
    e_Sugar.delete(0,'end')
    e_Washing_powder.delete(0,'end')
    e_cooking_oil.delete(0,'end')
    e_coke.delete(0,'end')
    e_cocacola.delete(0,'end')
    e_fanta.delete(0,'end')
    e_softdrinks_tax.delete(0,'end')
    e_softdrinks_products.delete(0,'end')
    e_Maaza.delete(0,'end')
    e_jeera.delete(0,'end')
    e_bathsoap.insert(0,0)
    e_bodylotion.insert(0,0)
    e_hairoil.insert(0,0)
    e_fashwash.insert(0,0)
    e_hairshampoo.insert(0,0)
    e_Wheatflour.insert(0,0)
    e_Rice.insert(0,0)
    e_Sugar.insert(0,0)
    e_Washing_powder.insert(0,0)
    e_cooking_oil.insert(0,0)
    e_coke.insert(0,0)
    e_cocacola.insert(0,0)
    e_fanta.insert(0,0)
    e_Maaza.insert(0,0)
    e_jeera.insert(0,0)
    textarea.delete(1.0,'end')
   
def exit():
    '''to exit from application'''
    root.destroy() 


# defining total function
def total():
    '''total function to make total of all products'''
    global soap,bodylotion,fashwash,hairshampoo,hairoil,wheat,rice,cookingoil,sugar,powder,coke,cola,jeera,fanta,maaza,body_tax,grocery_tax,softdrink_tax,total
    soap = int(e_bathsoap.get())*15
    bodylotion = int(e_bodylotion.get())*40
    fashwash = int(e_fashwash.get())*60
    hairshampoo = int(e_hairshampoo.get())*10
    hairoil = int(e_hairoil.get())*50
    wheat = int(e_Wheatflour.get())*55
    cookingoil = int(e_cooking_oil.get())* 120
    rice = int(e_Rice.get())*200
    sugar = int(e_Sugar.get())*50
    powder = int(e_Washing_powder.get())*330
    coke = int(e_coke.get()) * 40
    jeera = int(e_jeera.get()) * 40
    cola = int(e_cocacola.get()) * 40
    fanta = int(e_fanta.get()) * 40
    maaza = int(e_Maaza.get()) * 40
    total_body = soap+bodylotion+fashwash+hairshampoo+hairoil
    e_body_products.delete(0,'end')
    e_body_products.insert(0,f'₹ {total_body} /-')
    total_grocery = wheat+cookingoil+rice+sugar+powder
    e_grocery_products.delete(0,'end')
    e_grocery_products.insert(0,f'₹ {total_grocery} /-')
    total_softdrink = coke+jeera+cola+fanta+maaza
    e_softdrinks_products.delete(0,'end')
    e_softdrinks_products.insert(0,f'₹ {total_softdrink} /-')
    body_tax = total_body *0.28
    e_body_tax.delete(0,'end')
    e_body_tax.insert(0,f'₹ {ceil(body_tax)} /-')
    grocery_tax = total_grocery * 0.18
    e_grocery_tax.delete(0,'end')
    e_grocery_tax.insert(0,f'₹ {ceil(grocery_tax)} /-')
    softdrink_tax = total_softdrink * 0.40
    e_softdrinks_tax.delete(0,'end')
    e_softdrinks_tax.insert(0,f'₹ {ceil(softdrink_tax)} /-')
    total = total_body+total_grocery+total_softdrink+body_tax+grocery_tax+softdrink_tax
def generate_bill():
    '''generates bill in text area and update bill number and save data into txt file'''
    # delete all data from textarea
    textarea.delete(1.0,'end')
    if e_cusname.get()=="" or e_phno.get()=="":
        msg.showerror("Error","Customer Name and Phone Number is Manadatory")
    else:
        if e_body_products.get()=="" and e_grocery_products.get()=='' and e_softdrinks_products.get()=="":
            msg.showerror("Error","Please Select atleast One Product")
        elif e_body_products.get()=='₹ 0 /-' and e_grocery_products=="₹ 0 /-" and e_softdrinks_products=='₹ 0 /-':
                msg.showerror("Error","Please Select atleast One Product")
        else:
            textarea.insert('end',f'\t-------Welcome Customer-------\n')
            textarea.insert('end',f'bill number : {bill_num}\n')
            textarea.insert('end',f'Customer name : {e_cusname.get()}\n')
            textarea.insert('end',f'Mobile Number  : {e_phno.get()}\n')
            textarea.insert('end','*'*45)
            textarea.insert('end','\n Products\t\t   Quantity\t\t   Price\n')
            textarea.insert('end','*'*45)
            textarea.insert('end',"\n")
            if e_bathsoap.get()!='0':
                textarea.insert('end',f'Bath Soap \t\t    {e_bathsoap.get()}\t\t    {soap} /-\n')
            if e_bodylotion.get()!='0':
                textarea.insert('end',f'Body Lotion \t\t    {e_bodylotion.get()}\t\t    {bodylotion} /-\n')
            if e_hairshampoo.get()!='0':
                textarea.insert('end',f'Bath Soap \t\t    {e_hairshampoo.get()}\t\t    {hairshampoo} /-\n')
            if e_fashwash.get()!='0':
                textarea.insert('end',f'Bath Soap \t\t    {e_fashwash.get()}\t\t    {fashwash} /-\n')
            if e_hairoil.get()!='0':
                textarea.insert('end',f'Hair Oil \t\t    {e_hairoil.get()}\t\t    {hairoil} /-\n')
            if e_Wheatflour.get()!='0':
                textarea.insert('end',f'Ashirwad Atta \t\t    {e_Wheatflour.get()} kg\t\t    {wheat} /-\n')
            if e_Rice.get()!='0':
                textarea.insert('end',f'Basmati Rice \t\t    {e_Rice.get()} kg\t\t    {rice} /-\n')
            if e_Sugar.get()!='0':
                textarea.insert('end',f'Madhur Sugar \t\t    {e_Sugar.get()} kg\t\t    {sugar} /-\n')
            if e_Washing_powder.get()!='0':
                textarea.insert('end',f'Washing Powder \t\t   {e_Washing_powder.get()} kg\t\t    {powder} /-\n')
            if e_cooking_oil.get()!='0':
                textarea.insert('end',f'Cooking Oil \t\t    {e_cooking_oil.get()} l\t\t    {cookingoil} /-\n')
            if e_coke.get()!='0':
                textarea.insert('end',f'Coke \t\t    {e_coke.get()}\t\t    {coke} /-\n')
            if e_cocacola.get()!='0':
                textarea.insert('end',f'Coca-Cola \t\t    {e_cocacola.get()}\t\t    {cola} /-\n')
            if e_fanta.get()!='0':
                textarea.insert('end',f'Fanta \t\t    {e_fanta.get()}\t\t    {fanta} /-\n')
            if e_Maaza.get()!='0':
                textarea.insert('end',f'Maaza \t\t    {e_Maaza.get()}\t\t    {maaza} /-\n')
            if e_jeera.get()!='0':
                textarea.insert('end',f'Davat Jeera \t\t    {e_jeera.get()}\t\t    {jeera} /-\n')
            textarea.insert('end','*'*45)
            textarea.insert('end','\n\n')
            if body_tax!=0:
                textarea.insert('end',f'Body Products Tax \t\t\t\t   ₹ {ceil(body_tax)} /-\n')
            if grocery_tax!=0:
                textarea.insert('end',f'Grocery Products Tax \t\t\t\t   ₹ {ceil(grocery_tax)} /-\n')
            if softdrink_tax!=0:
                textarea.insert('end',f'Soft-Drink Products Tax \t\t\t\t   ₹ {ceil(softdrink_tax)} /-\n')
            textarea.insert('end','\n\n')
            textarea.insert('end','*'*45)
            if total!=0:
                textarea.insert('end',f'\n\n Total Amount -----------------  ₹ {ceil(total)} /-\n')
            textarea.insert('end','*'*45)
            updatebill()
            savebill()
            dbstore()

            
            


# Create a main application window
root = Tk()
root.title("SuperStar Mega Mall")
root.geometry("1270x685") 
root.iconbitmap(r'D:\brijesh\python\Python_assessment\billing Application\assets\icon.ico')

root.minsize(400,300) # Set the window size
root.maxsize(1400,1100)

# Create Title 
title =Label(root,fg="white",background="brown4",font="Arial 28 bold", text="SuperStar Billing System",borderwidth=10,relief=SUNKEN)
# Create customer details frame
cus_details_frame = LabelFrame(root,text="Customer Details",bg="brown4",fg='gold',bd=8,relief=SUNKEN)
# create customer details label and entry widgets
l_cusname = Label(cus_details_frame,background="brown4",fg = "white",font="Arial 15",text="Customer Name : ")
e_cusname = Entry(cus_details_frame,font="Arial 15",bd=7,width=20)    #store customer name
l_phno = Label(cus_details_frame, background="brown4", fg="white", font="Arial 15", text="Phone Number : ")
e_phno = Entry(cus_details_frame,font="Arial 15",bd=7,width=10)   #store phone number
l_bill = Label(cus_details_frame, background="brown4", fg="white", font="Arial 15", text="Bill Number : ")
e_bill = Label(cus_details_frame,background="white",fg="black",bd=7,font="Arial 15 bold",width=7,text=f"{bill_num}")   
enter_button = Button(cus_details_frame,text="Enter",font="Arial 12 bold",bd = 7,bg="red4",fg="white",width=10)

# Create Product Frame
product_frame  = Frame(root) # Frame does not have a label(title).
# create Body Products Frame
body_products_frame = LabelFrame (product_frame,text="Body Products",bg ="brown4",fg="gold" , bd = 8, relief = SUNKEN )
l_bathsoap = Label(body_products_frame,text="Bath Soap",bg="brown4",fg="white",font="Arial 15")
e_bathsoap = Entry(body_products_frame,font="Arial 15",bd=5,width=8)
e_bathsoap.insert(0,0)
l_bodylotion = Label(body_products_frame,text="Body Lotion",bg="brown4",fg="white",font="Arial 15")
e_bodylotion = Entry(body_products_frame,font="Arial 15",bd=5,width=8)
e_bodylotion.insert(0,0)
l_hairshampoo = Label(body_products_frame,text="Hair Shampoo",bg="brown4",fg="white",font="Arial 15")
e_hairshampoo = Entry(body_products_frame,font="Arial 15",bd=5,width=8)
e_hairshampoo.insert(0,0)
l_fashwash = Label(body_products_frame,text="Fash Wash",bg="brown4",fg="white",font="Arial 15")
e_fashwash = Entry(body_products_frame,font="Arial 15",bd=5,width=8)
e_fashwash.insert(0,0)
l_hairoil = Label(body_products_frame,text="Hair Oil",bg="brown4",fg="white",font="Arial 15")
e_hairoil = Entry(body_products_frame,font="Arial 15",bd=5,width=8)
e_hairoil.insert(0,0)

# Create Grocery Products Frame
grocery_frame = LabelFrame (product_frame,text="Grocery Products",bg ="brown4",fg="gold" , bd = 8, relief = SUNKEN )
l_Wheatflour = Label(grocery_frame,text="Wheat Flour",bg="brown4",fg="white",font="Arial 15")
e_Wheatflour = Entry(grocery_frame,font="Arial 15",bd=5,width=8)
e_Wheatflour.insert(0,0)
l_Rice = Label(grocery_frame,text="Rice",bg="brown4",fg="white",font="Arial 15")
e_Rice = Entry(grocery_frame,font="Arial 15",bd=5,width=8)
e_Rice.insert(0,0)
l_Sugar = Label(grocery_frame,text="Sugar",bg="brown4",fg="white",font="Arial 15")
e_Sugar = Entry(grocery_frame,font="Arial 15",bd=5,width=8)
e_Sugar.insert(0,0)
l_Washing_powder = Label(grocery_frame,text="Washing Powder",bg="brown4",fg="white",font="Arial 15")
e_Washing_powder = Entry(grocery_frame,font="Arial 15",bd=5,width=8)
e_Washing_powder.insert(0,0)
l_cooking_oil = Label(grocery_frame,text="Cooking Oil",bg="brown4",fg="white",font="Arial 15")
e_cooking_oil = Entry(grocery_frame,font="Arial 15",bd=5,width=8)
e_cooking_oil.insert(0,0)

# Create Softdrink Products Frame
softdrink_frame = LabelFrame (product_frame,text="Soft-drink Products",bg ="brown4",fg="gold" , bd = 8, relief = SUNKEN )
l_coke = Label(softdrink_frame,text="Coke",bg="brown4",fg="white",font="Arial 15")
e_coke = Entry(softdrink_frame,font="Arial 15",bd=5,width=8)
e_coke.insert(0,0)
l_cocacola = Label(softdrink_frame,text="Coca-cola",bg="brown4",fg="white",font="Arial 15")
e_cocacola = Entry(softdrink_frame,font="Arial 15",bd=5,width=8)
e_cocacola.insert(0,0)
l_fanta = Label(softdrink_frame,text="Fanta",bg="brown4",fg="white",font="Arial 15")
e_fanta = Entry(softdrink_frame,font="Arial 15",bd=5,width=8)
e_fanta.insert(0,0)
l_Maaza = Label(softdrink_frame,text="Maaza",bg="brown4",fg="white",font="Arial 15")
e_Maaza = Entry(softdrink_frame,font="Arial 15",bd=5,width=8)
e_Maaza.insert(0,0)
l_jeera = Label(softdrink_frame,text="Davat Jeera",bg="brown4",fg="white",font="Arial 15")
e_jeera = Entry(softdrink_frame,font="Arial 15",bd=5,width=8)
e_jeera.insert(0,0)

# create bill frame
bill_frame = Frame(product_frame,borderwidth= 8,relief=GROOVE)
bill_area = Label(bill_frame,text="Bill Area",font="Arial 15",bd = 8,relief=GROOVE)
# create scroll-bar
scrollbar = Scrollbar(bill_frame,orient=VERTICAL)
textarea = Text(bill_frame,height=14,width=45,yscrollcommand=scrollbar.set)

# create bill amount frame
bill_menu_frame = LabelFrame (root,text="Bill Menu",bg ="brown4",fg="gold" , bd = 8, relief = SUNKEN )
l_body_products = Label(bill_menu_frame,text="Body Products",bg="brown4",fg="white",font="Arial 15")
e_body_products = Entry(bill_menu_frame,font="Arial 15",bd=5,width=8)
l_grocery_products = Label(bill_menu_frame,text="Grocery Products",bg="brown4",fg="white",font="Arial 15")
e_grocery_products = Entry(bill_menu_frame,font="Arial 15",bd=5,width=8)
l_softdrinks_products = Label(bill_menu_frame,text="Softdrink Products",bg="brown4",fg="white",font="Arial 15")
e_softdrinks_products = Entry(bill_menu_frame,font="Arial 15",bd=5,width=8)
l_body_tax = Label(bill_menu_frame,text="Body Tax",bg="brown4",fg="white",font="Arial 15")
e_body_tax = Entry(bill_menu_frame,font="Arial 15",bd=5,width=8)
l_grocery_tax = Label(bill_menu_frame,text="Grocery Tax",bg="brown4",fg="white",font="Arial 15")
e_grocery_tax = Entry(bill_menu_frame,font="Arial 15",bd=5,width=8)
l_softdrinks_tax = Label(bill_menu_frame,text="Softdrink Tax",bg="brown4",fg="white",font="Arial 15")
e_softdrinks_tax = Entry(bill_menu_frame,font="Arial 15",bd=5,width=8)

# create button 
total_button = Button(bill_menu_frame,text="TOTAL",font="Arial 12 bold",bd = 7,bg="red4",fg="white",width=10,command=total)
generate_button = Button(bill_menu_frame,text="Generate Bill",font="Arial 12 bold",bd = 7,bg="red4",fg="white",width=10,command=generate_bill)
clear_button = Button(bill_menu_frame,text="Clear",font="Arial 12 bold",bd = 7,bg="red4",fg="white",width=10,command=clear)
exit_button = Button(bill_menu_frame,text="Exit",font="Arial 12 bold",bd = 7,bg="red4",fg="white",width=10,command=exit)

title.pack(fill=X,pady=5)
# placing customer details
cus_details_frame.pack(fill=X)
l_cusname.grid(row=0,column=0,padx=20)
e_cusname.grid(row=0,column=1) 
l_phno.grid(row=0,column=2,padx=20)
e_phno.grid(row=0,column=3)
l_bill.grid(row=0,column=4,padx=20)
e_bill.grid(row=0,column=5)
enter_button.grid(row=0,column=6,padx=70,pady=8)
product_frame.pack(pady=5)
# placing body products
body_products_frame.grid(row=0,column=0,padx=2)
l_bathsoap.grid(row=0,column=0,padx=9,pady=8,sticky='w')
e_bathsoap.grid(row=0,column=1,padx=9,pady=8)
l_bodylotion.grid(row=1,column=0,padx=9,pady=8,sticky='w')
e_bodylotion.grid(row=1,column=1,padx=9,pady=8)
l_hairshampoo.grid(row=2,column=0,padx=9,pady=8,sticky='w')
e_hairshampoo.grid(row=2,column=1,padx=9,pady=8)
l_fashwash.grid(row=3,column=0,padx=9,pady=8,sticky='w')
e_fashwash.grid(row=3,column=1,padx=9,pady=8)
l_hairoil.grid(row=4,column=0,padx=9,pady=8,sticky='w')
e_hairoil.grid(row=4,column=1,padx=9,pady=8)
# placing grocery products
grocery_frame.grid(row=0,column=1,padx=2)
e_Wheatflour.grid(row=0,column=1,padx=9,pady=8)
l_Wheatflour.grid(row=0,column=0,padx=9,pady=8,sticky='w')
l_Rice.grid(row=1,column=0,padx=9,pady=8,sticky='w')
e_Rice.grid(row=1,column=1,padx=9,pady=8)
l_Sugar.grid(row=2,column=0,padx=9,pady=8,sticky='w')
e_Sugar.grid(row=2,column=1,padx=9,pady=8)
l_Washing_powder.grid(row=3,column=0,padx=9,pady=8,sticky='w')
e_Washing_powder.grid(row=3,column=1,padx=9,pady=8)
l_cooking_oil.grid(row=4,column=0,padx=9,pady=8,sticky='w')
e_cooking_oil.grid(row=4,column=1,padx=9,pady=8)
# placing Soft-drink frame
softdrink_frame.grid(row=0,column=2,padx=2)
l_coke.grid(row=0,column=0,padx=9,pady=8,sticky='w')
e_coke.grid(row=0,column=1,padx=9,pady=8)
l_cocacola.grid(row=1,column=0,padx=9,pady=8,sticky='w')
e_cocacola.grid(row=1,column=1,padx=9,pady=8)
l_fanta.grid(row=2,column=0,padx=9,pady=8,sticky='w')
e_fanta.grid(row=2,column=1,padx=9,pady=8)
l_Maaza.grid(row=3,column=0,padx=9,pady=8,sticky='w')
e_Maaza.grid(row=3,column=1,padx=9,pady=8)
l_jeera.grid(row=4,column=0,padx=9,pady=8,sticky='w')
e_jeera.grid(row=4,column=1,padx=9,pady=8)
# placing bill frame
bill_frame.grid(row=0,column=3)
bill_area.pack(fill=X)
scrollbar.pack(side=RIGHT,fill=Y)
textarea.pack()
# to create y axis view of text area using scroll bar
scrollbar.config(command=textarea.yview)
# placig bill menu frame
bill_menu_frame.pack(fill=X)
l_body_products.grid(row=0,column=0,padx=9,pady=6,sticky='w')
e_body_products.grid(row=0,column=1,padx=9,pady=6)
l_grocery_products.grid(row=1,column=0,padx=9,pady=6,sticky='w')
e_grocery_products.grid(row=1,column=1,padx=9,pady=6)
l_softdrinks_products.grid(row=2,column=0,padx=9,pady=6,sticky='w')
e_softdrinks_products.grid(row=2,column=1,padx=9,pady=6)
l_body_tax.grid(row=0,column=2,padx=9,pady=6,sticky='w')
e_body_tax.grid(row=0,column=3,padx=9,pady=6)
l_grocery_tax.grid(row=1,column=2,padx=9,pady=6,sticky='w')
e_grocery_tax.grid(row=1,column=3,padx=9,pady=6)
l_softdrinks_tax.grid(row=2,column=2,padx=9,pady=6,sticky='w')
e_softdrinks_tax.grid(row=2,column=3,padx=9,pady=6)

# placing button frame in bill menu frame
total_button.grid(row=0,column=4,rowspan=3,padx=25)
generate_button.grid(row=0,column=5,rowspan=3,padx=25)
clear_button.grid(row=0,column=6,rowspan=3,padx=25)
exit_button.grid(row=0,column=7,rowspan=3,padx=25)

# Start the GUI main loop
root.mainloop()

