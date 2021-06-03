from inference import main
import os,sys
import cv2
import numpy as np
import pickle
import pandas as pd
def predict(image1):
    image1 = np.array(image1)
    with open("./streamlit_test/data/images/image.pkl","wb") as fw:
        pickle.dump(image1,fw)
    # cv2.imwrite('./streamlit_test/data/images/train_00000.jpg',image1) # must change
    test = "python streamlit_test/inference.py"
    os.system(test)
    f = open('./streamlit_test/submit/output.csv', 'r') # must change
    test = f.read()
    file_name = test.split('\t')[0]
    latex_info = test.split('\t')[1:]
    return latex_info[0]