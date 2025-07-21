import streamlit as st
import os
import tempfile
from pdf_utils.extract_images import extract_images_from_pdf
from pdf_utils.group_questions import group_images_into_questions
from PIL import Image

st.set_page_config(page_title="PDF Question Generator", layout="wide")
st.title("📘 PDF Visual Question Extractor")


uploaded_file = st.file_uploader("Upload an Olympiad-style PDF", type=["pdf"])

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
        temp_pdf.write(uploaded_file.read())
        pdf_path = temp_pdf.name

    # temporary image output folder
    temp_image_dir = os.path.join("data", "streamlit_images")
    os.makedirs(temp_image_dir, exist_ok=True)

    if st.button("🔍 Extract Questions from PDF"):
        with st.spinner("Extracting images and questions..."):
            image_paths = extract_images_from_pdf(pdf_path, temp_image_dir)
            question_blocks = group_images_into_questions(image_paths)

        st.success(f"{len(question_blocks)} questions extracted!")

        for i, block in enumerate(question_blocks):
            st.markdown(f"### Q{i+1}: {block['question']}")
            st.image(block["images"], caption="Question Image", width=300)
            st.markdown("**Options:**")
            cols = st.columns(len(block["option_images"]))
            for idx, (opt_img, col) in enumerate(zip(block["option_images"], cols)):
                with col:
                    st.image(opt_img, caption=f"Option {chr(65 + idx)}", width=150)
