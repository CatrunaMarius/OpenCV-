#sharping

#Are efectele de întărirea sau accentuarea marginilor 
#într-o imagine.

import cv2
import numpy as np

image = cv2.imread('D:\Programare\cv\Master OpenCV\images\input.jpg' )
cv2.imshow("Original" , image)

#crem karnel shaping, nu normalizam deoarece suma valoari maticei este 1
kernel_sharpening = np.array([[-1,-1,-1],
                              [-1, 9,-1],
                              [-1,-1,-1]])

##aplicam un alt kernel pe imaginea de intrare
sharpened = cv2.filter2D(image,-1,kernel_sharpening)

cv2.imshow('Image Sharpening', sharpened)

cv2.waitKey()
cv2.destroyAllWindows()