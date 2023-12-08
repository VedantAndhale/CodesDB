import streamlit as web
from PIL import Image

with web.expander("STart Camera"):
    #start camera
    camera_image=web.camera_input("camers")

if camera_image:
    # Create apillow image instance
    img =Image.open(camera_image)

    # Create apillow image to grayscale
    gray_image=img.convert("L")

    # Render the grayscale img
    web.image(gray_image)
