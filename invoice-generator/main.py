import tkinter as tk
from tkinter import ttk,messagebox
from docxtpl import DocxTemplate
import datetime

invoice_list = []

def clear():
    qty_spinbox.delete(0,tk.END)
    qty_spinbox.insert(0,"1")
    product_entry.delete(0,tk.END)
    price_entry.delete(0,tk.END)

def add_item():
    global invoice_list
    qty = int(qty_spinbox.get())
    product = product_entry.get()
    price = float(price_entry.get())
    total = qty*price
    invoice_item = [product,qty,price,total]
    invoice_list.append(invoice_item)
    tree.insert("",0,values=invoice_item)
    clear()

def generate_invoice():
    global invoice_list
    fname = fname_entry.get()
    address = address_entry.get()
    phone = phone_entry.get()
    date = datetime.datetime.today()
    subtotal = sum(item[3] for item in invoice_list)
    total = (subtotal+subtotal*(0.1)+20) - subtotal*0.05
    doc = DocxTemplate("invoice_skeleton.docx")
    doc.render({
        "name":fname,
        "address":address,
        "phone":phone,
        "date":date.strftime("%Y-%m-%d"),
        "invoice_list":invoice_list,
        "subtotal":subtotal,
        "discount": "5%",
        "total":total,
        "taxrate":"10%",
        "totaltax":0.1*(subtotal),
        "handling": 20
    })
    doc_name = "Invoice"+fname+date.strftime("%Y-%m-%d-%H-%M-%S")+".docx"
    doc.save(doc_name)
    new_invoice()
    messagebox.showinfo("Success","Invoice generated...")

def new_invoice():
    global invoice_list
    fname_entry.delete(0,tk.END)
    address_entry.delete(0,tk.END)
    phone_entry.delete(0,tk.END)
    clear()
    tree.delete(*tree.get_children())
    invoice_list.clear()

root = tk.Tk()
#root.geometry("<dimensions>")
root.state("zoomed")
root.title("Invoice Generator")
root.configure(bg="black")

frame = tk.Frame(root)
frame.pack(padx=20,pady=100)

# Labels
fname_label = tk.Label(frame,text="Name",font=("Helvetica", 12, "bold")).grid(row=0,column=0,pady=5)
address_label = tk.Label(frame,text="Address",font=("Helvetica", 12, "bold")).grid(row=0,column=1,pady=5)
phone_label = tk.Label(frame,text="Phone",font=("Helvetica", 12, "bold")).grid(row=0,column=2,pady=5)
qty_label = tk.Label(frame,text="Qty",font=("Helvetica", 12, "bold")).grid(row=2,column=0,pady=5)
product_label = tk.Label(frame,text="Product",font=("Helvetica", 12, "bold")).grid(row=2,column=1,pady=5)
price_label = tk.Label(frame,text="Price",font=("Helvetica", 12, "bold")).grid(row=2,column=2,pady=5)

# Entry fields
fname_entry = tk.Entry(frame)
fname_entry.grid(row=1,column=0)
address_entry = tk.Entry(frame)
address_entry.grid(row=1,column=1)
phone_entry = tk.Entry(frame)
phone_entry.grid(row=1,column=2)
qty_spinbox = tk.Spinbox(frame,from_=1,to=999,increment=1)
qty_spinbox.grid(row=3,column=0)
product_entry = tk.Entry(frame)
product_entry.grid(row=3,column=1)
price_entry = tk.Entry(frame)
price_entry.grid(row=3,column=2)

# Buttons
add_button = tk.Button(frame,text="Add Item",command=add_item).grid(row=4,column=2,pady=15)
generate_button = tk.Button(frame,text="Generate Invoice",command=generate_invoice).grid(row=7,column=0,columnspan=3,sticky="news",padx=15,pady=5)
new_button = tk.Button(frame,text="New Invoice",command = new_invoice).grid(sticky="news",row=6,column=0,columnspan=3,pady=5,padx=15)

columns = ("DESCRIPTION","QTY","UNIT PRICE","TOTAL")
tree = ttk.Treeview(frame,columns=columns,show="headings")
tree.heading("DESCRIPTION",text="DESCRIPTION")
tree.heading("QTY",text="QTY")
tree.heading("UNIT PRICE",text="UNIT PRICE")
tree.heading("TOTAL",text="TOTAL")
tree.grid(columnspan=3,column=0,row=5,padx=20,pady=20)

root.mainloop()