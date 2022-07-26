import cv2
import numpy as np


path = "../res/puppy.jpg"


img = cv2.imread(path)

resize_scale = 0.1

#cv2.imshow("Puppy", img)
while True:
    cv2.imshow("Puppy Frame", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
