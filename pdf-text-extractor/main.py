import tkinter as tk
from tkinter import filedialog
import PyPDF2 as pd

def openFile():
    filename = filedialog.askopenfilename(
        title="Open PDF file",
        initialdir=r"C:\Users\Dell\Desktop\tkinter\pdf-text-extractor",
        filetypes=[('PDF files', "*.pdf")]
    )
    filename_label.configure(text=filename)
    
    output_file_text.delete("1.0", tk.END)  # Delete text from previous PDF
    try:
        with open(filename, 'rb') as file:
            reader = pd.PdfReader(file)
            for i in range(len(reader.pages)):
                current_text = reader.pages[i].extract_text()
                output_file_text.insert(tk.END, current_text)
    except Exception as e:
        output_file_text.insert(tk.END, f"Error reading PDF: {e}")

root = tk.Tk()
root.title("PDF Text Extractor")
root.geometry("400x500")

bg_color = "#333333"
text_color = "#ffffff"

root.configure(bg=bg_color)

filename_label = tk.Label(root, text="No file selected", bg=bg_color, fg=text_color)
output_file_text = tk.Text(root, wrap=tk.WORD, bg=bg_color, fg=text_color, insertbackground=text_color)
open_file_button = tk.Button(root, text="Open PDF File", command=openFile, bg="#444444", fg=text_color, activebackground="#555555", activeforeground=text_color)

filename_label.pack()
output_file_text.pack(expand=True, fill=tk.BOTH)
open_file_button.pack()

root.mainloop()