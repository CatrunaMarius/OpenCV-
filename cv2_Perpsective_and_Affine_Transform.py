import cv2
import numpy as np
import matplotlib.pyplot as pltestc

image = cv2.imread('D:\Programare\cv\Master OpenCV\images\scan.jpg')

cv2.imshow('Original', image)
cv2.waitKey()

#Coordonatele celor 4 colțuri ale imaginii originale
points_A = np.float32([[320,15],[700,215],[85,610],[530,780]])

## Coordonatele celor 4 colțuri ale ieșirii dorite
# Folosim un raport dintr-un document A4 1: 1.41
points_B = np.float32([[0,0],[420,0],[0,594],[420,594]])

## Utilizați cele două seturi de patru puncte pentru a calcula
# matricea de transformare a perspectivei, M
m = cv2.getPerspectiveTransform(points_A, points_B)

warped = cv2.warpPerspective(image, m, (420,594))

cv2.imshow('warpPerspective', warped)
cv2.waitKey()
cv2.destroyAllWindows()

#La afine transformările  aveți nevoie doar de 3 coordonate pentru a obține transformarea corectă

image = cv2.imread('D:\Programare\cv\Master OpenCV\images\ex2.jpg')
rows,cols,ch = image.shape

cv2.imshow('Original', image)
cv2.waitKey()

#Coordonatele celor 4 colțuri ale imaginii originale
points_a = np.float32([[320,15],[700,215],[85,610]])

# Coordonatele celor 4 colțuri ale ieșirii dorite
# Folosim un raport dintr-un document A4 1: 1.41
points_b = np.float32([[0,0],[420,0],[0,594]])

# Utilizați cele două seturi de patru puncte pentru a calcula
# matricea de transformare a perspectivei, M

m = cv2.getAffineTransform(points_a,points_b)

warped = cv2.warpAffine(image,m,(cols,rows))

cv2.imshow('warpPerspective', warped)
cv2.waitKey()
cv2.destroyAllWindows()