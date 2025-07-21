from pdf_utils.extract_images import extract_images_from_pdf
from pdf_utils.group_questions import group_images_into_questions
import json
import os

# Set paths
pdf_path = "data/IMO_Olympiad.pdf"
images_dir = "data/images"
output_json_path = "data/questions_output.json"

# Step 1: Extract images from PDF
image_paths = extract_images_from_pdf(pdf_path, images_dir)

# Step 2: Group into question blocks
question_blocks = group_images_into_questions(image_paths)

# Step 3: Save as JSON
with open(output_json_path, "w") as f:
    json.dump(question_blocks, f, indent=2)

print("Done! Output saved to:", output_json_path)
