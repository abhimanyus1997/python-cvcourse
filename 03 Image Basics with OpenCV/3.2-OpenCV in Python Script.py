import cv2
import numpy as np


path = "../res/puppy.jpg"


img = cv2.imread(path)

resize_scale = 0.1
h,w, _ = img.shape
h_scaled, w_scaled = round(h*resize_scale), round(w*resize_scale)

#Scalling Down/Up the image
img = cv2.resize(img, (w_scaled, h_scaled))

print("Press Q to exit")
while True:
    cv2.imshow("Puppy Frame", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
