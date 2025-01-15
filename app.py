from io import BytesIO
import streamlit as st
from PIL import Image



def convert(input_image:BytesIO, type:str)-> str:
    pil_image = Image.open(input_image)

    if pil_image.mode in ["RGBA", "LA"]:
        background = Image.new("RGB", pil_image.size, (255, 255, 255))
        background.paste(pil_image, mask=pil_image.getchannel("A"))
        pil_image = background

    save_path = f"converted.{type}"
    pil_image.save(save_path, quality=95)

    return save_path



image_file = st.file_uploader("Upload the required file", type=("webp"))

convert_to = st.selectbox("Convert to", ("png", "jpeg/jpg"))
if convert_to == "jpeg/jpg":
    convert_to="jpg"

if st.button("Convert"):
    if image_file is None:
        st.error("Image file not uploaded")

    save_path = convert(image_file, convert_to)
    print(save_path)

    with open(save_path, "rb") as f:
        btn = st.download_button(
            label="Download Image",
            data=f,
            mime=f"image/{convert_to}"
        )