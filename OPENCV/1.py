import cv2
import numpy as np

# load image
img = cv2.imread(r"C:\Users\liys2\Desktop\12.png");

# change to hue colorspace
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV);
h,s,v = cv2.split(hsv);

# use clahe to improve contrast 
# (the contrast is pretty good already, so not much change, but good habit to have here)
clahe = cv2.createCLAHE(clipLimit = 10) 
contrast = clahe.apply(v);

# use canny
canny = cv2.Canny(contrast, 20, 110);

# show
cv2.imshow('i', img);
cv2.imshow('v', v);
cv2.imshow('c', contrast);
cv2.imshow("canny", canny);
cv2.waitKey(0);

# save
cv2.imwrite("edges.png", canny);