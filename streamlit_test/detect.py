from inference import main
import os,sys
import cv2
import numpy as np
import pandas as pd
def predict(image1):
    image1 = np.array(image1)
    cv2.imwrite('./streamlit_test/data/images/train_00000.jpg',image1) # must change
    test = "python inference.py"
    os.system(test)
    os.remove('./streamlit_test/data/images/train_00000.jpg')
    f = open('./streamlit_test/submit/output.csv', 'r') # must change
    os.remove('./streamlit_test/submit/output.csv')
    test = f.read()
    file_name = test.split('\t')[0]
    latex_info = test.split('\t')[1:]
    return latex_info[0]