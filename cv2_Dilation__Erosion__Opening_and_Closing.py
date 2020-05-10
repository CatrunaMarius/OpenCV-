import cv2
import numpy as np

image = cv2.imread('D:\Programare\cv\Master OpenCV\images\opencv_inv.png', 0)

cv2.imshow('Original', image)
cv2.waitKey()

#definim dimensiunea Kernel 
kernel = np.ones((5,5), np.uint8)

#Erosion -Înlătură pixelul la limitele obiectelor dintr-o imagine
erosion =cv2.erode(image, kernel, iterations=1)
cv2.imshow('Erosion', erosion)
cv2.waitKey()

#Dilation-Adaugă un pixel la limitele obiectelor dintr-o imagine
dilation = cv2.dilate(image, kernel, iterations= 1)
cv2.imshow('Dilation', dilation)
cv2.waitKey()

#Opening - bun pt a indeparta noise
#opening - Erosion urmata de dilation
opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
cv2.imshow('Opening', opening)
cv2.waitKey()

#Closing - bun pt indepartarea noise
#Closing este Dilation urmata de erosion
closing = cv2.morphologyEx(image,cv2.MORPH_CLOSE, kernel)
cv2.imshow('Closing', closing)
cv2.waitKey()

cv2.destroyAllWindows()
