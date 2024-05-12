# python3 -m venv venv
# . venv/bin/activate
# pip install streamlit
# pip install torch torchvision
# streamlit run main.py
import streamlit as st
from PIL import Image


import style


def style_transfer():
    st.title('PyTorch Style Transfer')

    img = st.selectbox(
        'Select Image',
        ('amber.jpg', 'cat.png')
    )
    style_name = st.selectbox(
        'Select Style',
        ('candy', 'mosaic', 'rain_princess', 'udnie')
    )


    model= "./pages/style_transfer/saved_models/" + style_name + ".pth"
    input_image = "./Image/content-images/" + img
    output_image = "./Image/output-images/" + style_name + "-" + img

    if input_image is not None:
        st.write('### Source image:')
        image = Image.open(input_image)
        st.image(image, width=400) # image: numpy array
        clicked = st.button('Stylize')

        if clicked:
            model = style.load_model(model)
            style.stylize(model, input_image, output_image)

            st.write('### Output image:')
            image = Image.open(output_image)
            st.image(image, width=400)
