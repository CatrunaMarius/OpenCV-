
#cv2.getRotationMatrix2D(rotation_center_x, rotation_center_y, angle of rotation, scale)

import cv2
import numpy as np

image = cv2.imread('D:\Programare\cv\Master OpenCV\images\input.jpg')
height, width = image.shape[:2]

#ACESTE DOUA FUCNCTI DE MAI JOS SUNT NECESARE PT A PUTEA ROTI IMAGINEA
#Imparte la doi pentru a rota imaginea in jurul centrului
rotation_matrix = cv2.getRotationMatrix2D((width/2, height/2),270, .6)

#transforma imaginea intro imagine  mai mica
rotation_image = cv2.warpAffine(image, rotation_matrix,(width,height))#in locul lui width si height poti aduga o rezolutie pe care o vrei tu
####################################################

cv2.imshow('Rotated Image', rotation_image)
cv2.waitKey()
cv2.destroyAllWindows()

#O ALTA OPTIUNE DE ROTATIE
img = cv2.imread("D:\Programare\cv\Master OpenCV\images\input.jpg")

rotated_image = cv2.transpose(img)

cv2.imshow('Rotated Image - Metoda 2', rotated_image)
cv2.waitKey()
cv2.destroyAllWindows()

#acum pe orizontal flip
flipped = cv2.flip(image,1)

cv2.imshow('Horizontal Flip', flipped)
cv2.waitKey()
cv2.destroyAllWindows()
