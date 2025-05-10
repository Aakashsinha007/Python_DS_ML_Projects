# 📸 JPG to Excel Converter

This tool uses **OCR (Optical Character Recognition)** to extract text from `.jpg` or `.jpeg` image files and saves the output to an Excel (.xlsx) file.

## 🛠 Features

- Select a `.jpg` image file using a dialog box
- Extracts all readable text using OCR.space API
- Saves extracted lines to an Excel file in your Downloads folder
- Also available as a `.exe` for non-technical users

---

## 🚀 How to Use

### ✅ Option 1: Python Script

1. Install dependencies:
    ```bash
    pip install requests openpyxl
    ```

2. Run the script:
    ```bash
    python jpg_to_excel_converter.py
    ```

3. Follow on-screen instructions:
    - Choose conversion option
    - Upload your `.jpg` file
    - Excel file will be saved in your Downloads folder

---

### ✅ Option 2: Windows Executable

- Run `jpg_to_excel_converter.exe`
- No Python installation required

> Note: The `.exe` version is available under the `dist/` folder or [GitHub Releases](#) (add link if available)

---

## 🧠 Tech Stack

- Python
- OCR.space API
- Tkinter GUI
- OpenPyXL for Excel handling
- PyInstaller for `.exe` build

---

## 📂 File Structure

