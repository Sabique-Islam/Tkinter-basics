import tkinter as tk
from tkinter import ttk,messagebox
import json
import openpyxl
import os

def load_countries(json_file):
    with open(json_file, 'r',encoding="utf-8") as file:
        countries = json.load(file)
        return [country["name"] for country in countries]

def enter_data():
    accept = accept_var.get()
    if accept == "Accepted":
        fname = first_name_entry.get()
        lname = last_name_entry.get()
        if fname and lname:
            title = title_combobox.get()
            age = age_spinbox.get()
            nation = nationality_combobox.get()
            registration_status = reg_status_var.get()
            courses = numcourses_spinbox.get()
            semester = numsemesters_spinbox.get()
            print("---------------------------------------------")
            print(f"Title: {title}  First name: {fname}  Last name: {lname}")
            print(f"Age: {age}  Nationality: {nation}")
            print(f"Courses: {courses}  Semesters: {semester}")
            print(f"Registration Status: {registration_status}")
            print("---------------------------------------------")

            filepath = r"C:\Users\Dell\Desktop\tkinter\data-entry-form\excel-data-entry-form\data.xlsx"
            if not os.path.exists(filepath):
                workbook = openpyxl.Workbook()
                sheet = workbook.active
                heading = ["Title","First name","Last name","Age","Nationality","Courses","Semesters","Registration Status"]
                sheet.append(heading)
                workbook.save(filepath)
            workbook = openpyxl.load_workbook(filepath)
            sheet = workbook.active
            sheet.append([title,fname,lname,age,nation,courses,semester,registration_status])
            workbook.save(filepath)
        else:
            messagebox.showwarning(title="Error", message="First name and last name are required.")
    else:
        messagebox.showwarning(title="Error", message="Please accept the terms and conditions.")
        
root = tk.Tk()
root.geometry("500x500")
root.title("ENTRY FORM")
frame = tk.Frame(root)

user_info_frame = tk.LabelFrame(frame,text="User Information")
user_info_frame.grid(row=0,column=0, padx=20,pady=10)

first_name_label = tk.Label(user_info_frame,text="First Name")
first_name_label.grid(row=0,column=0)
last_name_label = tk.Label(user_info_frame,text="Last Name")
last_name_label.grid(row=0,column=1)

first_name_entry = tk.Entry(user_info_frame)
last_name_entry = tk.Entry(user_info_frame)
first_name_entry.grid(row=1,column=0)
last_name_entry.grid(row=1,column=1)

title_label = tk.Label(user_info_frame,text="Title")
title_combobox = ttk.Combobox(user_info_frame,values=["","Mr.","Mrs.","Ms.","Dr."])
title_label.grid(row=0,column=2)
title_combobox.grid(row=1,column=2)

age_label = tk.Label(user_info_frame, text="Age")
age_spinbox = tk.Spinbox(user_info_frame, from_=10, to=110)
age_label.grid(row=2, column=0)
age_spinbox.grid(row=3, column=0)

nationality_label = tk.Label(user_info_frame, text="Nationality")
country = load_countries("country.json")
nationality_combobox = ttk.Combobox(user_info_frame, values=country)
nationality_combobox.set("Select a country")

nationality_label.grid(row=2, column=1)
nationality_combobox.grid(row=3, column=1)

for i in user_info_frame.winfo_children():
    i.grid_configure(padx=10,pady=5)

course_frame = tk.LabelFrame(frame)
course_frame.grid(row=1,column=0,sticky="news ",padx=20,pady=10)

registered_label = tk.Label(course_frame, text="Registration Status")
reg_status_var = tk.StringVar(value="Not Registered")
registered_check = tk.Checkbutton(course_frame, text="Currently Registered",variable=reg_status_var,onvalue="Registered",offvalue="Not registered")

registered_label.grid(row=0, column=0)
registered_check.grid(row=1, column=0)

numcourses_label = tk.Label(course_frame,text="# Completed Course")
numcourses_spinbox = tk.Spinbox(course_frame,from_=0,to=999)
numcourses_label.grid(row=0,column=1)
numcourses_spinbox.grid(row=1,column=1)

numsemesters_label = tk.Label(course_frame,text="# Semesters")
numsemesters_spinbox = tk.Spinbox(course_frame,from_=0,to=999)
numsemesters_label.grid(row=0,column=2)
numsemesters_spinbox.grid(row=1,column=2)

for i in course_frame.winfo_children():
    i.grid_configure(padx=10,pady=5)

terms_frame = tk.LabelFrame(frame,text="Terms & Conditions")
terms_frame.grid(row=2,column=0,sticky="news",padx=20,pady=10)

accept_var = tk.StringVar(value="Not accepted")
terms_check = tk.Checkbutton(terms_frame,text="I accept all the terms and conditions.",variable = accept_var,onvalue="Accepted",offvalue="Not accepted")
terms_check.grid(row=0,column=0)

button = tk.Button(frame,text="Enter data",command=enter_data)
button.grid(row=3,column=0,sticky="news",padx=220,pady=10)

frame.pack()
root.mainloop()