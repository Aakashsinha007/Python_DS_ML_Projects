import requests
import os
from tkinter import Tk, filedialog, messagebox, simpledialog
from openpyxl import Workbook
from pathlib import Path

API_KEY = 'helloworld'  # Replace with your actual OCR.Space API key

def extract_text_from_image(image_path):
    with open(image_path, 'rb') as f:
        response = requests.post(
            'https://api.ocr.space/parse/image',
            files={'filename': f},
            data={'apikey': API_KEY, 'language': 'eng'},
        )
    result = response.json()
    if result.get('IsErroredOnProcessing'):
        return None
    return result['ParsedResults'][0]['ParsedText']

def save_text_to_excel(text, file_path):
    wb = Workbook()
    ws = wb.active
    for i, line in enumerate(text.splitlines(), 1):
        ws.cell(row=i, column=1, value=line)
    wb.save(file_path)

def main():
    root = Tk()
    root.withdraw()

    # Step 1: Ask user to confirm the action
    user_choice = messagebox.askyesno("JPG to Excel Converter", "Do you want to convert JPG to Excel?")
    if not user_choice:
        return

    # Step 2: Ask user to upload file
    messagebox.showinfo("Upload", "Please upload file to be converted")
    image_path = filedialog.askopenfilename(filetypes=[("JPG files", "*.jpg;*.jpeg")])
    if not image_path:
        return

    # Step 3: Extract text
    text = extract_text_from_image(image_path)
    if text:
        output_file = Path.home() / "Downloads" / (Path(image_path).stem + "_output.xlsx")
        save_text_to_excel(text, output_file)
        messagebox.showinfo("Success", f"Excel file saved at:\n{output_file}")
    else:
        messagebox.showerror("Error", "Failed to extract text.")

if __name__ == "__main__":
    main()
