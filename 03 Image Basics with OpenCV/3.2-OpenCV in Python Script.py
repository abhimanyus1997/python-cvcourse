import cv2
import numpy as np
import logging

#Logger info
log_filename = "3.2_OpenCV.log"
logging.basicConfig(filename=log_filename, filemode='w', level=logging.INFO, format='%(asctime)s : %(levelname)s - %(message)s',datefmt='%c')



#Defining path for Image File
path = "../res/puppy.jpg"

try:
    #Creating CV2 image object
    img = cv2.imread(path)
    logging.info("cv2.imread() executed")
except Exception as e:
        logging.exception(f"Error @ cv2.imread(): {e}")

#Defining the scale
resize_scale = 0.1


logging.info("Getting shape of Image")
#Getting the shape of Image
h,w, _ = img.shape


#Scalling Down the image with predefined Scale while maintaining the Original Aspect Ratio
h_scaled, w_scaled = round(h*resize_scale), round(w*resize_scale)

try:
    #Scalling Down/Up the image
    img = cv2.resize(img, (w_scaled, h_scaled))
    logging.info("cv2.resize() executed")
except Exception as e:
    logging.error(f"Error @ cv2.resize(): {e}")

print("Press Q to exit")

#Looping the image to show again and again
# until user Presses "Q" key

loop_counter = 0

while True:
    try:
        #Showing Image in window titled "Puppy Frame"
        cv2.imshow("Puppy Frame", img)
        loop_counter+=1
    except Exception as e:
        logging.error(f"Error @ cv2.imshow(): {e}")

    try:
        #ord() function returns the Unicode code from a given character
        #chr() function returns a string from a Unicode code integer.
        if cv2.waitKey(1) & 0xFF == ord('q'):
            #Logging how many times the loop runs
            logging.info(f"cv2.imshow() executed: {loop_counter} times")
            logging.info(f"cv2.imshow() stopped")
            logging.info("cv2.waitKey() executed")
            break
    except Exception as e:
        logging.error(f"Error @ cv2.waitKey: {e}")
