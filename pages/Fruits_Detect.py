import streamlit as st
from PIL import Image
import numpy as np
import cv2

def nhan_dang_trai_cay():
    st.error("Chỉ để test thử")
    
    st.success("Nhập ảnh trái cây")
    uploaded_file = st.file_uploader("Chọn ảnh", type=['png', 'jpg', 'jpeg'])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Ảnh gốc', use_column_width=True)
        st.info("Ảnh gốc")
        st.image(image, caption='Ảnh gốc', use_column_width=True)
        st.info("Ảnh xử lí")
        # chỉ dùng để test chớ chưa xử lí gì cả
        if st.button("Xử lí"):
            image = np.array(image)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
            st.image(thresh, caption='Ảnh xử lí', use_column_width=True)
            st.info("Ảnh xử lí")
            st.info("Kết quả")
            if st.button("Nhận dạng"):
                pass
    else:
        st.info("Vui lòng chọn ảnh")
