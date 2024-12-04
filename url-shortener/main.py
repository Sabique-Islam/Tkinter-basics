import tkinter as tk
from tkinter import messagebox
import pyshorteners
import re

def shorten():
    try:
        long_url = long_url_entry.get()
        if not re.match(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', long_url):
            raise ValueError("Enter valid URL.")
        s = pyshorteners.Shortener()
        short_url = s.tinyurl.short(long_url)
        short_url_entry.delete(0, tk.END)
        short_url_entry.insert(0, short_url)

    except ValueError as e:
        messagebox.showerror("Error", str(e))

    except Exception as e:
        messagebox.showerror("Error", "An error occurred: " + str(e))

root = tk.Tk()
root.title("URL Shortener")
root.geometry("500x500")
root.config(bg="#333333")

long_url_label = tk.Label(root, text="Enter Long URL", fg="white", bg="#333333", font=("Helvetica", 14))
long_url_entry = tk.Entry(root, width=40, font=("Helvetica", 14), fg="white", bg="#3C3C3C", bd=0, insertbackground="white")
short_url_label = tk.Label(root, text="Shortened URL", fg="white", bg="#333333", font=("Helvetica", 14))
short_url_entry = tk.Entry(root, width=40, font=("Helvetica", 14), fg="white", bg="#3C3C3C", bd=0, insertbackground="white")

short_button = tk.Button(root, text="Shorten URL", command=shorten, fg="white", bg="#6A4C9C", font=("Helvetica", 14))

long_url_label.pack(pady=10)
long_url_entry.pack(pady=5)
short_url_label.pack(pady=10)
short_url_entry.pack(pady=5)
short_button.pack(pady=20)

root.mainloop()