# Project Idea Generator
Uses **`mistralai/mistral-7b-instruct-v0.3`**, an AI model, to generate the project ideas.

## Interface
![Interface](project-idea-generator/sample/image.png)

## Installation

```bash
git clone https://github.com/Sabique-Islam/Tkinter-basics
```
```bash
cd Tkinter-basics/project-idea-generator
```
```bash
pip install -r requirements.txt
```
```bash
python main.py
```
## Set Up Your API Key
This application requires an API key to interact with the NVIDIA API that provides access to `mistralai/mistral-7b-instruct-v0.3`. Follow these steps to set it up:

1. **Generate an API Key:**
   - [Click here](https://build.nvidia.com/mistralai/mistral-7b-instruct-v0).
   - Click on `Build with this NIM`.
   - Complete the login process.
   - Generate a new API key and copy it.

2. **Add Your API Key:**
   - Create a `.env` file in the `project-idea-generator` folder (if it doesn't exist already).
   - Add the following line to the `.env` file:

     ```env
     API_KEY=your_api_key
     ```

     Replace `your_api_key` with the API key you obtained in the previous step.