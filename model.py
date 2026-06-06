import cv2 
import numpy as np 
from image_finder import find_image_files
# creates class where we contain function for every tool(for usability and code readability)

class BasicImageProcessor():
    # init function
    def __init__(self, images):
        self.images = images
    
    def grayscale(self):
        for f in self.images:
            img = cv2.imread(f)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            cv2.imshow("Greyscale",gray)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
    def blur(self):
        for f in self.images:
            img = cv2.imread(f)
            blur = cv2.blur(img, (5,5))
            cv2.imshow("Blur", blur)
            cv2.waitKey(0)
    def rotate_image(self, angle, clockwise = True): 
        if angle != 180 or 90:
             raise ValueError("angle must be 180 or 90")
        for f in self.images:
             img = cv2.imread(f)
             if angle == 180:
                 rotated = cv2.rotate(img, cv2.ROTATE_180)
                 cv2.imshow("180 degrees rotated image", rotated)
                 cv2.waitKey(0)
             elif clockwise == False and angle == 90:
                  rotated = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
                  cv2.imshow("90 degrees rotated counterclockwise", rotated)
                  cv2.waitKey(0)
             elif clockwise == True and angle == 90:
                 rotated = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
                 cv2.imshow("90 degrees rotated clockwise",rotated)
    

            