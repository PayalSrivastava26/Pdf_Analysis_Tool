# 📄 PDF Analysis Tool

A Python-based tool that extracts structured questions and images from educational PDFs (like Olympiad sample papers). Includes both a **command-line interface** and a **Streamlit-based GUI** to make the process easy and visual.

---

## Features

- ✅ Extracts all images from the uploaded PDF
- ✅ Organizes question blocks in structured JSON format
- ✅ Supports educational content with image-based questions
- ✅ Streamlit app for uploading PDFs and viewing output instantly
- ✅ Clean folder structure and modular utility scripts

---

##  Tech Stack

- Python 3.10+
- [PyMuPDF](https://github.com/pymupdf/PyMuPDF) (for image + text extraction)
- Streamlit (for GUI)
- Pillow (for image processing)
- json (for structured output)

---

## Project Structure

pdf-question-tool/
├── data/
│ ├── IMO_Olympiad.pdf
│ ├── images/
│ └── questions_output.json
├── pdf_utils/
│ ├── extract_images.py
│ └── group_questions.py
├── main.py
├── requirements.txt

##  How to Use

1. Clone the Repository

```bash
git clone https://github.com/PayalSrivastava26/Pdf_Analysis_Tool.git
cd Pdf_Analysis_Tool

2.Install Dependencies
python -m venv .venv
.\.venv\Scripts\activate  # For Windows
pip install -r requirements.txt


