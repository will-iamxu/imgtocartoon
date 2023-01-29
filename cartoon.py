
import cv2
import numpy as np
import os

input_dir = input("Enter the input directory path: ")
output_dir = input("Enter the output directory path: ")

for file in os.listdir(input_dir):
    
    if file.endswith(".jpg") or file.endswith(".png"):
        
        img = cv2.imread(os.path.join(input_dir, file))
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.medianBlur(gray, 7)
        edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
        color = cv2.bilateralFilter(img, 9, 300, 300)
        cartoon = cv2.bitwise_and(color, color, mask=edges)
        cv2.imwrite(os.path.join(output_dir, file), cartoon)
