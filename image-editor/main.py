import tkinter as tk
from tkinter import filedialog 
from tkinter import messagebox
from tkinter import colorchooser
from PIL import Image, ImageOps, ImageTk,ImageFilter,ImageGrab
from tkinter import ttk # themed tkinter
from shades import colors

pen_color = "white"
pen_size = 5
file_path = ""
user_act = []

def add_img():
    global file_path
    file_path = filedialog.askopenfilename(initialdir = "C:")
    save_canvas()

    image = Image.open(file_path)
    #width,height = int(image.width/2),int(image.height/2)
    image = image.resize((canvas.winfo_width(), canvas.winfo_height()),Image.Resampling.LANCZOS)
    canvas.config(width = image.width,height=image.height)
    image = ImageTk.PhotoImage(image)
    canvas.image = image
    canvas.create_image(0,0,image=image,anchor="nw")

def draw(event):
    save_canvas()
    x1,y1 = (event.x - pen_size),(event.y - pen_size) #event.__ : "click event"
    x2,y2 = (event.x + pen_size),(event.y + pen_size)
    canvas.create_oval(x1,y1,x2,y2,fill=pen_color,outline="")

def change_color():
    global pen_color
    pen_color = colorchooser.askcolor(title="Select Pen Color")[1]

def change_size(size):
    global pen_size
    pen_size = size

def clear_canvas():
    save_canvas()  
    canvas.delete("all")
    canvas.create_image(0,0,image=canvas.image,anchor="nw")

def apply_filter(filter):
    save_canvas()
    image=Image.open(file_path)
    width,height = int(image.width/2),int(image.height/2)
    image = image.resize((width,height),Image.Resampling.LANCZOS)

    if filter == "Black and White":
        image = ImageOps.grayscale(image)
    elif filter == "Blur":
        image = image.filter(ImageFilter.BLUR)
    elif filter == "Emboss":
        image = image.filter(ImageFilter.EMBOSS)
    elif filter == "Sharpen":
        image = image.filter(ImageFilter.SHARPEN)
    elif filter == "Smooth":
        image = image.filter(ImageFilter.SMOOTH)
    elif filter == "Contour":
        image = image.filter(ImageFilter.CONTOUR)
    elif filter == "Detail":
        image = image.filter(ImageFilter.DETAIL)
    elif filter == "Edge Enhance":
        image = image.filter(ImageFilter.EDGE_ENHANCE)
    
    image = ImageTk.PhotoImage(image)
    canvas.image = image
    canvas.create_image(0,0,image=canvas.image,anchor="nw")

# adjust image capture as per screen size 
#  :( 
def save():
    save_path = filedialog.asksaveasfilename(defaultextension=".png",filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All files", "*.*")])
    x1 = 275
    y1 = 27
    x2 = 2000
    y2 = 1100

    #print(f" x1={canvas.winfo_rootx()}, y1={canvas.winfo_rooty()}, x2={canvas_left + canvas.winfo_width()}, y2={canvas_top + canvas.winfo_height()}")
    canvas_image = ImageGrab.grab(bbox=(x1, y1, x2, y2))
    canvas_image.save(save_path)
    messagebox.showinfo("Success", "Image saved!")

def save_canvas():
    x1 = 275
    y1 = 27
    x2 = 2000
    y2 = 1100
    current_canvas = ImageGrab.grab(bbox=(x1, y1, x2, y2))
    user_act.append(current_canvas)

def undo():
    last = user_act.pop()
    last = last.resize((canvas.winfo_width(), canvas.winfo_height()), Image.Resampling.LANCZOS)
    last = ImageTk.PhotoImage(last)
    canvas.delete("all")
    canvas.create_image(0, 0, image=last,anchor = "nw")

def erase():
    global pen_color
    save_canvas()
    pen_color = "#000000"
    save_canvas()
    global shape_detail
    shape_detail = None

root = tk.Tk()
root.state("zoomed") # earlier: 800x600
root.title("Image Editor")
root.config(bg="#000000")

left_frame = tk.Frame(root,width=300,height=500,bg=colors["shade_7"])
left_frame.pack(side="left",fill="y")

canvas = tk.Canvas(root,width=1300 , height=700,bg="#000000")
canvas.pack()

img_button = tk.Button(left_frame, text="Add Image",bg=colors["shade_2"],command=add_img)
img_button.pack(pady=10,side="top",fill="x")

color_button = tk.Button(left_frame,text="Pen Color",command=change_color,bg=colors["shade_2"])
color_button.pack(pady=10,fill="x")

pen_size_frame = tk.Frame(left_frame,bg=colors["shade_3"])
pen_size_frame.pack(pady=10,fill="x")

pen_size_1 = tk.Radiobutton(pen_size_frame,text="small",value=3,bg="white",command=lambda:change_size(3)) #purpose of lambda: function is only called when the event occurs.
pen_size_1.pack(side="left")

pen_size_2 = tk.Radiobutton(pen_size_frame,text="medium",value=5,bg="white",command=lambda:change_size(5))
pen_size_2.pack(side="left")
pen_size_2.select() # default

pen_size_3 = tk.Radiobutton(pen_size_frame,text="large",value=7,bg="white",command=lambda:change_size(7))
pen_size_3.pack(side="left")

save_button = tk.Button(left_frame, text="Save", bg=colors["shade_2"], command=save)
save_button.pack(side="bottom",pady=10,fill="x")

clear_button = tk.Button(left_frame, text="Clear",command = clear_canvas,bg="#B22222")
clear_button.pack(side="bottom",pady=10,fill="x")

filter_label = tk.Label(left_frame,text="Select Filter",bg=colors["shade_5"])
filter_label.pack(pady=10,fill="x")

filter_combo = ttk.Combobox(left_frame,values=["Black and White","Blur","Emboss","Sharpen","Smooth","Contour","Detail","Edge Enhance"])
filter_combo.pack(pady=10,fill="x")
filter_combo.bind("<<ComboboxSelected>>",lambda event:apply_filter(filter_combo.get()))

undo_button = tk.Button(left_frame, text="Undo",command=undo, bg=colors["shade_2"])
undo_button.pack(pady=10, fill="x")

eraser_button = tk.Button(left_frame, text="Eraser",command=erase, bg=colors["shade_2"])
eraser_button.pack(pady=10,fill="x")

canvas.bind("<B1-Motion>", draw)
root.mainloop()