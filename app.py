import streamlit as st
from PIL import Image
from caption_model import generate_caption

st.set_page_config(page_title="AI Image Caption Generator", page_icon="🖼️")

st.title("🖼️ AI Image Caption Generator")
st.write("Upload an image from your computer and let AI describe it instantly!")

# File uploader for direct local upload
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Open and display uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Generate caption immediately after upload
    with st.spinner("Generating caption..."):
        caption = generate_caption(image)
    st.success("Caption Generated!")
    st.write(f"**{caption}**")
