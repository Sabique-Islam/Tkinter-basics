import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Login Form")
window.geometry("500x500")
window.configure(bg='#333333')

def login():
    username = "Aragorn"
    password = "Frodo69"
    
    if username_entry.get()==username and password_entry.get()==password:
        messagebox.showinfo(title="Logged in",message="Welcome!")
    else:
        messagebox.showinfo(title="Error",message="Try again")

# Responsive UI
frame = tk.Frame(bg='#333333')

# Edit: Replaced parent "window" to "frame"
login_label = tk.Label(frame,text="Login", bg='#333333',fg="#FFFFFF",font={"Arial",30})
login_label.grid(row=0,column=0,columnspan=2,sticky="news",pady=40)

username_label = tk.Label(frame,text="Username", bg='#333333',fg="#FFFFFF",font={"Arial",20})
username_label.grid(row=1,column=0)

username_entry = tk.Entry(frame)
username_entry.grid(row=1,column=1,pady=20)

password_label = tk.Label(frame,text="Password", bg='#333333',fg="#FFFFFF",font={"Arial",20})
password_label.grid(row=2,column=0)

password_entry = tk.Entry(frame,show="*")
password_entry.grid(row=2,column=1,pady=20)

login_button = tk.Button(frame,text="Login", bg='#FF3399',fg="#FFFFFF",font={"Arial",20},command=login)
login_button.grid(row=3,column=0,columnspan=2,pady=30)

frame.pack() # Responsive by default
window.mainloop()