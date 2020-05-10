import cv2
import numpy as np
#Rotatia
#Re-size este foarte simba folosid doar functia cv22.resize
#cv2.resize(imaginea, dimensiunea(output dimensiuni imagini ), x scalarea, y scalarea, interpolation) # x = lungimea ,y inaltimea imagini scalate

#incarcarea imagini
image = cv2.imread("D:\Programare\cv\Master OpenCV\images\input.jpg")

#acum vom face imaginea la 3/4 din dimensiunea originala
image_scaled =cv2.resize(image, None,fx=0.75, fy=0.75)

cv2.imshow('Scaling - Linear Interpolation', image_scaled)
cv2.waitKey()

#acum vom dimensiona imaginea de doua ori
img_scaled=cv2.resize(image,None, fx=2,fy=2,interpolation =cv2.INTER_CUBIC)

cv2.imshow("Scaling - Cubic Interpolation", img_scaled)
cv2.waitKey()

#Să oblic re-dimensionarea prin stabilirea dimensiunilor exacte
img_scaled = cv2.resize(image,(900,400),interpolation = cv2.INTER_AREA)

cv2.imshow("Scaling - Skewed size", img_scaled)
cv2.waitKey()

cv2.destroyAllWindows()

