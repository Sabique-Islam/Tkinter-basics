import os
import customtkinter as ctk
import json
import requests
from dotenv import load_dotenv

def language(json_file):
    with open(json_file) as f:
        languages = json.load(f)
    return languages

def generate():
    prompt = "Generate 10 ideas for programming projects, they all must be unique and creative."
    lang = language_dropdown.get()
    prompt += f" The programming language is {lang}. "
    diff = difficult_value.get()
    prompt += f"The difficulty is {diff}. "

    if c1.get():
        prompt += " The project should include a database."
    if c2.get():
        prompt += " The project should include an API."

    load_dotenv()
    api_key = os.getenv("API_KEY")
    url = "https://integrate.api.nvidia.com/v1/chat/completions"
    payload = {
        "model": "mistralai/mistral-7b-instruct-v0.3",
        "messages": [
            {
                "content": prompt,
                "role": "user"
            }
        ],
        "temperature": 0.2,
        "top_p": 0.7,
        "frequency_penalty": 0,
        "presence_penalty": 0,
        "max_tokens": 1024,
        "stream": False,
        "stop": ["string"]
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": f"Bearer {api_key}"
    }

    response = requests.post(url, json=payload, headers=headers)
    try:
        data = response.json()
        ideas = data["choices"][0]["message"]["content"]
        result.delete("0.0", "end")
        result.insert("0.0", ideas)
    except Exception as e:
        result.delete("0.0", "end")
        result.insert("0.0", f"Error parsing response: {str(e)}")

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}+0+0")
root.title("Llama Chat")

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

main_frame = ctk.CTkFrame(root, corner_radius=15)
main_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

main_frame.grid_rowconfigure(2, weight=1)
main_frame.grid_columnconfigure(0, weight=1)

title_label = ctk.CTkLabel(
    main_frame, text="Llama Chat", font=ctk.CTkFont(size=36, weight="bold"), text_color="#A78BFA"
)
title_label.grid(row=0, column=0, pady=10, sticky="n")

language_frame = ctk.CTkFrame(main_frame, corner_radius=15)
language_frame.grid(row=1, column=0, sticky="ew", pady=(10, 5))
language_frame.grid_columnconfigure(1, weight=1)

language_label = ctk.CTkLabel(
    language_frame, text="Programming Language", font=ctk.CTkFont(weight="bold", size=16), text_color="#A78BFA"
)
language_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

language_dropdown = ctk.CTkComboBox(language_frame, values=language("lang.json"), corner_radius=10)
language_dropdown.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

difficulty_frame = ctk.CTkFrame(main_frame, corner_radius=15)
difficulty_frame.grid(row=2, column=0, sticky="ew", pady=(5, 5))
difficulty_frame.grid_columnconfigure((0, 1, 2), weight=1)

difficulty_label = ctk.CTkLabel(
    difficulty_frame, text="Project Difficulty", font=ctk.CTkFont(weight="bold", size=16), text_color="#A78BFA"
)
difficulty_label.grid(row=0, column=0, columnspan=3, pady=10)

difficult_value = ctk.StringVar(value="Easy")

radiobutton1 = ctk.CTkRadioButton(
    difficulty_frame, text="Easy", variable=difficult_value, value="Easy", corner_radius=10
)
radiobutton1.grid(row=1, column=0, padx=10, pady=10)

radiobutton2 = ctk.CTkRadioButton(
    difficulty_frame, text="Medium", variable=difficult_value, value="Medium", corner_radius=10
)
radiobutton2.grid(row=1, column=1, padx=10, pady=10)

radiobutton3 = ctk.CTkRadioButton(
    difficulty_frame, text="Hard", variable=difficult_value, value="Hard", corner_radius=10
)
radiobutton3.grid(row=1, column=2, padx=10, pady=10)

features_frame = ctk.CTkFrame(main_frame, corner_radius=15)
features_frame.grid(row=3, column=0, sticky="ew", pady=(5, 10))
features_frame.grid_columnconfigure((0, 1), weight=1)

features_label = ctk.CTkLabel(
    features_frame, text="Features", font=ctk.CTkFont(weight="bold", size=16), text_color="#A78BFA"
)
features_label.grid(row=0, column=0, columnspan=2, pady=10)

c1 = ctk.CTkCheckBox(features_frame, text="Database", corner_radius=10)
c1.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

c2 = ctk.CTkCheckBox(features_frame, text="API", corner_radius=10)
c2.grid(row=1, column=2, padx=10, pady=10, sticky="ew")

button = ctk.CTkButton(
    main_frame, text="Generate Ideas", command=generate, corner_radius=15, font=ctk.CTkFont(size=16, weight="bold"),fg_color="#A78BFA",hover_color="#8B5CF6"
)
button.grid(row=4, column=0, padx=10, pady=(10, 20), sticky="ew")

result = ctk.CTkTextbox(
    main_frame, font=ctk.CTkFont(size=15), text_color="#FFFFFF", corner_radius=15, height=200
)
result.grid(row=5, column=0, padx=10, pady=10, sticky="nsew")

root.mainloop()