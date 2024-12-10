import os, requests, base64, io
import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk
from dotenv import load_dotenv
load_dotenv()

def generate():
    api_key = os.getenv("API_KEY")
    user_prompt = prompt_entry.get("0.0", tk.END)
    user_prompt += "in"+style_dropdown.get()+"style."
    image_quantity = number_slider.get() # crying emoji
    styles = style_dropdown.get()

    url = "https://ai.api.nvidia.com/v1/genai/nvidia/consistory"
    payload = {
        "mode": "init",
        "subject_prompt": user_prompt,
        "subject_tokens": [user_prompt],
        "subject_seed": 0,
        "style_prompt": styles,
        "scene_prompt1": styles,
        "scene_prompt2": styles,
        "additional_scene_prompt": "",
        "additional_scene_seed": 0,
        "attention_dropout": 0.5,
        "cfg_scale": 5,
        "negative_prompt": "",
        "same_initial_noise": False,
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": f"Bearer {api_key}"
    }
    response = requests.post(url, json=payload, headers=headers) 
    if response.status_code == 200:
        full_response = response.json()

        if "artifacts" in full_response:
            images = []
            for artifact in full_response["artifacts"]:
                base64_image = artifact["base64"]
                image_data = base64.b64decode(base64_image)
                image = Image.open(io.BytesIO(image_data))

                canvas_width=canvas.winfo_width()
                canvas_height=canvas.winfo_height()

                image.thumbnail((canvas_width, canvas_height), Image.Resampling.LANCZOS)

                photo_image = ImageTk.PhotoImage(image)
                images.append(photo_image)

            def update_image(index=0):
                canvas.delete("all") 
                canvas.image = images[index]
                canvas.create_image(canvas.winfo_width() // 2,canvas.winfo_height() // 2,anchor="center",image=images[index])
                index = (index + 1) % len(images)
                canvas.after(2000, update_image, index)
            update_image()

root = ctk.CTk() # to create CTk window
root.geometry("800x600") # adjust as u plzz
root.title("AI Image Generator") # couldn't think of a name
ctk.set_appearance_mode("dark") # u dare use light mode !!
ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

input_frame = ctk.CTkFrame(root, corner_radius=15)
input_frame.pack(side="left", fill="both", expand=True,padx=20,pady=20)

prompt_label = ctk.CTkLabel(input_frame,text="Prompt",font=("Algerian", 14),corner_radius=70,fg_color = "#00599E")
prompt_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
prompt_entry = ctk.CTkTextbox(input_frame, height=80, width=300, border_width=1)
prompt_entry.grid(row=0, column=1, padx=10, pady=10, sticky="we")

style_label = ctk.CTkLabel(input_frame, text="Style",font=("Algerian", 14),corner_radius=70,fg_color = "#00599E")
style_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
style_dropdown = ctk.CTkComboBox(input_frame, values=["Realistic", "Cartoon", "3D Illustration", "Flat Art"], width=208)
style_dropdown.grid(row=1, column=1, padx=10, pady=10, sticky="we")

number_label = ctk.CTkLabel(input_frame, text="Image Quantity",font=("Algerian", 14),corner_radius=70,fg_color = "#00599E")
number_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
number_slider = ctk.CTkSlider(input_frame, from_=1, to=10, number_of_steps=9, width=200)
number_slider.grid(row=2, column=1, padx=10, pady=10, sticky="we")

generate_button = ctk.CTkButton(input_frame, text="Generate", command=generate, height=40, font=("Algerian", 20, "bold"), hover_color="#082d41",corner_radius=10,anchor="center")
generate_button.grid(row=3, column=0, columnspan=2, sticky="news", padx=10, pady=20)

canvas_frame = ctk.CTkFrame(root, corner_radius=15)
canvas_frame.pack(side="right", fill="both",expand=True,padx=20, pady=20)

canvas = tk.Canvas(canvas_frame, bg="#1a1a1a", highlightthickness=0, width=512, height=512)
canvas.pack(expand=True)

root.mainloop()