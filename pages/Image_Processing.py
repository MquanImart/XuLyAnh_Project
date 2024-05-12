import streamlit as st
from PIL import Image
import numpy as np
import cv2
from xu_ly_anh import Negative, NegativeColor, Logarit, Power, PiecewiseLinear, Histogram, LocalHist, HistStat, MyFilter2D, MySmooth, MyMedianFilter

def xu_li_anh():

    imgin = None
    imgout = None
    
    file_uploaded = st.file_uploader("Tải ảnh lên", type=['jpg', 'jpeg', 'png', 'bmp', 'tif'])
    if file_uploaded is not None:
        file_bytes = np.asarray(bytearray(file_uploaded.read()), dtype=np.uint8)
        imgin = cv2.imdecode(file_bytes, cv2.IMREAD_GRAYSCALE)
        st.image(imgin, channels="GRAY", use_column_width=True, caption="Input Image")

    if imgin is not None:
        operation = st.selectbox("Các tùy chọn", ["", "Negative", "NegativeColor", "Logarit", "Power",
                                                              "PiecewiseLinear", "Histogram", "Hist Equal",
                                                              "Local Hist", "Hist Stat", "Filter 2D", "My Smooth",
                                                              "Smooth Box", "Smooth Gaussian", "My Median",
                                                              "Median filter"])

        if operation == "Negative":
            imgout = Negative(imgin)
        elif operation == "NegativeColor":
            imgout = NegativeColor(imgin)
        elif operation == "Logarit":
            imgout = Logarit(imgin)
        elif operation == "Power":
            imgout = Power(imgin)
        elif operation == "PiecewiseLinear":
            imgout = PiecewiseLinear(imgin)
        elif operation == "Histogram":
            imgout = Histogram(imgin)
        elif operation == "Hist Equal":
            imgout = cv2.equalizeHist(imgin)
        elif operation == "Local Hist":
            imgout = LocalHist(imgin)
        elif operation == "Hist Stat":
            imgout = HistStat(imgin)
        elif operation == "Filter 2D":
            imgout = MyFilter2D(imgin)
        elif operation == "My Smooth":
            imgout = MySmooth(imgin)
        elif operation == "Smooth Box":
            imgout = cv2.boxFilter(imgin, cv2.CV_8UC1, (45, 45))
        elif operation == "Smooth Gaussian":
            imgout = cv2.GaussianBlur(imgin, (43, 43), 7.0)
        elif operation == "My Median":
            imgout = MyMedianFilter(imgin)
        elif operation == "Median filter":
            imgout = cv2.medianBlur(imgin, 5)

        if imgout is not None:
            st.image(imgout, channels="GRAY", use_column_width=True, caption="Output Image")

