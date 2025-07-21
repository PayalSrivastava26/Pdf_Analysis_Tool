# PDF Question Generator Tool

This tool extracts visual questions and options from an Olympiad-style educational PDF and outputs them in structured JSON format.


##  How It Works

1. Extracts all images from a PDF
2. Groups images into blocks: 1 question + 3 options
3. Saves data as `questions_output.json`

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